// Example from Node documentation
// https://nodejs.org/api/net.html#net_net_createserver_options_connectionlistener

'use strict';

var net = require('net');
const fs = require("fs");

var server = net.createServer(function(socket) { //'connection' listener
  console.log('client connected');

  socket.on('data', function(buffer) {
    console.log('* server.on(\'data\') /data received/:');
    console.log('%s', buffer.toString());
    fs.writeFileSync("response.txt", buffer);
  });

  

  socket.on('end', function() {
    console.log('client disconnected');
  });

  socket.write('hello\r\n');

  //socket.pipe(socket); //  Выходной поток socket (принимаемые данные) перенаправляем во входной поток того же объекта socket (данные для отправки)
});

server.listen(8124, function() { //'listening' listener
  console.log('server bound');
});
