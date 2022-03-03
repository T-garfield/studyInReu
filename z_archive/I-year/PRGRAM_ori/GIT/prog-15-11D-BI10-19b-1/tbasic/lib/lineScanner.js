'use strict';

const debug = require('./debug.js');
const ERRORS = require('./errors.json');


/**
 *  LineScanner
 */

class LineScanner {

  constructor() {
    this.line = '';
    this.pos = 0
  }


  setLine(line, pos) {
    this.line = line;
    this.pos = typeof pos !== 'undefined' ? pos : 0;
  };

  //

  isBOL() {
    if (this.pos === 0) { return true }
    else { return false };
  };

  newMethod() {
    throw new Error('Not implemented');
  }

  isEOL() {
    // Сапронова, Фонина
    if (this.pos >= (this.line.length - 1)) { 
      return true
    } else {
      return false
    }
  };

  peekChar() {
    //Горбачев, Мальчикова, Калинин 
    if (typeof this.line[this.pos] === 'undefined') {
      return null;
    } else {
      return this.line[this.pos];
    }
  };

 
  testSpace() { // Ибрагимова, Бутова, Нгуен Нгок Ань
    if (
    (this.line[this.pos] === ' ' || this.line[this.pos] === '\t') &&
    (!(this.isEOL()))
    ) {
      return true
      } else {
      return false
        };
    };

  getSpace() {

    // Сапронова, Фонина


    if (this.testSpace()) {
      this.pos += 1
      return (' ')
    } else { return null }
  };


  getSpaces() { // Ибрагимова, Бутова, Нгуен Нгок Ань
    var i = 0 
    while (this.getSpace()) {
    i += 1
    }
    if (i > 0) {
    return (' '.repeat(i))
    } else { return null }
};



  testChar(ch) {//dyachkov-nazarov-treznyuk
    if (this.line[this.pos] === ch) {
      return true;
    } else if (this.pos > this.line.length - 1) {
      return ('Index is out of the range');
    } else {
      return false;
    }
  };

  getChar(ch) {
    if (this.line.length >= this.pos) {
      if (this.testChar(ch)) {
        this.pos++;
        return ch;
      } else {
        return null;
      }
    }
    if (this.pos > this.line.length) {
      return null;
    }
  };

  testChars(chars) { //dyachkov-nazarov-treznyuk
    if (this.pos > this.line.length - 1) {
      return ('Index is out of the range')
    } else {
      for (let i = 0; i <= chars.length - 1; i++) {
        if (this.line[this.pos] === chars[i]) {
          return true;
        } else {
          return false;
        }
      }
    }
  };

  getChars(chars) {
    const ch = this.line[this.pos];
    if (chars.indexOf(ch) > 0) {
      this.pos++
      return ch;
    } else {
      return null;
    }
  };

  getCharNot(chars) {
    const ch = this.line[this.pos];
    if (chars.indexOf(ch) < 0) {
      this.pos++
      return ch;
    } else {
      return null;
    }
  };


  testNumber() {
    // Пояркова, Ибрагимова, Бутова
    let nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
    for (var i = 0; i < nums.length; i++) {
      if (this.line[this.pos] == nums[i]) {
        return true;
      }
    }
    return false;

  };

  testCharNot(ch) {
    // Пояркова, Ибрагимова, Бутова
    if (this.pos <= this.line.length) {
      if (ch == this.line[this.pos]) {
        return false;
      } else {
        return true;
      };
    } else {
      return 'выход за пределы строки';
    }
  };

  getNumber() {
    let result = '';
    do {
      const ch = this.line[this.pos];
      const found = '0123456789'.indexOf(ch) >= 0
      if (found) {
        this.pos++
        result = result + ch
      }
      else {
        if (result === '') { return null }
        else {
          let numResult = parseInt(result)
          return numResult
        }
      }
    } while (true)
  };


  testString(str) {
    if (this.line.slice(this.pos, this.pos + str.length) === str) {
      return true;
    } else {
      return false;
    }
  };

  getString(str) {
    // Ибрагимова, Бутова
    let pos = 0
    for (let i = 0; i < str.length; i++) {
      if (str[i] === this.line[this.pos + i]) {
        pos++
      }
      else {
        return null
      }
    }
    this.pos = this.pos + pos
    return str
  };


  testStrings(strings) {
    // Пояркова, Дьячков, Назаров
    for (var i = 0; i < strings.length; i++) {
      let str = strings[i];
      if (this.testString(str)) {
        return true;
      } else {
        return null;
      }
    }
  };


  getStrings(strings) { // Нгуен Нгок Ань
    for ( let i = 0; i < strings.length; i++) {
      let str = strings[i];
      if (this.testString(str)) {
      this.pos++
        return str;
        } else { 
           return null;
         }
       }
};


  shift(num) { //dyachkov-nazarov-treznyuk
    if (num) {
      this.pos += num;
    } else {
      this.pos += 1;
    }
    if (this.pos <= this.line.length - 1) {
      return true;
    } else {
      return false;
    }
  };

}


module.exports = LineScanner;
