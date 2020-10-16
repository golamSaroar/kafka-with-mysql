from stream_processing import kafka_producer
from json import load
from time import sleep

if __name__ == '__main__':
    kafka_producer = kafka_producer.Producer()

    with open('stream_processing/data.json', encoding="utf-8") as f:
        data = load(f)

    for e in range(1000):
        kafka_producer.send_message(data)
        sleep(2)
