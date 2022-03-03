'use strict';

var request = require('request');
var request = require('cheerio');

request('https://www.gismeteo.ru/weather-moscow-4368/gm/'), function (error, response, body) {
 if (error|| response.statusCode !== 200) {
   console.log ('error: %j; response.statusCode: %s', error, response.statusCode);
 } else {
   console.log('response.statusCode: %s', response.statusCode);
   var $ = cheerio.load(body);
   console.log ('Индекс геомагнитной активности: ', $('widget__item').text());

 };
};