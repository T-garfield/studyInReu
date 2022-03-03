'use strict';

var request = require('request');
var parseString = require('xml2js').parseString;
var iconv = require('iconv-lite');

var fromEnc = 'cp1251';
var toEnc = 'utf-8';


request({
    url: 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=26/05/2020',
    encoding: null
  },
  function (error, response, body) {
    if (error || response.statusCode !== 200) {
      console.log('error: %j; response.statusCode: %s', error, response.statusCode);
    } else {
      console.log('response.statusCode: %s', response.statusCode);


	body = iconv.decode(body, fromEnc);


      parseString(body, function (err, result) {
        if (err) {
          console.log('error:', err);
        }

        var curr = result.ValCurs.Valute[1];
        console.log( curr );

       });
    }
  });
