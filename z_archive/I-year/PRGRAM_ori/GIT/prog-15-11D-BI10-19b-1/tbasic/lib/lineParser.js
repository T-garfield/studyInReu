'use strict';

const debug = require('./debug.js');
const ERRORS = require('./errors.json');


const LineScanner = require('./lineScanner.js');

class LineParser extends LineScanner {

  getVariable() {
    // Хайретдинова, Голованова
    this.getSpaces();
    const line01 = this.line.toUpperCase();
    const varUpper = line01[this.pos];
    if (varUpper >= 'A' && varUpper <= 'Z') {
      this.pos++;
      return varUpper;
    }
    else {
      return null;
    }  
  };

    getQuotedString() {
    //Сапронова, Фонина
    while(this.line[this.pos]===' '){
      this.pos++
    }
    if (this.line[this.pos]==='"' &&this.pos<this.line.length ){
      this.pos++
      let d=''
      while(this.line[this.pos]!=='"' && this.pos<this.line.length){
        d=d+this.line[this.pos]
        this.pos++
      }
      if (this.pos>=this.line.length) 
      {throw new Error('No closing quotation mark')}
      else{
        return d
      }
    }
    else{
      return null
    }
  };

}

module.exports = LineParser;
