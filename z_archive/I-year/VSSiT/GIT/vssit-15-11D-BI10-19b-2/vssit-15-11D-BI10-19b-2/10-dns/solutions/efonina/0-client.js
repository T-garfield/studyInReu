/**
 * Created by alykoshin on 10.10.15.
 */

'use strict';

var dns = require('dns');

var HOSTNAME1 = 'apple.com'
var HOSTNAME2 = 'samsung.com'
var HOSTNAME3 = 'adobe.com'
var HOSTNAME4 = 'kinopoisk.ru'
var HOSTNAME5 = 'genius.com'



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

dns.lookup(HOSTNAME1, options, function(err, address, family) {
  console.log('* dns.lookup(1): err: %j; address: %j; family: %d', err, address, family);
});

dns.lookup(HOSTNAME2, options, function(err, address, family) {
  console.log('* dns.lookup(2): err: %j; address: %j; family: %d', err, address, family);
});

dns.lookup(HOSTNAME3, options, function(err, address, family) {
  console.log('* dns.lookup(3): err: %j; address: %j; family: %d', err, address, family);
});

dns.lookup(HOSTNAME4, options, function(err, address, family) {
  console.log('* dns.lookup(4): err: %j; address: %j; family: %d', err, address, family);
});

dns.lookup(HOSTNAME5, options, function(err, address, family) {
  console.log('* dns.lookup(5): err: %j; address: %j; family: %d', err, address, family);
});

options = {
  all: true
};

dns.lookup(HOSTNAME1, options, function(err, addresses) {
  console.log('* dns.lookup(1): err: %j; addresses: %j', err, addresses);
});

dns.lookup(HOSTNAME2, options, function(err, addresses) {
  console.log('* dns.lookup(2): err: %j; addresses: %j', err, addresses);
});
dns.lookup(HOSTNAME3, options, function(err, addresses) {
  console.log('* dns.lookup(3): err: %j; addresses: %j', err, addresses);
});
dns.lookup(HOSTNAME4, options, function(err, addresses) {
  console.log('* dns.lookup(4): err: %j; addresses: %j', err, addresses);
});
dns.lookup(HOSTNAME5, options, function(err, addresses) {
  console.log('* dns.lookup(5): err: %j; addresses: %j', err, addresses);
});

dns.resolve(HOSTNAME1, 'A', function(err, rec) {
  console.log('* dns.resolve(1): err: %j; rec: %j', err, rec);
});
dns.resolve(HOSTNAME2, 'A', function(err, rec) {
  console.log('* dns.resolve(2): err: %j; rec: %j', err, rec);
});
dns.resolve(HOSTNAME3, 'A', function(err, rec) {
  console.log('* dns.resolve(3): err: %j; rec: %j', err, rec);
});
dns.resolve(HOSTNAME4, 'A', function(err, rec) {
  console.log('* dns.resolve(4): err: %j; rec: %j', err, rec);
});
dns.resolve(HOSTNAME5, 'A', function(err, rec) {
  console.log('* dns.resolve(5): err: %j; rec: %j', err, rec);
});


dns.resolveNs(HOSTNAME1, function(err, rec) {
  console.log('* dns.resolveNs(1): err: %j; rec: %j', err, rec);
});
dns.resolveNs(HOSTNAME2, function(err, rec) {
  console.log('* dns.resolveNs(2): err: %j; rec: %j', err, rec);
});
dns.resolveNs(HOSTNAME3, function(err, rec) {
  console.log('* dns.resolveNs(3): err: %j; rec: %j', err, rec);
});
dns.resolveNs(HOSTNAME4, function(err, rec) {
  console.log('* dns.resolveNs(4): err: %j; rec: %j', err, rec);
});
dns.resolveNs(HOSTNAME5, function(err, rec) {
  console.log('* dns.resolveNs(5): err: %j; rec: %j', err, rec);
});


//var ip = '5.255.255.5';
var ip1 = '2.21.109.82';
var ip2 = '92.122.108.71'
var ip3 = '92.122.108.118'
var ip4 = '87.250.251.105'
var ip5 = '104.18.19.96'

dns.reverse(ip1, function(err, rec) {
  console.log('* dns.reverse(1): err: %j; rec: %j', err, rec);
});
dns.reverse(ip2, function(err, rec) {
  console.log('* dns.reverse(): err: %j; rec: %j', err, rec);
});
dns.reverse(ip3, function(err, rec) {
  console.log('* dns.reverse(): err: %j; rec: %j', err, rec);
});
dns.reverse(ip4, function(err, rec) {
  console.log('* dns.reverse(): err: %j; rec: %j', err, rec);
});
dns.reverse(ip5, function(err, rec) {
  console.log('* dns.reverse(): err: %j; rec: %j', err, rec);
});