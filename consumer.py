from kafka import KafkaConsumer
from json import loads
import db
from config import kafka

consumer = KafkaConsumer(
     kafka["topic"],
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

db.createTable()

for message in consumer:
    message = message.value
    db.insertRow(message)