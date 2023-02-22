import os

from kafka import KafkaConsumer


consumer = KafkaConsumer(
    "dbi-kafka-workshop",
    bootstrap_servers=['super-satyr-10812-eu1-kafka.upstash.io:9092'],
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_SSL',
    sasl_plain_username=os.environ.get("UPSTASH_KAFKA_USERNAME"),
    sasl_plain_password=os.environ.get("UPSTASH_KAFKA_PASSWORD"),
    group_id="$GROUP_NAME",
    auto_offset_reset="earliest",
)
for each in consumer:
    print(each)

consumer.close()
