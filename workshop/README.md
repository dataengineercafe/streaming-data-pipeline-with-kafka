# Workshop on Streaming Data Pipeline with Kafka

## Topics

```bash
bin/kafka-topics.sh --bootstrap-server 0.0.0.0:9092 --create --topic tisco
bin/kafka-topics.sh --bootstrap-server 0.0.0.0:9092 --create --topic test-topic
```

```bash
bin/kafka-topics.sh --bootstrap-server 0.0.0.0:9092 --list
```

```bash
bin/kafka-topics.sh --bootstrap-server 0.0.0.0:9092 --describe
```

## Producer

```bash
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test-zkan
```

```bash
bin/kafka-topics.sh --bootstrap-server 0.0.0.0:9092 --create --topic test-zkan-x --partitions 2
```

```bash
bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test-zkan-x --property "parse.key=true" --property "key.separator=:"
```

## Consumer

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-zkan
```

```bash
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test-zkan --group mygroup --from-beginning
```

## Consumer Group

```bash
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list
```

```bash
bin/kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --all-groups
```
