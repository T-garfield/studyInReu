'use strict';

const debug = require('./debug.js');
const ERRORS = require('./errors.json');


const binary = function(a, op, b) {
  if (op === '+') {
  return a+b;
  } else if (op === '-') {
  return a-b;
  } else if (op === '*') {
  return a*b;
  } else if (op === '/') {
  return Math.floor(a/b);
  }
  // Операции сравнения
  if (op === '>') {
    return a>b;
    } else if (op === '<') {
    return a<b;
    } else if (op === '>=') {
    return a>=b;
    } else if (op === '<=') {
    return a<=b;
    }
  // Логические операции
  if (op === '&&') {
    return a&&b;
    } else if (op === '||') {
    return a||b;
    } else if (op === '!') {
    return a = !b;
    } else if (op === 'XOR') {
    return (a || b) && (!(a && b));
    }
};

//const unary = function(op, a) { // Калинин, Горбачёв
//  if (op === '-') {
//  return -a
//  }
//  };

/**
 * Implements unary operations over integer numbers
 *
 * @param {'+'|'-'} op
 * @param {number}  a
 * @return {number}
 */
const unary = function(op, a) {
  const operations = {
    '-': (a) => -a,
    '+': (a) => a,
  };
  const fn = operations[op];
  if (typeof fn === 'undefined') throw new Error(ERRORS.INVALID_OPERATION);
  return fn(a);
};


module.exports = {
  unary: unary,
  binary: binary
};
