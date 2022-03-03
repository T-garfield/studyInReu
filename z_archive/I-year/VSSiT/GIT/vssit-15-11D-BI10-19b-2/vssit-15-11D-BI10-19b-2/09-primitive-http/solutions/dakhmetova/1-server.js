// Example from Node documentation
// https://nodejs.org/api/net.html#net_net_createserver_options_connectionlistener

'use strict';

var net = require('net');

var server = net.createServer(function (socket) {
  console.log('CLIENT CONNECTED');

  socket.on('end', function () {
    console.log('CLIENT DISCONNECTED');
  });

  socket.on('data', () => {

    const content = `<html>
<body>
<h1> dakhmetova
<h2> ${new Date().toString()}
</h2>
</h1>
</body>
</html>`
    const headers = `HTTP/1.1 200 OK
Content-Length: ${content.length}`
    socket.write(`${headers}\r\n`);
    socket.write(`\r\n${content}`);
    socket.end();
  });

});

server.listen(8080, function () {
  console.log('SERVER BOUND');
});
