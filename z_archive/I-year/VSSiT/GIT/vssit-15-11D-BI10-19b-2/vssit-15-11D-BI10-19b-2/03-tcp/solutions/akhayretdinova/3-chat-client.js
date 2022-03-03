
var connect = require('net');

var client = connect.connect('8124', 'localhost');

client.on('data', function(buffer) {
  console.log('* client.on(\'data\') /data received/:');
  console.log('%s', buffer.toString());
});

client.on('connect', function() {
  console.log('* client.on(\'connect\') /connection successfully established/');
  client.write('Hello from client');
});

client.on('end', function() {
  console.log('* client.on(\'end\') /disconnected from server/:');
});

client.on('close', function(had_error) {
  console.log('* client.on(\'close\') /socket fully closed/: had_error: %j', had_error);
  process.stdin.pause();
});

process.stdin.on('data', function (chunk) {
  client.write(chunk.toString());
});

