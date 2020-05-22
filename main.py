#!/usr/bin/python
# import os
import sys
import csv
import time
import random
from selenium import webdriver
# from selenium.common import exceptions as e
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# VARIABLES
# Configuration settings for webdriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_experimental_option("useAutomationExtension", False),
wait_time = 30
short_wait_time = 5
user = ""
password = ""
instanceURL = ""

driver = webdriver.Chrome(options=options, executable_path="/usr/bin/chromedriver")
wait = WebDriverWait(driver, wait_time)
short_wait = WebDriverWait(driver, short_wait_time)


# store person strings in list
def parse_csv(file):
    people = []
    family_id = []
    checkin_type = []
    with open('./csv/' + file, 'r') as file:
        read_csv = csv.reader(file, delimiter=',')
        for row in read_csv:
            checkin_type.append(row[0])
            people.append(row[1])
            family_id.append(row[2])
    return checkin_type, people, family_id


# Zip up lists then shuffle the zipped list.
# After the list is shuffled unzip it back into 
# the list so they can be passed into the for loop
# for processing.
def shuffle(c, x, y):
    mapped = list(zip(c, x, y))
    random.shuffle(mapped)
    c[:], x[:], y[:] = zip(*mapped)
    return c, x, y


def child_checkin(checkin_type, person, family_id):
    try:
        if short_wait.until(ec.title_contains("Login")):
            input_login_username = driver.find_element(
                By.CSS_SELECTOR, "input[id$='tbUserName']")
            input_login_username.send_keys(user)
            input_login_password = driver.find_element(
                By.CSS_SELECTOR, "input[id$='tbPassword']")
            input_login_password.send_keys(password)
            btn_login = driver.find_element(By.CSS_SELECTOR, "a[id$='btnLogin']")
            btn_login.click()
    except:
        pass

    if wait.until(ec.title_contains("Welcome")) and checkin_type != "BC":
        time.sleep(1)
        btn_start = wait.until(ec.element_to_be_clickable(
            (By.CSS_SELECTOR, "a.btn-checkin")))
        btn_start.click()
        if short_wait.until(ec.title_contains("Search")) and checkin_type != "BC":
            time.sleep(2)
            # PAGE - FAMILY SEARCH
            input_fam_search = short_wait.until(ec.presence_of_element_located(
                (By.CSS_SELECTOR, "input[id$='txtName']")))
            input_fam_search.send_keys(person)
            btn_search = short_wait.until(ec.presence_of_element_located(
                (By.CSS_SELECTOR, "a[id$='lbSearch'")))
            btn_search.click()
        try:
            if wait.until(ec.title_contains("Family Select")):
                time.sleep(1)
                # PAGE - FAMILY SELECT
                btn_family = wait.until(ec.element_to_be_clickable(
                    (By.CSS_SELECTOR, "div[data-target*='{}']".format(family_id))))
                btn_family.click()
        except:
            pass

    if checkin_type == "BC":
        script = ''' let barcode =''' + person + '''; $('#hfSearchEntry').val(barcode); window.location = "javascript:__doPostBack('hfSearchEntry', 'Wedge_Entry')";'''
        driver.execute_script(script)

    try:
        if wait.until(ec.title_contains("Person Select")):
            time.sleep(2)
            btn_person = wait.until(ec.element_to_be_clickable(
                (By.CSS_SELECTOR, "div[id$='pnlPersonButton']")))
            btn_person.click()
            btn_person_next = wait.until(ec.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[id$='lbSelect']")))
            btn_person_next.click()
    except:
        pass

    try:
        if short_wait.until(ec.title_contains("Group Type Select")):
            time.sleep(1)
            btn_area = short_wait.until(ec.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[id$='lbSelect']")))
            btn_area.click()

        if short_wait.until(ec.title_contains("Group Select")):
            time.sleep(1)
            btn_group = short_wait.until(ec.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[id$='lbSelect']")))
            btn_group.click()

        if short_wait.until(ec.title_contains("Time Select")):
            time.sleep(1)
            btn_time = short_wait.until(ec.element_to_be_clickable(
                (By.CSS_SELECTOR, ".checkin-timelist .btn-checkbox")))
            btn_time.click()
            btn_checkin = driver.find_element(By.CSS_SELECTOR, "a[id$='lbSelect']")
            btn_checkin.click()
    except:
        pass


def main():
    # Loop forever and iterate over csv files
    # getting people values and id values.
    driver.get(instanceURL)
    while True:
        checkin_type, people, family_id = parse_csv(sys.argv[1])
        checkin_type, people, family_id = shuffle(checkin_type, people, family_id)

        for checkin, person, family in zip(checkin_type, people, family_id):
            print("Type: ", checkin, person, family)
            child_checkin(checkin, person, family)


if __name__ == "__main__":
    main()
