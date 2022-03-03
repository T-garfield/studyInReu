/**
 * Created by alykoshin on 25.09.15.
 */

'use strict';

var net    = require('net');
var config = require('./2-config').server;

// net.createServer([options][, connectionListener])
//   options = { allowHalfOpen: false, pauseOnConnect: false }
var server = net.createServer();

// server.listen(port[, hostname][, backlog][, callback])
// server.listen(path[, callback])
// server.listen(handle[, callback])
// server.listen(options[, callback])
//   options Object - Required. Supports the following properties:
//     port Number - Optional.
//     host String - Optional.
//     backlog Number - Optional.
//     path String - Optional.
//     exclusive Boolean - Optional.
//   callback Function - Optional.
server.listen({ port: config.port, host: config.host }, null);

server.on('listening', function() {
  console.log('* server.on(\'listening\')');

  var address = server.address();
  console.log('  server.address(): %j', address);
});

server.on('connection', function(socket) {
  console.log('* server.on(\'connection\') /client connected/:');
  console.log('  socket.remoteAddress: %s, socket.remoteFamily: %s, socket.remotePort: %d', socket.remoteAddress, socket.remoteFamily, socket.remotePort);
  server.getConnections(function(err, count) {
    console.log('  server.getConnections(): err: %j, count: %d', err, count);
  });

  socket.on('end', function() {
    console.log('* client.on(\'end\') /client disconnected/');
  });

  socket.on('error', function(err) {
    console.log('* client.on(\'error\') err:', err);
  });

  socket.write('Welcome to server\r\n');
  socket.pipe(socket);

});

server.on('close', function() {
  console.log('* server.on(\'close\')');
});

var MAX_ATTEMPT = 3,
  RETRY_TIMEOUT = 1000;
var attempt = 1;

server.on('error', function(err) {
  console.log('* client.on(\'error\') /error occurs/: err: %j', err);

  if (err.code === 'EADDRINUSE') {

    if (attempt++ > MAX_ATTEMPT) {
      console.log('  Max attempt reached, exiting');
    }

    console.log('  Address in use, retrying...');

    setTimeout(function () {
      server.close();
      server.listen({ port: config.port, host: config.host });
    }, RETRY_TIMEOUT);
  } else if (err.code === 'EACCES') {
    console.log('  Insufficient privileges, Try to run with sudo');
  }

});
