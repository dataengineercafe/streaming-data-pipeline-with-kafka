const express = require('express')
const app = express()
const http = require('http')
const server = http.createServer(app)

const { Server } = require('socket.io')
const io = new Server(server)

const consume = require('./consumer')

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html')
})

consume(({ message }) => {
  io.sockets.emit('message', message.value.toString())
})

io.on('connection', socket => {
  console.log('a user connected')

  socket.on('disconnect', () => {
    console.log('user disconnected')
  })
})

server.listen(3000, () => {
  console.log('listening on *:3000')
})
