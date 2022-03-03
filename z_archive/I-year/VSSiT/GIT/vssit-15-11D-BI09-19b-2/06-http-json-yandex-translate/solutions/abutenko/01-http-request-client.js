'use strict';

const request = require('request');

const credentials = require('./credentials.json');

const API_KEY = credentials.apiKey,
      BASE_URL      = 'https://translate.yandex.net/api/v1.5/tr.json/',
      TEXT1 =
        'Я не вернусь, так говорил когда-то ' +
        'И туман глотал мои слова и превращал их в воду ' +
        'Я всё отдам за продолжение пути ' +
        'Оставлю позади свою беспечную свободу ',
      TEXT2 =
        'Пятнадцать человек на сундук мертвеца. '+
        'Йо-хо-хо, и бутылка рому! ' +
        'Пей, и дьявол тебя доведет до конца. ' +
        'Йо-хо-хо, и бутылка рому!';


function getLangs(/**String*/ key, /**String=*/ ui, /**String=*/ jsonpCallback, /**function=*/ callback) {
  callback = (typeof callback === 'function') ? callback : function() {};

  // Request Syntax
  // https://tech.yandex.ru/translate/doc/dg/reference/getLangs-docpage/
  //
  // https://translate.yandex.net/api/v1.5/tr.json/getLangs ?
  // key=<API-ключ>
  //  & [ui=<код языка>]
  //  & [callback=<имя callback-функции>]
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

function detect(/**String*/ key, /**String*/ text, /**String=*/ jsonpCallback, /**function=*/ callback) {
  callback = (typeof callback === 'function') ? callback : function() {};

  // Request Syntax
  // https://tech.yandex.ru/translate/doc/dg/reference/detect-docpage/
  //
  // https://translate.yandex.net/api/v1.5/tr.json/detect ?
  // key=<API-ключ>
  //  & text=<текст>
  //  & [callback=<имя callback-функции>]
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

function translate(/**String*/ key, /**String*/ text, /**String*/ lang, /**String=*/ format, /**Number=*/ options, /**String=*/ jsonpCallback, /**function=*/ callback) {
  callback = (typeof callback === 'function') ? callback : function() {};
  var url = BASE_URL + 'translate' + '?key=' + key + '&text=' + encodeURIComponent(text) + '&lang=' + lang + '&format=' + format + (jsonpCallback ? '&callback='+jsonpCallback : '');
  request({
      url:    url,
      method: 'GET'
    },
    function (error, response, body) {
      if (error || response.statusCode !== 200) {
        console.log('translate(): error: %j; response.statusCode: %s,  body: %s', error, response.statusCode, body);
        callback(error, response, body);
        return;
      }
      console.log('translate(): response.statusCode: %s', response.statusCode);
      console.log('translate(): body: %s', body);
      callback(error, response, body);
    }
  );
}

// JSON

getLangs(API_KEY);
getLangs(API_KEY, 'ru');

detect(API_KEY, TEXT2);

translate(API_KEY, TEXT2, 'ru-en', 'plain');
translate(API_KEY, TEXT2,    'fr', 'html', 1);

translate(API_KEY, TEXT1, 'ru-en', 'plain');
translate(API_KEY, TEXT1,    'fr', 'html', 1);

