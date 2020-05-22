# Golem

Golem is written in python and used for loadtesting rocks checkin process. To do this we use the selenium library to go through the checkin process just like a normal user would. Using Docker and Kubernetes we can spin up containers equal to the number of checkin kiosks that you would have on a weekend.

## Getting Started

This project uses Selenium Web Browser Automation `https://www.seleniumhq.org/`

Provide a csv file in the csv folder.
You can change the name of this file if you would like but you have to make sure to change the name in the docker file as well.
The data in this file needs to be checkin data from your past checkins, we used our easter service for the largest number of checkins possible, we then randomize the checkins for the best simulation possible for people checking in on the weekends.

Here is a example of data

``` text
BC,112253,138665
BC,176311,1783301
BC,10006163,41924
BC,160140,112688
BC,167065,96195
BC,210112,61570
BC,225048,191011
BC,167055,99247
BC,190534,35745
BC,140371,104746
BC,137029,1930481
BC,170965,60578
BC,102062,40006
FullName,Joe Bob,2213051
BC,106341,165980
FullName,"Bob, Joe",2200056
```

BC stands for barcode in this instance and the ID in the 3rd column is the group ID

## Configuring

Install Python 3.7
`https://www.python.org/downloads/`
Install Selenium
`pip install selenium`
Install Chrome WebDriver
`http://chromedriver.chromium.org/downloads`

Edit Dockerfile with correct information if needed
```
CMD ["python", "main.py", "file.csv"]
```

## Usage

``` shell
python main.py file.csv

or

sudo docker build -t golem/latest .
sudo docker container run -a stdout -a stdin -it golem/latest
```

## Dependencies

This project uses [pip]() for dependency management

```
pip -r requirements

```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/lifechurch/golem/tags).

## Authors

* **Jesse Barton** - *Initial work* - [jessebarton](https://github.com/jessebarton)
* **Cameron Pak** - *Initial work* - [cameronpak](https://github.com/cameronapak)

<!-- See also the list of [contributors](https://github.com/lifechurch/golem/contributors) who participated in this project. -->

## License

This project is licensed under and modeled after the ISC License - see the [LICENSE.md](LICENSE.md) file for details
