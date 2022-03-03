'use strict';

const debug = require('./debug.js');
const ERRORS = require('./errors.json');

const arithmetics = require('./arithmetics.js');


const OPTION_LABEL_EXPRESSION = true;


class Expression {

  constructor(tbasic) {
    this.tbasic = tbasic;
  }


  get_factor() {
    // Дьячков, Назаров, Пояркова
    // throw new Error('Not implemented');

    this.tbasic.parser.getSpaces();
    let a = this.tbasic.parser.getNumber();
    //console.log('начальное а', a);
    let b = this.tbasic.variables.get(this.tbasic.parser.getVariable());
    //console.log('начальное b', b);
    let c = null;
    //console.log('начальное c', c);
    let d;
    if (a) {
      // console.log('factor число' ,a);
      // console.log('pos factor', this.tbasic.parser.pos);
      return a;
    } else if (typeof b === 'number' && b != 0) {
      return b;
    }
    
    else if (this.tbasic.parser.peekChar() === '(') {
      this.tbasic.parser.pos++
      d = this.get_expression();
      if (this.tbasic.parser.peekChar() === ')') {
        this.tbasic.parser.pos++
        console.log(d);
        return d;
      }
    }

    else {
      //console.log(c);
      return c;
    }
  };


  get_term() {
    // Дьячков, Назаров, Пояркова
    //throw new Error('Not implemented');

    let a = this.get_factor();
    console.log('term a', a);
    // console.log('pos term', this.tbasic.parser.pos);
    this.tbasic.parser.getSpaces();
    if (this.tbasic.parser.peekChar() === '*' || this.tbasic.parser.peekChar() === '/') {
      let op = this.tbasic.parser.peekChar();
      this.tbasic.parser.pos++;
      // console.log(' term op', op);
      // console.log('pos term', this.tbasic.parser.pos);
      this.tbasic.parser.getSpaces();
      let b = this.get_factor();
      //console.log('term b', b);
      return arithmetics.binary(a, op, b);
    } else {
      return a;
    }
  };

  //

  get_unsignedexpr() {
    // Хайретдинова, Голованова

    let a = this.get_term();
    console.log(a);
    // console.log(this.tbasic.parser.pos);
    this.tbasic.parser.getSpaces();
    if (this.tbasic.parser.peekChar() === '+' || this.tbasic.parser.peekChar() === '-') {
      let op = this.tbasic.parser.peekChar();
      this.tbasic.parser.pos++;
      this.tbasic.parser.getSpaces();
      let b = this.get_term();
      return arithmetics.binary(a, op, b);
    } else {
      return a
    }
  };

  //

  get_expression() {
    // Хайретдинова, Голованова

    let a = this.get_unsignedexpr();
    //console.log(a);
    // console.log(this.tbasic.parser.pos);
    this.tbasic.parser.getSpaces();
    if (this.tbasic.parser.peekChar() === '+' || this.tbasic.parser.peekChar() === '-') {
      let op = this.tbasic.parser.peekChar();
      this.tbasic.parser.pos++;
      this.tbasic.parser.getSpaces();
      return arithmetics.unary(op, a);
    } else {
      return a
    }
  };


  //get_logical_expr() {
  //  throw new Error('Not implemented');
  //};


}


module.exports = Expression;
