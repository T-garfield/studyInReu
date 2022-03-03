/* globals describe, before, beforeEach, after, afterEach, it */

'use strict';

const chai = require('chai');
//const assert = chai.assert;
const expect = chai.expect;
//const should = chai.should();


// declaring global vars
let lineParser;


describe('LineParser', function() {

  before('before', function() {
    const LineParser = require('../../lib/lineParser.js');
    lineParser = new LineParser();
  });


  describe('getVariable', function() {
    //Хайретдинова, Голованова
    it('is a function', function () {
      expect(lineParser.getVariable).to.be.a('function');
    });

    it('getSpaces is a function', function () {
      expect(lineParser.getSpaces).to.be.a('function');
    });
  
    it('Returning var name', function () {
      const line = '  a ';
      const pos = 1;
      lineParser.setLine(line, pos)
      
      expect(lineParser.getVariable()).to.equal('A');
    });
    
    it('There is a space', function () {
      const line = 'a bcd e';
      const pos = 1;
      lineParser.setLine(line, pos)
      
      expect(lineParser.getVariable()).to.equal('B');
    });
    
    it('Starting with space', function () {
      const line = ' 203 59';
      const pos = 0;
      lineParser.setLine(line, pos)

      expect(lineParser.getVariable()).to.equal(null);
    });
  });  
});
  


describe('getQuotedString', function() {
  //Сапронова, Фонина  
 it('is a function', function () {
   expect(lineParser.getQuotedString).to.be.a('function');
 });

 it('test 1',function(){
   const line = '"abcd"'
   const pos = 0
   lineParser.setLine(line, pos)
   expect(lineParser.getQuotedString()).to.equal('abcd')
 });

 it('test 2',function(){
   const line = '   "efgh"'
   const pos = 0
   lineParser.setLine(line, pos)
   expect(lineParser.getQuotedString()).to.equal('efgh')
 })  
 
 it('test 3',function(){
   const line = '""'
   const pos = 0
   lineParser.setLine(line, pos)
   expect(lineParser.getQuotedString()).to.equal('')
 }) 
 it('test error',function(){
   const line = '"mnop'
   const pos = 0
   lineParser.setLine(line, pos)
   expect(lineParser.getQuotedString.bind()).to.throw();
 }) 

 it('test null 1',function(){
  const line = '"igkl"'
  const pos = 2
  lineParser.setLine(line, pos)
  expect(lineParser.getQuotedString()).to.equal(null)
 })

 it('test null 2',function(){
   const line = '   '
   const pos = 0
   lineParser.setLine(line, pos)
   expect(lineParser.getQuotedString()).to.equal(null)
 }) 

});
