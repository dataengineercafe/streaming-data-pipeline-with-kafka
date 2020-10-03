const { Kafka } = require('kafkajs')

const host = '127.0.0.1'

const kafka = new Kafka({
  clientId: 'my-app',
  brokers: [`${host}:9092`,]
})

const producer = kafka.producer()

const run = async () => {
  // Producing
  await producer.connect()
  await producer.send({
    topic: 'test-topic',
    messages: [
      { value: 'Hello KafkaJS user!' },
    ],
  })
  await producer.disconnect()
}

run().catch(console.error)