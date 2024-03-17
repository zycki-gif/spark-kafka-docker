from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

while True:
    data = {'number' : 100}
    producer.send('test', json.dumps(data).encode('utf-8'))
    time.sleep(1)
