'use strict';

const request = require('request');

const credentials = require('./credentials.json');

const API_KEY = credentials.apiKey,
      BASE_URL      = 'https://translate.yandex.net/api/v1.5/tr.json/',
      
      TEXT1 ='Ты видел деву на скале '+
      'В одежде белой над волнами '+
      'Когда, бушуя в бурной мгле, '+
      'Играло море с берегами, '+
      'Когда луч молний озарял '+
      'Ее всечасно блеском алым ',
      TEXT2 =
        'Пятнадцать человек на сундук мертвеца. '+
        'Йо-хо-хо, и бутылка рому! ' +
        'Пей, и дьявол тебя доведет до конца. ' +
        'Йо-хо-хо, и бутылка рому!';

function getLangs(key,  ui, jsonpCallback, callback) {
  callback = (typeof callback === 'function') ? callback : function() {};


  var url  = BASE_URL + 'getLangs'  + '?' + 'key=' + key + (ui ? '&ui='+ui : '') + (jsonpCallback ? '&callback='+jsonpCallback : '');
  request({
      url:    url,
      method: 'GET'
    },
    function (error, response, body) {
      if (error || response.statusCode !== 200) {
        console.log('getLangs(): error: %j; response.statusCode: %s,  body: %s', error, response.statusCode, body);
        callback(error, response, body);
        return;
      }
      console.log('getLangs(): response.statusCode: %s', response.statusCode);
      console.log('getLangs(): body: %s', body);
      callback(error, response, body);
    }
  );
}

function detect( key,  text,  jsonpCallback, callback) {
  callback = (typeof callback === 'function') ? callback : function() {};

 
  var url = BASE_URL + 'detect' + '?key=' + key + '&text=' + encodeURIComponent(text) + (jsonpCallback ? '&callback='+jsonpCallback : '');
  request({
      url:    url,
      method: 'GET'
    },
    function (error, response, body) {
      if (error || response.statusCode !== 200) {
        console.log('detect(): error: %j; response.statusCode: %s,  body: %s', error, response.statusCode, body);
        callback(error, response, body);
        return;
      }
      console.log('detect(): response.statusCode: %s', response.statusCode);
      console.log('detect(): body: %s', body);
      callback(error, response, body);
    }
  );
}

function translate( key,  text,  lang,  format,  options,  jsonpCallback,  callback) {
callback = (typeof callback === 'function') ? callback : function() {};
var url = BASE_URL + 'translate' + '?key=' + key + '&text=' + encodeURIComponent(text) +  '&lang=' + lang + '&format='+ format  + (options ? '&options=' + options:'') + (jsonpCallback ? '&callback='+jsonpCallback : '');
request({
  url:    url,
  method: 'GET'
},
function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.log('detect(): error: %j; response.statusCode: %s,  body: %s', error, response.statusCode, body);
    callback(error, response, body);
    return;
  }
  console.log('detect(): response.statusCode: %s', response.statusCode);
  console.log('detect(): body: %s', body);
  callback(error, response, body);
}
);
}
getLangs(API_KEY);
getLangs(API_KEY, 'ru');

detect(API_KEY, TEXT1);

translate(API_KEY, TEXT1, 'ru-en', 'plain', 1);
translate(API_KEY, TEXT2,    'fr', 'html', 1);

