'use strict';

var net = require('net');

var server = net.createServer(function(socket) {
    console.log('client connected');

    socket.on('end', function() {
    console.log('client disconnected');
    });

    socket.on('data', ()=> {
    const content = `eremina ${new Date().toString()}`
    const headers = `HTTP/1.1 200 OK
    Content-Length: ${content.length}`
    socket.write(`${headers}/1`);
    socket.write(`/1${content}`);
    socket.end();
    });
});

server.listen(8080, function() {
 console.log('server bound');
});
