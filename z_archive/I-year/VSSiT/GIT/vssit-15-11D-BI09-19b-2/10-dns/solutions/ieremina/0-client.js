/**
 * Created by alykoshin on 10.10.15.
 */

'use strict'; 

var dns = require('dns'); 

var HOSTNAME = 'pinterest.ru'; 

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

var ADDRESS = '127.0.0.1',
  PORT = 80; 
dns.lookupService(ADDRESS, PORT, function(err, hostname, service) { 
    console.log('* dns.lookupService(): err: %j; hostname: %j; service: %j', err, hostname, service); 
}); 

dns.resolve(HOSTNAME, 'A', function(err, rec) { 
    console.log('* dns.resolve(): err: %j; rec: %j', err, rec); 
}); 

dns.resolveNs(HOSTNAME, function(err, rec) { 
    console.log('* dns.resolveNs(): err: %j; rec: %j', err, rec); 
}); 

var ip = '31.173.87.84'; 
dns.reverse(ip, function(err, rec) { 
    console.log('* dns.reverse(): err: %j; rec: %j', err, rec); 
}); 

var servers; 
servers = dns.getServers(); 
console.log('* dns.getServers(): servers: %j', servers); 

setTimeout( 
    function() {
      servers = [ 
     '77.88.8.7', '77.88.8.3', // Yandex Family
      ]; 
      dns.setServers(servers); 
      
      servers = dns.getServers(); 
      console.log('* dns.getServers(): servers: %j', servers); 
      
      dns.lookup(HOSTNAME, options, function(err, address, family) { 
          console.log('* dns.lookup(): err: %j; address: %j; family: %d', err, address, family); 
        }); 
        
     dns.resolve(HOSTNAME, 'A', function(err, rec) { 
         console.log('* dns.resolve(): err: %j; rec: %j', err, rec);
        }); 
setTimeout(
 function() {
      servers = [
      '77.88.8.7', '77.88.8.3', //Yandex Family 
       ];
       dns.setServers(severs);
        
       servers = dns.getServers();
       console.log('*dns.getServers(): servers: %j', servers);

       dns.lookup(HOSTNAME, options, function(err, address, family) { 
            console.log('* dns.lookup(): err: %j; address: %j; family: %d', err, address, family); 
       });
        
       dns.resolve(HOSTNAME, 'A', function(err, rec) { 
            console.log('* dns.resolve(): err: %j; rec: %j', err, rec); 
       }); 
        
      var ip = '31.173.87.84'; 
       dns.reverse(ip, function(err, rec) { 
            console.log('* dns.reverse(): err: %j; rec: %j', err, rec); 
        }); 
  }, 5 * 1000 
);
});      
