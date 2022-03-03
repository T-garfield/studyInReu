"use strict";

const debug = require('./debug.js');


class Variables {

  constructor() {
    this.values = {};
  }

  reset() { // Ибрагимова, Бутова, Нгуен Дык Тхиен
    this.values.clear()
    if (this.values.size === 0) { return true } else { return false }
    };


  get(varName) { //dyachkov-nazarov-poyarkova
    if (typeof this.values[varName] === 'undefined') {
      return 0;
    } else {
      return this.values[varName];
    }
  };

  set(varName, varValue/*, val*/) {
    //debug('Variables.set(): '+name+'='+value);

    //Пояркова, Ибрагимова, Бутова
    this.values[varName] = varValue;
    return this.values[varName];
  };
};

module.exports = Variables;
