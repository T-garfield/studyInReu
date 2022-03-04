/**
 * Created by alykoshin on 26.09.15.
 */

'use strict';

var net = require('net');

var sockets = [];
var niknames = [];
var server = net.createServer(function(socket) { 
  console.log('client connected');
  sockets.push(socket);
  niknames.push(undefined)

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

socket.write('Now you are underfind,please set your nick with /nick yournickhear. ')

socket.write('To kick someone use /kick hisnickname. ')

socket.write('To get list of clients use /list. ')

socket.on('data', function(buffer) {
  console.log('* client.on(\'data\') /data received/:');
  console.log('%s', buffer.toString());

  for (var i=0; i<sockets.length; i++) {
    sockets[ i ].write(buffer) ;
  }

  var cmd = buffer.toString().trim();
  if (cmd === '/quit') {
    socket.destroy()
  }
  if (cmd.substr(0,5)==='/nick'){
    socket.write(' Saved')
    niknames[sockets.indexOf(socket)]=cmd.slice(6)
  }
  if (cmd.substr(0,5)==='/kick'){
    sockets[niknames.indexOf(cmd.slice(6))].end()
  }
  if (cmd==='/list'){
    for (var i=0; i<sockets.length; i++) {
      socket.write(' ' + niknames[i])
    }}
  });

});   


server.listen(8124, function() {
  console.log('server bound');
});