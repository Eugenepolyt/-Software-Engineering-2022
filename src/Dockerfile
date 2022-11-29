FROM ubuntu:latest
MAINTAINER Borisov Eugene 'jykaswift@gmail.com'
RUN apt-get update -qy
RUN apt-get install -qy python3.10 python3-pip python3.10-dev
RUN apt-get install -y nodejs
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python3","main.py"]
