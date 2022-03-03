///Еремина и Исхакова
'use strict';

var request = require('request');
var cheerio = require("cheerio");

request('https://www.gismeteo.ru/weather-moscow-4368/now/', function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.log('error: %j; response.statusCode: %s', error, response.statusCode);
} else {
    console.log('response.statusCode: %s', response.statusCode);
    var $ = cheerio.load(body);c
    console.log('Геомагнитная активность в Москве: ', $('value').text()+ ' балла(-ов)')
  }
});
