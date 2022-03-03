// Example from Node documentation
// https://nodejs.org/api/net.html#net_net_createserver_options_connectionlistener

'use strict';

var net = require('net');

var server = net.createServer(function(socket) { //'connection' listener
  console.log('client connected');

  socket.on('end', function() {
    console.log('client disconnected');
  });

  socket.on('data', () => {

      const content = `<html>
      <body>
        <h1> akhayretdinova </h1> 
        <h3> ${new Date().toString()} </h3>
      </body>
      </html>`
      const headers = `HTTP/1.1 200 OK
      Content-Length: ${content.length}`
      socket.write(`${headers}\r\n`);
      socket.write (`\r\n${content}`);
      socket.end();
  });

});

server.listen(8080, function() { //'listening' listener
  console.log('server bound');
});