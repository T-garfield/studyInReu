'use strict';

var request = require('request');
var cheerio = require("cheerio");
//Джикаева, Калинина
request('https://yandex.ru/pogoda/moscow?utm_campaign=informer&utm_content=main_informer&utm_medium=web&utm_source=home&utm_term=title', function (error, response, body) {
  if (error || response.statusCode !== 200) {
      console.log('error: %j; response.statusCode: %s', error, response.statusCode);
  } else {
    console.log('response.statusCode: %s', response.statusCode);
    var $ = cheerio.load(body);
    console.log('Значение ветра: ', $('.fact__wind-speed').text());
  }
});
