/**
* Created by alykoshin on 10.10.15.
*/

'use strict';
//[{"address":"104.215.148.63","family":4},{"address":"40.76.4.15","family":4},{"address":"40.112.72.205","family":4},{"address":"40.113.200.201","family":4},{"address":"13.77.161.179","family":4}]
var dns = require('dns');

var HOSTNAME1 = 'google.com';
var HOSTNAME2 = 'vk.com';
var HOSTNAME3 = 'instagram.com';
var HOSTNAME4 = 'twitter.com';
var HOSTNAME5 = 'mail.ru';
var ip1 = "87.240.190.67";
var ip2 = "173.194.222.102";
var ip3 = "34.204.228.16";
var ip4 = "54.152.61.144";
var ip5 = "217.69.139.200";
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
dns.lookup(HOSTNAME1, options, function(err, address, family) {
console.log('* dns.lookup() for 1: err: %j; address: %j; family: %d', err, address, family);
});
dns.lookup(HOSTNAME2, options, function(err, address, family) {
console.log('* dns.lookup() for 2: err: %j; address: %j; family: %d', err, address, family);
});
dns.lookup(HOSTNAME3, options, function(err, address, family) {
console.log('* dns.lookup() for 3: err: %j; address: %j; family: %d', err, address, family);
});
dns.lookup(HOSTNAME4, options, function(err, address, family) {
console.log('* dns.lookup() for 4: err: %j; address: %j; family: %d', err, address, family);
});
dns.lookup(HOSTNAME5, options, function(err, address, family) {
console.log('* dns.lookup() for 5: err: %j; address: %j; family: %d', err, address, family);
});
options = {
//family: 4, // 6
//hints: dns.ADDRCONFIG | dns.V4MAPPED, // getaddrinfo flags
all: true
};
dns.lookup(HOSTNAME1, options, function(err, addresses) {
console.log('* dns.lookup() for 1: err: %j; addresses: %j', err, addresses);
});
dns.lookup(HOSTNAME2, options, function(err, addresses) {
console.log('* dns.lookup() for 2: err: %j; addresses: %j', err, addresses);
});
dns.lookup(HOSTNAME3, options, function(err, addresses) {
console.log('* dns.lookup() for 3: err: %j; addresses: %j', err, addresses);
});
dns.lookup(HOSTNAME4, options, function(err, addresses) {
console.log('* dns.lookup() for 4: err: %j; addresses: %j', err, addresses);
});
dns.lookup(HOSTNAME5, options, function(err, addresses) {
console.log('* dns.lookup() for 5: err: %j; addresses: %j', err, addresses);
});
/*
2) Functions that connect to an actual DNS server to perform name resolution, and that always use the network to perform DNS queries. This category contains all functions in the dns module but dns.lookup. These functions do not use the same set of configuration files than what dns.lookup uses. For instance, they do not use the configuration from /etc/hosts. These functions should be used by developers who do not want to use the underlying operating system's facilities for name resolution, and instead want to always perform DNS queries.
*/
var ADDRESS = '127.0.0.1',
PORT = 80;
// dns.lookupService(ADDRESS, PORT, function(err, hostname, service) {
// console.log('* dns.lookupService(): err: %j; hostname: %j; service: %j', err, hostname, service);
// });
 
dns.resolve(HOSTNAME1, 'A', function(err, rec) {
console.log('* dns.resolve() for 1: err: %j; rec: %j', err, rec);
});
dns.resolve(HOSTNAME2, 'A', function(err, rec) {
console.log('* dns.resolve() for 2: err: %j; rec: %j', err, rec);
});
dns.resolve(HOSTNAME3, 'A', function(err, rec) {
console.log('* dns.resolve() for 3: err: %j; rec: %j', err, rec);
});
dns.resolve(HOSTNAME4, 'A', function(err, rec) {
console.log('* dns.resolve() for 4: err: %j; rec: %j', err, rec);
});
dns.resolve(HOSTNAME5, 'A', function(err, rec) {
console.log('* dns.resolve() for 5: err: %j; rec: %j', err, rec);
});

