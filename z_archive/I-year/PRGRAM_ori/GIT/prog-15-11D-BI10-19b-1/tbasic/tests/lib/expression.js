/* globals describe, before, beforeEach, after, afterEach, it */

 'use strict';

var chai = require('chai');
var assert = chai.assert;
var expect = chai.expect;
//var should = chai.should();

const vm = require('vm');

// declaring global vars
var expression;


describe('Expression', function() {
  var tbasic;

  before('before', function() {
    // initializing common test data
    //var Tbasic = require('../../lib/tbasic.js');
    var LineParser = require('../../lib/lineParser.js');
    var Variables = require('../../lib/variables.js');
    //tbasic = new Tbasic();
    tbasic = {
      parser: new LineParser(),
      variables: new Variables()
    };
    var Expression = require('../../lib/expression.js');
    expression = new Expression(tbasic);

  });


  describe('expression', function () {

    it('is a function', function () {
      expect(expression.get_expression).to.be.a('function');
      expect(expression.get_term).to.be.a('function');
      expect(expression.get_factor).to.be.a('function');
      expect(expression.get_unsignedexpr).to.be.a('function');
    });

    it('factor число', function (){
      const line = '2';
      const pos = 0;
      tbasic.parser.setLine(line,pos);      
      expect(expression.get_expression()).to.equal(2)
    });

    it('factor переменная', function(){
      tbasic.variables.set('N',2)
      const line = 'N';
      const pos = 0;
      tbasic.parser.setLine(line,pos);      
      expect(expression.get_expression()).to.equal(2)
    })

    it('factor нет чисел и переменных', function(){
      const line = 'mama';
      const pos = 0;
      tbasic.parser.setLine(line,pos);      
      expect(expression.get_expression()).to.equal(null)
    })

    it('term умножение', function(){
      const line = '9*40';
      const pos = 0;
      tbasic.parser.setLine(line, pos);
      expect(expression.get_expression()).to.equal(360)
    })

    it('term деление', function () {
      const line = '60/10';
      const pos = 0;
      tbasic.parser.setLine(line, pos);
      expect(expression.get_expression()).to.equal(6) 
    })

    it('term переменная умножение',function () {
      tbasic.variables.set('O', 34)
      const line = 'O*2';
      const pos = 0;
      tbasic.parser.setLine(line,pos);      
      expect(expression.get_expression()).to.equal(68)
    })

    it('term переменная деление',function () {
      tbasic.variables.set('K', 80)
      const line = 'K/40';
      const pos = 0;
      tbasic.parser.setLine(line,pos);      
      expect(expression.get_expression()).to.equal(2)
    })

    it('term умножение 2 переменных', function() {
      tbasic.variables.set('A', 2)
      tbasic.variables.set('B', 10)
      const line = 'A*B';
      const pos = 0;
      tbasic.parser.setLine(line,pos);
      expect(expression.get_expression()).to.equal(20)
    })

    it('term деление 2 переменных', function() {
      tbasic.variables.set('A', 500)
      tbasic.variables.set('B', 5)
      const line = 'A/B';
      const pos = 0;
      tbasic.parser.setLine(line,pos);
      expect(expression.get_expression()).to.equal(100)
    })

    it('unsignedexpr сложение', function() {
      const line = '10+7';
      const pos = 0;
      tbasic.parser.setLine(line, pos);
      expect(expression.get_expression()).to.equal(17)
    })

    it('unsignedexpr вычитание', function() {
      const line = '25-8';
      const pos = 0;
      tbasic.parser.setLine(line, pos);
      expect(expression.get_expression()).to.equal(17)
    })

    it('unsignedexpr переменная сложение', function() {
      tbasic.variables.set('L', 2)
      const line = 'L+1000';
      const pos = 0;
      tbasic.parser.setLine(line, pos);
      expect(expression.get_expression()).to.equal(1002)
    })

    it('unsignedexpr переменная вычитание', function() {
      tbasic.variables.set('P', 33)
      const line = 'P-19';
      const pos = 0;
      tbasic.parser.setLine(line, pos);
      expect(expression.get_expression()).to.equal(14)
    })

    it('unsignedexpr 2 переменные сложение', function() {
      tbasic.variables.set('M', 30)
      tbasic.variables.set('K', 15)
      const line = 'M+K';
      const pos = 0;
      tbasic.parser.setLine(line, pos);
      expect(expression.get_expression()).to.equal(45)
    })

    it('unsignedexpr 2 переменные вычитание', function() {
      tbasic.variables.set('A', 90)
      tbasic.variables.set('X', 100)
      const line = 'X-A';
      const pos = 0;
      tbasic.parser.setLine(line, pos);
      expect(expression.get_expression()).to.equal(10)
    })

    it('expr -', function() {
      const line = '-234';
      const pos = 0;
      tbasic.parser.setLine(line, pos);
      expect(expression.get_expression()).to.equal(-234)
    })

    it('expr - переменная', function() {
      tbasic.variables.set('V', 342)
      const line = '-V'
      const pos = 0;
      tbasic.parser.setLine(line, pos);
      expect(expression.get_expression()).to.equal(-342)
    })

    it('mixed all', function() {
      tbasic.variables.set('A', 900)
      tbasic.variables.set('B', -1/10)
      const line = '(((-A*B)+20)*3)-300';
      const pos = 0;
      tbasic.parser.setLine(line, pos);
      expect(expression.get_expression()).to.equal(30)
    })
    it('expression числа в скобках', function () {
      const line = '(60+10)*2';
      const pos = 0;
      tbasic.parser.setLine(line, pos);
      expect(expression.get_expression()).to.equal(140) 
    })

  })
})   