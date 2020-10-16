from kafka import KafkaConsumer
from json import loads
import db
from config import kafka


class Consumer:

    def __init__(self):
        self.consumer = KafkaConsumer(
            kafka["topic"],
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: loads(x.decode('utf-8')))

    def receive(self):
        # for testing purpose, creating new table everytime
        db.createTable()
        for message in self.consumer:
            message = message.value
            db.insertRow(message)