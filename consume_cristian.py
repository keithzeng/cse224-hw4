from kafka import KafkaConsumer
from kafka import KafkaProducer
from datetime import datetime

consumer = KafkaConsumer('test', bootstrap_servers='54.186.176.84:9092')
producer = KafkaProducer(bootstrap_servers='54.186.176.84:9092')
for msg in consumer:
    producer.send('back', b'{},{}'.format(msg.value,datetime.now()))
