'use strict';


module.exports = function debug(s, lvl) {

  var prefix = '';
  if (typeof lvl !== 'undefined') {
    for (var i=0; i<lvl; i++) { prefix += '#'; }
    prefix += ' ';
  }
  console.log('*** ' + prefix + s);

};
