/* globals describe, before, beforeEach, after, afterEach, it */

'use strict';

const chai = require('chai');
//const assert = chai.assert;
const expect = chai.expect;
//const should = chai.should();


// declaring global vars
let variables;


describe('Variables', function() {

  before('before', function() {
    // initializing common test data
    const Variables = require('../../lib/variables.js');
    variables = new Variables();
  });

  beforeEach('beforeEach', function() {
  });

  afterEach('afterEach', function() {
  });

  after('after', function() {
  });

 //poyarkova_butova_ibragimova
  describe('set', function () {
    it('is a function', function () {
      expect(variables.set).to.be.a('function');
    });

    it('name = nanana, value = bebebe', function () {
      const varName = 'nanana';
      const varValue = 'bebebe';
      variables.set(varName, varValue);
      expect(variables.set(varName, varValue)).to.equal('bebebe');
    });
  });

  describe('reset', function() { // Ибрагимова, Бутова, Нгуен Дык Тхиен
 
    it('is a function', function() {
    expect(variables.reset).to.be.a('function');
    });
    
    it('test for working', function() {
    variables.set(1, 'test');
    variables.reset()
    expect(variables.reset()).to.equal(true);
    });
  });

  describe('get', function () { //dyachkov-nazarov-poyarkova

    it('is a function', function () {
      expect(variables.get).to.be.a('function');
    });

    it('return value if varName is defined', function () {
      let varName = 'sss';
      let varValue = 5;
      variables.set(varName, varValue)
      variables.get(varName);
      expect(variables.get(varName)).to.equal(5);
    });

    it('0 if value of varName is undefined', function () {
      let varName = 'sss'
      let varValue;
      variables.set(varName, varValue)
      variables.get(varName);
      expect(variables.get(varName)).to.equal(0);
    });

  })

});
