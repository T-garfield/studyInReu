'use strict';

const request = require('request');

const credentials = require('./credentials.json');

const API_KEY = credentials.apiKey,
      BASE_URL      = 'https://translate.yandex.net/api/v1.5/tr.json/',
      TEXT1 =
        'Такой вот парадокс: ' +
        'мы совершаем подвиги для тех, ' +
        'кому до нас нет никакого дела, ' +
        'а любят нас те, ' +
        'кому мы нужны и без всяких подвигов.',
      TEXT2 =
        'На старых сидениях кинотеатра '+
        'В лучах прожектора мы с тобою вдвоём ' +
        'Мы одни, ты смотришь на героев с экрана' +
        'Мне так сложно сидеть с тобою спокойно'+
        'Моя тревога внутри',
      TEXT3 = 
        'Не влюбляйся, не пей вина ' + 
        'И на лбу себе высеки ' +
        'Жизнь тебе для того дана ' +
        'Чтобы взять три яйца...',
     

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
  
  var url = BASE_URL + 'translate' + '?key=' + key + '&text=' + encodeURIComponent(text) + '&lang=' + lang + '&format=' + format + '&option=' + options + (jsonpCallback ? '&callback='+jsonpCallback : '');
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



// JSON

getLangs(API_KEY);
getLangs(API_KEY, 'ru');

detect(API_KEY, TEXT2);

translate(API_KEY, TEXT2, 'ru-en', 'plain');
translate(API_KEY, TEXT2,    'fr', 'html', 1);
translate(API_KEY, TEXT3, 'ru-fr', 'html');

