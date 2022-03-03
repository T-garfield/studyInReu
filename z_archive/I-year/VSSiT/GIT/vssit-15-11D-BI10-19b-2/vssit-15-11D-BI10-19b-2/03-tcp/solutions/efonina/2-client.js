'use strict';

var net = require('net');
var config = require('./2-config').client;

// socket.connect(options[, connectListener])
//   options argument should be an object which specifies:
//     port: Port the client should connect to (Required).
//     host: Host the client should connect to. Defaults to 'localhost'.
//     localAddress: Local interface to bind to for network connections.
//     localPort: Local port to bind to for network connections.
//     family : Version of IP stack. Defaults to 4.
//     lookup : Custom lookup function. Defaults to dns.lookup.
//   For local domain sockets, options argument should be an object which specifies:
//     path: Path the client should connect to (Required).
// socket.connect(port[, host][, connectListener])#
// socket.connect(path[, connectListener])
var client = net.connect({ port: config.port, host: config.host }, null);

client.on('lookup', function(err, address, family) {
  console.log('* client.on(\'lookup\') /after resolving the hostname but before connecting/: err: %j, address: %s, family: %s', err, address, family);
});

client.on('connect', function() {
  console.log('* client.on(\'connect\') /connection successfully established/');
  console.log('  client.remoteAddress: %s, client.remoteFamily: %s, client.remotePort: %d', client.remoteAddress, client.remoteFamily, client.remotePort);
  console.log('  client.localAddress: %s,  client.localFamily: %s,  client.localPort: %d',  client.localAddress,  client.localFamily,  client.localPort);
  console.log('  client.address(): %j', client.address());
});

client.on('data', function(buffer) {
  console.log('* client.on(\'data\') /data received/:');
  console.log('%s', buffer.toString());

  client.end();
});

client.on('end', function() {
  console.log('* client.on(\'end\') /disconnected from server/:');
  console.log('  bytesRead: %d',    client.bytesRead);
  console.log('  bytesWritten: %d', client.bytesWritten);
});

client.on('timeout', function() {
  console.log('* client.on(\'timeout\') /timed out from inactivity/');
});

client.on('drain', function() {
  console.log('* client.on(\'drain\') /write buffer is empty/');
});

client.on('error', function(err) {
  console.log('* client.on(\'error\') /error occurs/: err: %j', err);
});

client.on('close', function(had_error) {
  console.log('* client.on(\'close\') /socket fully closed/: had_error: %j', had_error);
});
