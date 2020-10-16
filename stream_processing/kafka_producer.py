from kafka import KafkaProducer
from config import kafka
from json import dumps


class Producer:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                      value_serializer=lambda x:
                                      dumps(x).encode('utf-8'))

    def send_message(self, data):
        self.producer.send(kafka["topic"], value=data)
