'use strict';

var request = require('request');

request('https://www.gismeteo.ru/city/daily/4368/', function (error, response, body) {
  if (error || response.statusCode !== 200) {
      console.log('error: %j; response.statusCode: %s', error, response.statusCode);
  } else {
    console.log(body);
  }
});
