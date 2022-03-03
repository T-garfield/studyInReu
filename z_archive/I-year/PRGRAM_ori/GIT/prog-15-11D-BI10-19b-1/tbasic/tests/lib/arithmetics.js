/* globals describe, before, beforeEach, after, afterEach, it */

'use strict';

const chai = require('chai');
//const assert = chai.assert;
const expect = chai.expect;
//const should = chai.should();


// declaring global vars
let arithmetics;


describe('arithmetics', function() {

  before('before', function() {
    // initializing common test data
    arithmetics = require('../../lib/arithmetics.js');
  });

  beforeEach('beforeEach', function() {
  });

  afterEach('afterEach', function() {
  });

  after('after', function() {
  });


  describe('binary', function() {
    it('is a function', function () {
      expect(arithmetics.binary).to.be.a('function');
    });
    
    it('+', function () {
      const a = 1;
      const op = '+';
      const b = 5;
      expect(arithmetics.binary(a, op, b)).to.equal(6);
    });

    it('-', function () {
      const a = 13;
      const op = '-';
      const b = 3;
      expect(arithmetics.binary(a, op, b)).to.equal(10);
    });

    it('*', function () {
      const a = 3;
      const op = '*';
      const b = 6;
      expect(arithmetics.binary(a, op, b)).to.equal(18);
    });

    it('/', function () {
      const a = 9;
      const op = '/';
      const b = 2;
      expect(arithmetics.binary(a, op, b)).to.equal(4);
    });

    // Операции сравнения

    it('>', function () {
      const a = 7;
      const op = '>';
      const b = 3;
      expect(arithmetics.binary(a, op, b)).to.equal(true);
    });

    it('<', function () {
      const a = 1;
      const op = '<';
      const b = 2;
      expect(arithmetics.binary(a, op, b)).to.equal(true);
    });

    it('>=', function () {
      const a = 6;
      const op = '>=';
      const b = 6;
      expect(arithmetics.binary(a, op, b)).to.equal(true);
    });

    it('<=', function () {
      const a = 10;
      const op = '<=';
      const b = 10;
      expect(arithmetics.binary(a, op, b)).to.equal(true);
    });

    // Логические операции

    it('&&', function () {
      const a = 1;
      const op = '&&';
      const b = 1;
      expect(arithmetics.binary(a, op, b)).to.equal(1);
    });

    it('||', function () {
      const a = 0;
      const op = '||';
      const b = 1;
      expect(arithmetics.binary(a, op, b)).to.equal(1);
    });

    it('!', function () {
      const a = 1;
      const op = '!';
      const b = 0
      expect(arithmetics.binary(a, op, b)).to.equal(true);
    });

    it('XOR1', function () {
      const a = 1;
      const b = 0;
      const op = 'XOR';
      expect(arithmetics.binary(a, op, b)).to.equal(true);
    });

    it('XOR2', function () {
      const a = 1;
      const b = 1;
      const op = 'XOR';
      expect(arithmetics.binary(a, op, b)).to.equal(false);
    });
    
  });

  //describe('unary arithmetics', function() {
  //  //Калинин, Горбачёв
  //  it('is a function', function () {
  //  expect(arithmetics.unary).to.be.a('function');
  //  });
  //
  //  it('op = - ?', function () {
  //  const op = '-';
  //  const a = -3;
  //  expect(arithmetics.unary(op, a)).to.equal(3);
  //  });
  //
  //  });

  describe('unary arithmetics', function() {

    it('is a function', function () {
      expect(arithmetics.unary).to.be.a('function');
    });

    it('-', function () {
      expect(arithmetics.unary('-', 1)).to.equal(-1);
    });

    it('+', function () {
      expect(arithmetics.unary('+', 1)).to.equal(1);
    });

    it('invalid op', function () {
      expect(function() {
        arithmetics.unary('invalid', 1)
      }).to.throw();
    });

  });


});

