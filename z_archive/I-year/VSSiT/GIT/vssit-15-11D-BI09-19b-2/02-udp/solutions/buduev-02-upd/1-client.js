/**
 * Created by alykoshin on 03.10.15.
 */

'use strict';

var dgram = require("dgram");

// dgram.createSocket(type[, callback])
// dgram.createSocket(options[, callback])
var client = dgram.createSocket('udp4'); // Will use random socket to send UDP datagram

// Event: 'message'
client.on("message", function (msg, rinfo) {
  console.log("* client.on(\'message\') msg: \'%s\', rinfo: %j", msg, rinfo);
});

// Event: 'listening' - not appicable to pure client
client.on("listening", function () {
  console.log("* client.on(\'listening\')");

  // socket.address()
  console.log('  client.address(): %j', client.address());
});

// Event: 'close'
client.on("close", function () {
  console.log('* client.on(\'close\')');
});

// Event: 'error'
client.on("error", function (error) {
  console.log('* client.on(\'error\'): error: %j', error);

  // socket.close([callback])
  client.close();
});

var SERVER_PORT = 41234;
var SERVER_HOST = '127.0.0.1';
var message = Buffer.from('Message from client');

console.log('* client.send(): message: \'%s\', host:port: %s:%d', message, SERVER_HOST, SERVER_PORT);

// socket.send(buf, offset, length, port, address[, callback])
client.send(message, 0, message.length, SERVER_PORT, SERVER_HOST, function(error, bytes) {

  console.log('* client.send(): callback(): err: %j, bytes:', error, bytes);
});
