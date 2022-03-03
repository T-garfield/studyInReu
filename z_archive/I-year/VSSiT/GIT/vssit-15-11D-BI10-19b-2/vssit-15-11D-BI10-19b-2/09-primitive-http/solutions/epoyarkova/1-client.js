// Example from Node documentation
// https://nodejs.org/api/net.html#net_net_createserver_options_connectionlistener

'use strict';

var net = require('net');
const fs = require("fs");

var client = net.connect({ port: 80, host: "www.google.ru" }, function() { //'connect' listener
  console.log('connected to server!');
  client.write(`GET / HTTP/1.1
  Host: www.google.ru:80

  `);
});

client.on('data', function(data) {
  console.log(data.toString());
  fs.writeFileSync("response1.txt", data);
  client.end();
});

client.on('end', function() {
  console.log('disconnected from server');
});
