from kafka import KafkaConsumer
from datetime import datetime

consumer = KafkaConsumer('test', bootstrap_servers='54.186.176.84:9092')

for msg in consumer:
    nw = datetime.utcnow()
    rc = datetime.strptime(msg.value, '%Y-%m-%d %H:%M:%S.%f')
    print(nw,rc,nw - rc)
