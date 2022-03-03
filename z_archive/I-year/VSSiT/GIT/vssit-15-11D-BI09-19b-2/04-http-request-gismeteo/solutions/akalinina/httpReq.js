'use strict';

var request = require('request');
var cheerio = require("cheerio");
// Калинина,Джикаева
request('https://yandex.ru/pogoda/moscow?utm_source=serp&utm_campaign=wizard&utm_medium=desktop&utm_content=wizard_desktop_main&utm_term=title', function (error, response, body) {
  if (error || response.statusCode !== 200) {
      console.log('error: %j; response.statusCode: %s', error, response.statusCode);
  } else {
    console.log('response.statusCode: %s', response.statusCode);
    var $ = cheerio.load(body);
    console.log ('Значение ветра: ', $('.fact__wind-speed').text())
  }
});