// dns.resolve4(HOSTNAME, function(err, rec) {
// console.log('* dns.resolve4(): err: %j; rec: %j', err, rec);
// });

// dns.resolve6(HOSTNAME, function(err, rec) {
// console.log('* dns.resolve6(): err: %j; rec: %j', err, rec);
// });

// dns.resolveMx(HOSTNAME, function(err, rec) {
// console.log('* dns.resolveMx(): err: %j; rec: %j', err, rec);
// });

// dns.resolveTxt(HOSTNAME, function(err, rec) {
// console.log('* dns.resolveTxt(): err: %j; rec: %j', err, rec);
// });
// dns.resolveSrv(HOSTNAME, function(err, rec) {
// console.log('* dns.resolveSrv(): err: %j; rec: %j', err, rec);
// });
// dns.resolveSoa(HOSTNAME, function(err, rec) {
// console.log('* dns.resolveSoa(): err: %j; rec: %j', err, rec);
// });
dns.resolveNs(HOSTNAME1, function(err, rec) {
console.log('* dns.resolveNs() for 1: err: %j; rec: %j', err, rec);
});
dns.resolveNs(HOSTNAME2, function(err, rec) {
console.log('* dns.resolveNs() for 2: err: %j; rec: %j', err, rec);
});
dns.resolveNs(HOSTNAME3, function(err, rec) {
console.log('* dns.resolveNs() for 3: err: %j; rec: %j', err, rec);
});
dns.resolveNs(HOSTNAME4, function(err, rec) {
console.log('* dns.resolveNs() for 4: err: %j; rec: %j', err, rec);
});
dns.resolveNs(HOSTNAME5, function(err, rec) {
console.log('* dns.resolveNs() for 5: err: %j; rec: %j', err, rec);
});
// dns.resolveCname(HOSTNAME, function(err, rec) {
// console.log('* dns.resolveCname(): err: %j; rec: %j', err, rec);
// });

//var ip = '5.255.255.5';
dns.reverse(ip1, function(err, rec) {
console.log('* dns.reverse() for 1: err: %j; rec: %j', err, rec);
});
dns.reverse(ip2, function(err, rec) {
console.log('* dns.reverse() for 2: err: %j; rec: %j', err, rec);
});
dns.reverse(ip3, function(err, rec) {
console.log('* dns.reverse() for 3: err: %j; rec: %j', err, rec);
});
dns.reverse(ip4, function(err, rec) {
console.log('* dns.reverse() for 4: err: %j; rec: %j', err, rec);
});
dns.reverse(ip5, function(err, rec) {
console.log('* dns.reverse() for 5: err: %j; rec: %j', err, rec);
});

// var servers;
// servers = dns.getServers();
// console.log('* dns.getServers(): servers: %j', servers);

// There is a bug in dns.setServers
// It may be called onyl hen other methods cleaned up
/*
node: ../deps/cares/src/ares_destroy.c:102: ares__destroy_servers_state: Assertion `ares__is_list_empty(&server->queries_to_server)' failed.

bug reports:
https://github.com/nodejs/node/issues/894
https://github.com/nodejs/node-v0.x-archive/issues/9243
*/

// setTimeout(
// function() {
// servers = [
// //'8.8.8.8', '8.8.4.4', // Google Public DNS
// //'77.88.8.8', '77.88.8.1', // Yandex Basic
// //'77.88.8.88', '77.88.8.2', // Yandex Safe
// '77.88.8.7', '77.88.8.3', // Yandex Family
// ];
// dns.setServers(servers);
// //dns.setServers(['8.8.8.8']);

// servers = dns.getServers();
// console.log('* dns.getServers(): servers: %j', servers);

// dns.lookup(HOSTNAME, options, function(err, address, family) {
// console.log('* dns.lookup(): err: %j; address: %j; family: %d', err, address, family);
// });

// dns.resolve(HOSTNAME, 'A', function(err, rec) {
// console.log('* dns.resolve(): err: %j; rec: %j', err, rec);
// });

// var ip = '93.158.134.250';
// dns.reverse(ip, function(err, rec) {
// console.log('* dns.reverse(): err: %j; rec: %j', err, rec);
// });


// }, 5 * 1000
// );