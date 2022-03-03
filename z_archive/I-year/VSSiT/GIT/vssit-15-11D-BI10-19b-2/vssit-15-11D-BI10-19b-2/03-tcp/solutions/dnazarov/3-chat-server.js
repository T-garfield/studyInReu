/**
 * Created by alykoshin on 26.09.15.
 */

'use strict';

var net = require('net');

var sockets = [];

var nicknames = [];

var server = net.createServer(function(socket) { // 'connection' listener
  console.log('client connected');
  sockets.push(socket);
  nicknames.push(undefined);

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

  socket.write('enter your nickname /nick ..');

  socket.write('kick someone /kick ..');

  socket.write('get the list of clients  /list ..');


  socket.on('data', function(buffer) {
    console.log('* client.on(\'data\') /data received/:');
    console.log('%s', buffer.toString());

    for (var i=0; i<sockets.length; i++) {
      sockets[ i ].write(buffer);
    }

    var cmd = buffer.toString().trim();
    if (cmd === '/quit') {
        socket.destroy(); 
    }
    
    if (cmd.substr(0,5)==='/nick') {
        socket.write(' Saved');
        nicknames[sockets.indexOf(socket)]=cmd.slice();
    }
    
    if (cmd.substr(0,5)==='/kick') {
        sockets[nicknames.indexOf(cmd.slice())].end();
    }
   
    if (cmd==='/list'){
     for (var i=0; i<sockets.length; i++) {
      socket.write(' ' + nicknames[i]) ;
         };
      };

    });

});

server.listen(8124, function() { // 'listening' listener
  console.log('server bound');
});