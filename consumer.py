from stream_processing import kafka_consumer


if __name__ == '__main__':
    receiver = kafka_consumer.Consumer()
    receiver.receive()
