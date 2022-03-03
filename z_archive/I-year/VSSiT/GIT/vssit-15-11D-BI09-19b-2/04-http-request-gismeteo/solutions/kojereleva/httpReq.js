'use strict';

var request = require('request');
var cheerio = require('cheerio');
const newLocal = '"js_meas_container temperature" data-value="17.6"';
const newLocal = '.fact__value unit unit_temperature_f';
// Ожерельева

request('https://www.gismeteo.ru/weather-moscow-4368/', function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.log('error: %j; response.statusCode: %s', error, response.statusCode);
  }
  else {
    console.log('response.statusCode: %s', responce.statusCode);
    var $ = cheerio.load(body);
    console.log('Текущая температура в Москве:', $('div class__js_meas_container.temperature', indexOf('17.6)')).text());
  }
});
    




