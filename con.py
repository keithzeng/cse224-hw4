from kafka import KafkaConsumer
from datetime import datetime

consumer = KafkaConsumer('back', bootstrap_servers='54.186.176.84:9092')

for msg in consumer:
    t1,t2 = msg.value.split(',')
    t3 = t2# datetime.fromtimestamp(long(msg.timestamp) / 1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')
    t1 = datetime.strptime(t1, '%Y-%m-%d %H:%M:%S.%f')
    t4 = datetime.now()
    # print(str(t1),t2,t3,str(t4),t4-t1)
    print((t4 - t1).microseconds)
