/**
 * Created by alykoshin on 03.10.15.
 */

'use strict';

var dgram = require("dgram");

var BIND_PORT = 41234;          // default value - random
var BIND_INTERFACE = '0.0.0.0'; // default value - '0.0.0.0'

// dgram.createSocket(type[, callback])
// dgram.createSocket(options[, callback])
var server = dgram.createSocket("udp4");

// Event: 'message'
server.on("message", function (msg, rinfo) {
  console.log("* server.on(\'message\') msg: \'%s\', rinfo: %j", msg, rinfo);

  var message = new Buffer('Message from server');

  console.log('* server.send(): message: \'%s\', host:port: %s:%d', message, rinfo.address, rinfo.port);

// socket.send(buf, offset, length, port, address[, callback])
  server.send(message, 0, message.length, rinfo.port, rinfo.address, function(error, bytes) {

    console.log('* server.send(): callback(): err: %j, bytes:', error, bytes);
  });
});

// Event: 'listening'
server.on("listening", function () {
  console.log("* server.on(\'listening\')");

  // socket.address()
  console.log('  server.address(): %j', server.address());
});

// Event: 'close'
server.on("close", function () {
  console.log('* server.on(\'close\')');
});

// Event: 'error'
server.on("error", function (error) {
  console.log('* server.on(\'error\'): error: %j', error);

  // socket.close([callback])
  server.close();
});

// socket.bind([port][, address][, callback])
// socket.bind(options[, callback])
//   option: { port: Number [, address: String = '0.0.0.0'] [, exclusive: Boolean = false] }
server.bind(BIND_PORT, BIND_INTERFACE /*, callback */);