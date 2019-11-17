from kafka import KafkaProducer
from datetime import datetime
import time
producer = KafkaProducer(bootstrap_servers='54.186.176.84:9092')

for _ in range(1):
    dt = datetime.now()
    print(dt)
    producer.send('test', b'{}'.format(dt))
producer.flush()
