import json

from confluent_kafka import Consumer


topics = ['test-topic',]

# Doc: docs.confluent.io/current/clients/confluent-kafka-python/
c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(topics)

while True:
    msg = c.poll(1.0)
    if msg is None:
        continue

    data = json.loads(msg.value().decode('utf-8'))
    print(data['text'])
    print('---')

c.close()
