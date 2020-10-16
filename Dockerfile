FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip default-libmysqlclient-dev build-essential

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
COPY . /app

CMD ["python3", "index.py"]
