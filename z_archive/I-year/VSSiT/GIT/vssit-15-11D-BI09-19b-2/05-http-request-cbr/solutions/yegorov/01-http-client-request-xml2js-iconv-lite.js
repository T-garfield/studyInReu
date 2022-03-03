//Егоров-Дерюгина

'use strict';

var request = require('request');
var parseString = require('xml2js').parseString;
//var Iconv = require('iconv').Iconv;
var iconv = require('iconv-lite');

var fromEnc = 'cp1251';
var toEnc = 'utf-8';

//var iconv = new Iconv(fromEnc,toEnc);

request({
    url: 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=18/03/2017',
    encoding: null
  },
  function (error, response, body) {
    if (error || response.statusCode !== 200) {
      console.log('error: %j; response.statusCode: %s', error, response.statusCode);
    } else {
      console.log('response.statusCode: %s', response.statusCode);


      // Convert encoding from Win1251 to utf8

      //console.log(body);
      //body = new Buffer(body, 'binary');
      //body = iconv.convert(body).toString();
      //console.log(body);
	body = iconv.decode(body, fromEnc);

      // parse XML using xml2js

      parseString(body, function (err, result) {
        if (err) {
          console.log('error:', err);
        }

        //console.dir(result);
        //console.log( result.ValCurs.Valute[0] );
        var curr = result.ValCurs.Valute[3];
        console.log('| 3 | ' + curr.Name + ' ' + curr.Value + ' |');

       });
    }
  });
