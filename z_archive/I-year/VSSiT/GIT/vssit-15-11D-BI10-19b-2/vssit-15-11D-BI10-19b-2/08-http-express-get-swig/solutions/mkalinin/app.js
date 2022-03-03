/**
 * Создаем подкаталог views, где будут размещаться шаблоны,
 * добавлям в него файл index.html
 */

var HTTP_PORT  = 8080;

var express     = require('express')
  , app         = express()
  , http        = require('http')
  , httpServer  = http.createServer(app)
  , cons        = require('consolidate')           // Template library
;

// Template engine
app.engine('html', cons.swig);
app.set('view engine', 'html');
app.set('views', __dirname + '/views');

// Открываем порт
httpServer.listen(HTTP_PORT); // веб-сервер

app.get('/', function(req, res, next) {
  console.log('app.get(\'/\')', req.body );

  var var1 = 'mkalinin',
      var2 = new Date().toLocaleDateString();

  // вернем браузеру шаблон HTML страницы,
  // в который будут подставлены значения переменных `var1`, `var2`
  res.render('index.html', { var1: var1, var2: var2 } );
});
