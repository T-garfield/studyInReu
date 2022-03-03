/**
 * Created by alykoshin on 06.12.14.
 */

var HTTP_PORT  = 8080;

var express     = require('express')
  , app         = express()
  , http        = require('http')
  , httpServer  = http.createServer(app)
  
  ;

// Открываем порт
httpServer.listen(HTTP_PORT); // веб-сервер

app.get('/', function(req, res, next) {
  console.log('app.get(\'/\')', req.body );

  res.send('Hello, world');
});

app.get('/date', function(req, res, next) {
  
  console.log('app.get(\'/\')', req.body );
  var date = new Date();
  res.send(date + ' dp');
});


