/**
 * Created by alykoshin on 10.10.15.
 */

'use strict';

var dns = require('dns');

var HOSTNAME = 'yandex.ru';

var callback = function(err, rec) {
  if (err) {
    console.log('* callback(): err', err);
  }
  console.log('* callback(): rec', rec);
};

var options;

/*
 1) Functions that use the underlying operating system facilities to perform name resolution, and that do not necessarily do any network communication. This category contains only one function: dns.lookup. Developers looking to perform name resolution in the same way that other applications on the same operating system behave should use dns.lookup.
 */
options = {
  //family: 4, // 6
  //hints: dns.ADDRCONFIG | dns.V4MAPPED, // getaddrinfo flags
  all: false
};
/*
 dns.ADDRCONFIG: Returned address types are determined by the types of addresses supported by the current system. For example, IPv4 addresses are only returned if the current system has at least one IPv4 address configured. Loopback addresses are not considered.
 dns.V4MAPPED: If the IPv6 family was specified, but no IPv6 addresses were found, then return IPv4 mapped IPv6 addresses. Note that it is not supported on some operating systems (e.g FreeBSD 10.1).
 */
dns.lookup(HOSTNAME, options, function(err, address, family) {
  console.log('* dns.lookup(): err: %j; address: %j; family: %d', err, address, family);
});

options = {
  //family: 4, // 6
  //hints: dns.ADDRCONFIG | dns.V4MAPPED, // getaddrinfo flags
  all: true
};
dns.lookup(HOSTNAME, options, function(err, addresses) {
  console.log('* dns.lookup(): err: %j; addresses: %j', err, addresses);
});

/*
 2) Functions that connect to an actual DNS server to perform name resolution, and that always use the network to perform DNS queries. This category contains all functions in the dns module but dns.lookup. These functions do not use the same set of configuration files than what dns.lookup uses. For instance, they do not use the configuration from /etc/hosts. These functions should be used by developers who do not want to use the underlying operating system's facilities for name resolution, and instead want to always perform DNS queries.
 */
var ADDRESS = '127.0.0.1',
    PORT    = 80;
dns.lookupService(ADDRESS, PORT, function(err, hostname, service) {
  console.log('* dns.lookupService(): err: %j; hostname: %j; service: %j', err, hostname, service);
});

dns.resolve(HOSTNAME, 'A', function(err, rec) {
  console.log('* dns.resolve(): err: %j; rec: %j', err, rec);
});

dns.resolve4(HOSTNAME, function(err, rec) {
  console.log('* dns.resolve4(): err: %j; rec: %j', err, rec);
});

dns.resolve6(HOSTNAME, function(err, rec) {
  console.log('* dns.resolve6(): err: %j; rec: %j', err, rec);
});

dns.resolveMx(HOSTNAME, function(err, rec) {
  console.log('* dns.resolveMx(): err: %j; rec: %j', err, rec);
});

dns.resolveTxt(HOSTNAME, function(err, rec) {
  console.log('* dns.resolveTxt(): err: %j; rec: %j', err, rec);
});
dns.resolveSrv(HOSTNAME, function(err, rec) {
  console.log('* dns.resolveSrv(): err: %j; rec: %j', err, rec);
});
dns.resolveSoa(HOSTNAME, function(err, rec) {
  console.log('* dns.resolveSoa(): err: %j; rec: %j', err, rec);
});
dns.resolveNs(HOSTNAME, function(err, rec) {
  console.log('* dns.resolveNs(): err: %j; rec: %j', err, rec);
});
dns.resolveCname(HOSTNAME, function(err, rec) {
  console.log('* dns.resolveCname(): err: %j; rec: %j', err, rec);
});

//var ip = '5.255.255.5';
var ip = '216.18.168.16';
dns.reverse(ip, function(err, rec) {
  console.log('* dns.reverse(): err: %j; rec: %j', err, rec);
});

var servers;
servers = dns.getServers();
console.log('* dns.getServers(): servers: %j', servers);

// There is a bug in dns.setServers
// It may be called onyl hen other methods cleaned up
/*
 node: ../deps/cares/src/ares_destroy.c:102: ares__destroy_servers_state: Assertion `ares__is_list_empty(&server->queries_to_server)' failed.

 bug reports:
 https://github.com/nodejs/node/issues/894
 https://github.com/nodejs/node-v0.x-archive/issues/9243
 */

setTimeout(
  function() {
    servers = [
      //'8.8.8.8',    '8.8.4.4',   // Google Public DNS
      //'77.88.8.8',  '77.88.8.1', // Yandex Basic
      ////'77.88.8.88', '77.88.8.2', // Yandex Safe
      '77.88.8.7',  '77.88.8.3', // Yandex Family
    ];
    dns.setServers(servers);
    //dns.setServers(['8.8.8.8']);

    servers = dns.getServers();
    console.log('* dns.getServers(): servers: %j', servers);

    dns.lookup(HOSTNAME, options, function(err, address, family) {
      console.log('* dns.lookup(): err: %j; address: %j; family: %d', err, address, family);
    });

    dns.resolve(HOSTNAME, 'A', function(err, rec) {
      console.log('* dns.resolve(): err: %j; rec: %j', err, rec);
    });

    var ip = '93.158.134.250';
    dns.reverse(ip, function(err, rec) {
      console.log('* dns.reverse(): err: %j; rec: %j', err, rec);
    });


  }, 5 * 1000
);
