from kafka import KafkaConsumer

consumer = KafkaConsumer('topic1')
for msg in consumer:
    print(msg)
