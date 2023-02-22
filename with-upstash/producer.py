import os
import sys

from kafka import KafkaProducer


producer = KafkaProducer(
    bootstrap_servers=['super-satyr-10812-eu1-kafka.upstash.io:9092'],
    sasl_mechanism='SCRAM-SHA-256',
    security_protocol='SASL_SSL',
    sasl_plain_username=os.environ.get("UPSTASH_KAFKA_USERNAME"),
    sasl_plain_password=os.environ.get("UPSTASH_KAFKA_PASSWORD"),
)

producer.send("dbi-kafka-workshop", sys.argv[1].encode("utf-8"))

producer.close()
