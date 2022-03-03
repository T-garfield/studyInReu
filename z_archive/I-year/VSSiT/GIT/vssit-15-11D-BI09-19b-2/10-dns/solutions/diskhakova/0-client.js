/**
 * Created by alykoshin on 10.10.15.
 */

'use strict';

var net = require('net');

var server = net.createServer(function(socket) { //'connection' listener

console.log('client connected');

socket.on('end', function() {

console.log('client disconnected');
});

socket.on('data', ()=> {


//socket.write(`HTTP/1.0 200 OK\r\n\r\n`);

// const content = `<html>

//<body>

//<h1>Hello, World!</h1>

//</body>

//</html>`

const content = `yegorov ${new Date}`

// const headers = `HTTP/1.1 200 OK

//Date: Mon, 27 Jul 2009 12:28:53 GMT

//Server: Apache/2.2.14 (Win32)

//Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT

//Content-Length: ${content.length}

//Content-Type: text/html

//Connection: Closed`

const headers = `HTTP/1.1 200 OK

Content-Length: ${content.length}
`

socket.write(`${headers}

${content}`);

//socket.end();

});

});

server.listen(8124, function() { //'listening' listener

console.log('server bound');
});