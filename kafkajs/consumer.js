const { Kafka } = require('kafkajs')

const host = '127.0.0.1'

const kafka = new Kafka({
  clientId: 'my-app',
  brokers: [`${host}:9092`,]
})

const consumer = kafka.consumer({ groupId: 'test-group' })

const run = async () => {  
  // Consuming
  await consumer.connect()
  await consumer.subscribe({ topic: 'test-topic', fromBeginning: true })

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      console.log({
        partition,
        offset: message.offset,
        value: message.value.toString(),
      })
    },
  })
}

run().catch(console.error)