from time import sleep
from json import load, dumps
from kafka import KafkaProducer
from config import kafka

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

def sendMessage(data):
    producer.send(kafka["topic"], value=data)

with open('data.json') as f:
  data = load(f)

for e in range(1000):
    sendMessage(data)
    sleep(5)