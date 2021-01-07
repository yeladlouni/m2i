from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(100):
    future = producer.send('topic1', key=b'%d' % i, value=b'message %d' %i)
    result = future.get(timeout=60)
    producer.flush()

