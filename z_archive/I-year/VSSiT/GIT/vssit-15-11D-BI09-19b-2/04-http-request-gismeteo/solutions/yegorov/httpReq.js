///Егоров и Дерюгина
'use strict';

var request = require('request');
var cheerio = require("cheerio");


const url = 'https://yandex.ru/pogoda/213';

request(url, function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.log('error: %j; response.statusCode: %s', error, response.statusCode);
  } else {
    console.log('response.statusCode: %s', response.statusCode);
    var $ = cheerio.load(body);

    console.log($('div.temp.fact__temp.fact__temp_size_s').text() + '\'');

  }
});

