/**
 * Created by alykoshin on 10.10.15.
 */

'use strict';

var dns = require('dns');

var HOSTNAME = 'tweetch.tv';

var callback = function(err, rec) {
  if (err) {
    console.log('* callback(): err', err);
  }
  console.log('* callback(): rec', rec);
};

var options;

options = {
  all: false
};

dns.lookup(HOSTNAME, options, function(err, address, family) {
  console.log('* dns.lookup(): err: %j; address: %j; family: %d', err, address, family);
});

options = {
  all: true
};
dns.lookup(HOSTNAME, options, function(err, addresses) {
  console.log('* dns.lookup(): err: %j; addresses: %j', err, addresses);
});

dns.resolve(HOSTNAME, 'A', function(err, rec) {
  console.log('* dns.resolve(): err: %j; rec: %j', err, rec);
});

dns.resolveNs(HOSTNAME, function(err, rec) {
  console.log('* dns.resolveNs(): err: %j; rec: %j', err, rec);
});

//var ip = '5.255.255.5';
var ip = '217.70.184.38';
dns.reverse(ip, function(err, rec) {
  console.log('* dns.reverse(): err: %j; rec: %j', err, rec);
});
