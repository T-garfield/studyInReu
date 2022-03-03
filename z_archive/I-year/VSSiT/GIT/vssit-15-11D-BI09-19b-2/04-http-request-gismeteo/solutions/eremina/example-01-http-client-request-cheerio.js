'use strict';

var request = require('request');
var cheerio = require("cheerio");


const url = 'https://www.gismeteo.ru/weather-moscow-4368/';

request(url, function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.log('error: %j; response.statusCode: %s', error, response.statusCode);
  } else {
    console.log('response.statusCode: %s', response.statusCode);
    var $ = cheerio.load(body);


    console.log('.pageinfo_title h1: \'',  $('.pageinfo_title h1').text() + '\'');

  }
});
