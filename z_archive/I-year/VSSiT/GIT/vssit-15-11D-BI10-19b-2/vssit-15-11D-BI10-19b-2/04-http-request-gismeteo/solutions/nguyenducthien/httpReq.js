'use strict';

var request = require('request');
var cheerio = require("cheerio");

request('https://www.gismeteo.ru/city/daily/4368/now/', function (error, response, body) {
  if (error || response.statusCode !== 200) {
      console.log('error: %j; response.statusCode: %s', error, response.statusCode);
  } else {
    console.log('response.statusCode: %s', response.statusCode);
    var $ = cheerio.load(body)

    console.log('Значение температуры: ', $('.temperature').text())
  }
});
