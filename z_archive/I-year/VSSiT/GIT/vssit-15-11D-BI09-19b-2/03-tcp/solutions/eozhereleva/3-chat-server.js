/**
 * Created by alykoshin on 26.09.15.
 */

'use strict';

var net = require('net');

var sockets = [];

var server = net.createServer(function(socket) { // 'connection' listener
  console.log('client connected');
  sockets.push(socket);

  for (var i=0; i<sockets.length; i++) {
    sockets[ i ].write('* client from '+socket.remoteAddress+':'+socket.remotePort+' connected\n');
  }

  socket.on('end', function() {
    console.log('client disconnected');
    var idx = sockets.indexOf(socket);
    if (idx > -1) {
      sockets.splice(idx, 1);
    }

    for (var i=0; i<sockets.length; i++) {
      sockets[ i ].write('* client from '+socket.remoteAddress+':'+socket.remotePort+' disconnected\n');
    }

  });

  socket.on('error', function(err) {
    console.log('* client.on(\'error\') err:', err);
  });

  socket.write('hello from server\r\n');

  socket.on('data', function(buffer) {
    console.log('* client.on(\'data\') /data received/:');
    console.log('%s', buffer.toString());

    for (var i=0; i<sockets.length; i++) {
      sockets[ i ].write(buffer);
    }

    var cmd = buffer.toString().trim();
    if (cmd === '/quit') {
      socket.end();
    }

  });

});
if (cmd === '/list') {
  for (let i = 0; i < sockets.length; i ++){
    console.log('nickname: ' + sockets[i].name);
  }   
}
if (cmd.startsWith('/nick')) {
  socket.name = cmd.split(" ")[1];
}
if (cmd.startsWith('/kick')) {
  let nickname = cmd.split(" ")[1];
  for (let i = 0; i < sockets.length; i ++)
    if (sockets[i].name === nickname) sockets[i].end();
}

server.listen(8124, function() { // 'listening' listener
  console.log('server bound');
});

