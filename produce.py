from kafka import KafkaProducer
from datetime import datetime

producer = KafkaProducer(bootstrap_servers='54.186.176.84:9092')

for _ in range(10):
    producer.send('test', b'{}'.format(datetime.utcnow()))
producer.flush()
