/**
 * Created by alykoshin on 03.10.15.
 */

'use strict';

var dgram = require("dgram");

var SERVER_PORT = 41234;
var SERVER_HOST = 'localhost'; // 127.0.0.1

var client = dgram.createSocket("udp4");

var message = Buffer.from('Message from client');

client.send(message, 0, message.length, SERVER_PORT, SERVER_HOST, function(error, bytes) {
  console.log('* client.send(): callback(): err: %j, bytes:', error, bytes);
  client.close();
});

console.log('Finished');
