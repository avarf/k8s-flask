FROM ubuntu:18.04

MAINTAINER Ali Varfan

RUN apt-get update  --fix-missing
RUN apt-get install -y python3
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-setuptools
RUN apt-get install -y python3-pip

COPY code /code

EXPOSE 5000

WORKDIR /code

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"
