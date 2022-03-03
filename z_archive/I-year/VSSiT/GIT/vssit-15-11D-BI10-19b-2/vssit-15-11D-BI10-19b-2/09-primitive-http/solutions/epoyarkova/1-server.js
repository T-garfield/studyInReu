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

  socket.on('data', () => {

    const content = `<html>
<body>
<h1> epoyarkova
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

  // socket.write(`HTTP/1.1
  // X-Tracking-Ref: <0.2428.7420>
  // Content-Type: text/html; charset=ISO-8859-1
  
  // <epoyarkova>
  // `);

  //socket.pipe(socket); //  Выходной поток socket (принимаемые данные) перенаправляем во входной поток того же объекта socket (данные для отправки)
});

server.listen(8080, function() { //'listening' listener
  console.log('server bound');
});
