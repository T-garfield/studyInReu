'use strict';

var request = require('request');
var cheerio = require("cheerio")

request('https://yandex.ru/pogoda/nalchik', function (error, response, body) {
  if (error || response.statusCode !== 200) {
      console.log('error: %j; response.statusCode: %s', error, response.statusCode);
  } else {
    console.log('response.statusCode: %s', response.statusCode);
    var $ = cheerio.load(body)

console.log('Значение ветра: ',  $('.wind-speed').text());
 console.log('м/с');
 }
});
