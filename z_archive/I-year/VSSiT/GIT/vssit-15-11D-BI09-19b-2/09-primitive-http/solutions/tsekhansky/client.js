'use strict';

var net = require('net');

var client = net.connect({ port: 80, host: 'www.google.ru' }, function () { //'connect' listener
    console.log('connected to server!');
    client.write('GET\r\n');
});

client.on('data', function (data) {
    console.log(data.toString());
    client.end();
});

client.on('end', function () {
    console.log('disconnected from server');
});
