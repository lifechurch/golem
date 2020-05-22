FROM alpine:latest

RUN apk update
RUN apk add python
RUN apk add curl
RUN apk add chromium-chromedriver
RUN apk add chromium
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python get-pip.py

COPY . /golem
WORKDIR /golem

RUN pip install -r requirements.txt

CMD ["python", "main.py", "attender.csv"]