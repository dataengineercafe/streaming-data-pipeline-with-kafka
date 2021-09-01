const { Kafka } = require('kafkajs')

const host = '127.0.0.1'

const kafka = new Kafka({
  clientId: 'my-app',
  brokers: [`${host}:9092`,]
})

const consumer = kafka.consumer({ groupId: 'test-consumer-group' })

const consume = async callback => {
  await consumer.connect()
  await consumer.subscribe({ topic: 'odds', fromBeginning: true })

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      console.log({
        partition,
        offset: message.offset,
        value: message.value.toString(),
      })
      callback({ message })
    },
  })
}

module.exports = consume
