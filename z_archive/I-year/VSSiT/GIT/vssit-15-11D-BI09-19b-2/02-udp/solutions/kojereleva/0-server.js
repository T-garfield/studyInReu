/**
 * Created by alykoshin on 03.10.15.
 */

'use strict';

var dgram = require("dgram");

var BIND_PORT = 41234;

var server = dgram.createSocket("udp4");

server.on("message", function (msg, rinfo) {
  console.log("* server.on(\'message\') msg: \'%s\', rinfo: %j", msg, rinfo);
});

server.on("listening", function () {
  console.log("* server.on(\'listening\')");
  console.log('  server.address(): %j', server.address());
});

server.on("error", function (error) {
  console.log('* server.on(\'error\'): error: %j', error);
  server.close();
});

server.bind(BIND_PORT);
