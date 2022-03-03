/* globals describe, before */

'use strict'

const chai = require('chai')
//const assert = chai.assert
const expect = chai.expect
//const should = chai.should()
const fs = require('fs');

const Tbasic = require('../../lib/tbasic');
const Operators = require('../../lib/operators.js')
const source = require('../../lib/source.js');
const LineScanner = require('../../lib/lineScanner.js');

// declaring global vars
let tbasic;

describe('operators', function () {

  before('before', function () {
    // initializing common test data
    tbasic = new Tbasic();
  })

  describe('CLEAR', function () {

    it("clears source", function () {
      tbasic.source.lines = ['line', 'line2'];
      tbasic.source.label = 111;
      tbasic.source.lineIdx = 1;
      tbasic.operators.handlers.clear();
      expect(tbasic.source.lines.length).to.equal(0);
      expect(tbasic.source.label).to.equal(0);
      expect(tbasic.source.lineIdx).to.equal(0);
    })

  })

  describe('load', function () {
    //Горбачев, Калинин

    it('is a function', function() { 
    expect(tbasic.operators.handlers.load).to.be.a('function'); 
    }); 
    
    it('proverka 1', function(){ 
    tbasic.source.clear() 
    tbasic.source.insert('1 LOAD "../tbasic/tests/lib/rr.txt"') 
    tbasic.source.goto(1) 
    tbasic.parser.pos=6 
    tbasic.operators.handlers.load() 
    
    expect(tbasic.source.lines[0]).to.equal('1000 hhhhh') 
    }) 
    it('proverka 2', function(){ 
    tbasic.source.clear() 
    tbasic.source.insert('1 INPUT R, J') 
    tbasic.source.goto(1) 
    tbasic.parser.pos=7 
    tbasic.operators.handlers.input() 
    tbasic.source.insert('2 LOAD "../tbasic/tests/lib/rr.txt"') 
    tbasic.source.goto(2) 
    tbasic.parser.pos=6 
    tbasic.operators.handlers.load() 
    expect(tbasic.variables.values.size).to.equal(0) 
    }) 


    it('is a function', function () {
      expect(tbasic.operators.handlers.load).to.be.a('function');
    });

    it('proverka 1', function () {
      tbasic.source.clear()
      tbasic.source.insert('1 LOAD "../tbasic/tests/lib/rr.txt"')
      tbasic.source.goto(1)
      tbasic.parser.pos = 6
      tbasic.operators.handlers.load()

      expect(tbasic.source.lines[0]).to.equal('1000 hhhhh')
    })
    it('proverka 2', function () {
      tbasic.source.clear()
      tbasic.source.insert('1 INPUT R, J')
      tbasic.source.goto(1)
      tbasic.parser.pos = 7
      tbasic.operators.handlers.input()
      tbasic.source.insert('2 LOAD "../tbasic/tests/lib/rr.txt"')
      tbasic.source.goto(2)
      tbasic.parser.pos = 6
      tbasic.operators.handlers.load()
      expect(tbasic.variables.values.size).to.equal(0)
    })

  })

  describe('save', function () {
    //Горбачев, Калинин 
    it('is a function', function () {
      expect(tbasic.operators.handlers.save).to.be.a('function');
    });
  });

  describe('input', function () {
    it('is a function', function () {
      expect(tbasic.operators.handlers.input).to.be.a('function');
    });
    it('test 1', function () {
      tbasic.source.clear()
      tbasic.source.insert('1 INPUT R')
      tbasic.source.goto(1)
      tbasic.parser.pos = 7
      tbasic.operators.handlers.input()
      expect(tbasic.variables.get('R')).to.not.equal(null)
    });
    it('test 2', function () {
      tbasic.source.clear()
      tbasic.source.insert('1 INPUT H, P')
      tbasic.source.goto(1)
      tbasic.parser.pos = 7
      tbasic.operators.handlers.input()
      expect(tbasic.variables.get('P')).to.not.equal(null)
    });
    it('test 3', function () {
      tbasic.source.clear()
      tbasic.source.insert('1 INPUT O, T')
      tbasic.source.goto(1)
      tbasic.parser.pos = 7
      tbasic.operators.handlers.input()
      expect(tbasic.variables.get('T')).to.not.equal(null)
    });
  });



  //

  describe('list', function () {
  // Назаров, Дьячков, Пояркова
  it('is a function', function () {
    expect(tbasic.operators.handlers.list).to.be.a('function');
  });

  it('works', function () {
    tbasic.source.lines = ['line', 'haha'];
    tbasic.operators.handlers.list();
    // проверяет действительно ли функция распечатывает массив
  });
  });

  describe('rem', function () {

  it('it is a function', function () {
    expect(tbasic.operators.handlers.rem).to.be.a('function');
  });
  it('goes to the end of a line', function () {
    tbasic.parser.line = 'abcdefghij'
    tbasic.parser.pos = 2;
    tbasic.operators.handlers.rem();
    expect(tbasic.parser.pos).to.equal(9)
  })

  })

  describe('gosub', function () {

  it('it is a function', function () {
    expect(tbasic.operators.handlers.gosub).to.be.a('function');
  });

  it('is stack true?', function () {
    tbasic.source.lines = [
      '10 GOSUB 30  ',   
      '20 a',            
      '30 b',            
      '40 c',            
    ];
    tbasic.source.lineIdx = 0;
    tbasic.parser.line = tbasic.source.lines[tbasic.source.lineIdx];
    tbasic.parser.pos = 8;
    tbasic.operators.stack.length = 0;
    const finalElement = tbasic.operators.stack.length;
    const result = tbasic.operators.handlers.gosub();
    expect(tbasic.operators.stack[finalElement]).to.eql({ lineIdx: 0, pos: 11 })
    expect(tbasic.source.lineIdx).to.equals(2);
    expect(tbasic.source.label).to.equals(30);
  });

  it('stack > 100', function() {
    tbasic.operators.stack.length = 160;
    expect(function() {tbasic.operators.handlers.gosub()}).to.throw('Error!');
  });
 
  });



  describe('if', function () {
  // Назаров, Дьячков, Пояркова
  it('is a function', function () {
    expect(tbasic.operators.handlers.if).to.be.a('function');
  });

  it('> false', function () {
    tbasic.parser.pos = 0;
    tbasic.parser.line = ' 5>10 then print';
    tbasic.operators.handlers.if();
    expect(tbasic.operators.handlers.if()).to.equal('следующая строка');
  });

  it('> true', function () {
    tbasic.parser.pos = 0;
    tbasic.parser.line = ' 15>10 THEN print';
    tbasic.operators.handlers.if();
    expect(tbasic.parser.pos).to.equal(12);
  });
  });

  describe('else', function () {
    //Сапронова, Фонина, Голованова, Хайретдинова
    it('is a function', function () {
      expect(tbasic.operators.handlers.else).to.be.a('function');
    });

    it('reading IF', function () {
      tbasic.parser.line = 'IF 30<100 THEN PRINT';
      tbasic.parser.pos = 0;
      const res = tbasic.operators.handlers.else();
      console.log(res);
      expect(res).to.be.a('следующая строка');
    });
  })

  describe('run', function () {
  it('is a funcion', function () {
    expect(tbasic.operators.handlers.run).to.be.a('function');
  });
  it("clears", function () {
    tbasic.source.lines = ['line', 'line2'];
    tbasic.source.label = 111;
    tbasic.source.lineIdx = 1;
    tbasic.operators.handlers.clear();
    expect(tbasic.source.lines.length).to.equal(0);
    expect(tbasic.source.label).to.equal(0);
    expect(tbasic.source.lineIdx).to.equal(0);
  });
  });

  describe('return', function() { 
  // Ибрагимова, Бутова

    it('is a function', function() {
    expect(tbasic.operators.handlers.return).to.be.a('function');
    })
    it('test for normal work ', function() {
    tbasic.operators.stack = [{ 'lineIdx': 2, 'pos': 4 }]
    tbasic.operators.handlers.return()
    expect(tbasic.source.lineIdx).to.equal(2)
    expect(tbasic.parser.pos).to.equal(4)
    })
    });

    describe('print',function() { // Ибрагимова, Бутова
      it('print string', function () {
      tbasic.source.lines = ['12 GOSUB 49', '32 PRINT "abc";', '49 RETURN'];
      tbasic.parser.line = tbasic.source.lines[1];
      tbasic.source.lineIdx = 1;
      tbasic.parser.pos = 8;
      tbasic.operators.handlers.print();
      expect(tbasic.parser.pos).to.equal(15);
      })
      it('print string not ending with "," or ";"', function () {
      tbasic.source.lines = ['12 GOSUB 49', '32 PRINT "abc"', '49 RETURN'];
      tbasic.parser.line = tbasic.source.lines[1];
      tbasic.source.lineIdx = 1;
      tbasic.parser.pos = 8;
      tbasic.operators.handlers.print();
      expect(tbasic.parser.pos).to.equal(14);
      })
      it('print number', function () {
      tbasic.source.lines = ['12 GOSUB 49', '32 PRINT 3', '49 RETURN'];
      tbasic.parser.line = '32 PRINT 3';
      tbasic.source.lineIdx = 1;
      tbasic.parser.pos = 8;
      tbasic.operators.handlers.print();
      expect(tbasic.parser.pos).to.equal(10);
      })
      it('print string + number', function () {
      tbasic.source.lines = ['12 GOSUB 49', '32 PRINT "abc "; 3,', '49 RETURN'];
      tbasic.parser.line = '32 PRINT "abc "; 3,';
      tbasic.source.lineIdx = 1;
      tbasic.parser.pos = 8;
      tbasic.operators.handlers.print();
      expect(tbasic.parser.pos).to.equal(19);
      })
      })


 describe('GOTO ', function() {

      it('is a function', function() {
          expect(tbasic.operators.handlers.list).to.be.a('function');
      })

      it("строка существует", function() {
          tbasic.source.lines = ['10 110>100 THEN', '15 TEXT', '20 TEXT'];
          tbasic.source.label = 10;
          tbasic.source.lineIdx = 0;
          tbasic.parser.line = 'GOTO 10'
          tbasic.parser.pos = 5
          expect(tbasic.source.label).to.equal(10);
          expect(tbasic.source.lineIdx).to.equal(0);
          });

   // alykoshin >>>
   it("строка существует", function() {
     tbasic.source.lines = [
       '10 110>100 THEN', // 1
       '15 TEXT',         // 2
       '20 GOTO 15',      // 3
//      01234567890
       '30 TEXT',         // 4
     ];
     tbasic.source.label = 20;
     tbasic.source.lineIdx = 3;
     tbasic.parser.line = tbasic.source.lines[tbasic.source.lineIdx];
     tbasic.parser.pos = 7
     const result = tbasic.operators.handlers.goto();
     expect(result).to.equals(true);
     expect(tbasic.source.label).to.equal(15);
     expect(tbasic.source.lineIdx).to.equal(1);
   });
   // <<< alykoshin

      it("строки не существует", function() {
          tbasic.source.lines = ['10 110>100 THEN', '15 TEXT', '20 TEXT'];
          tbasic.source.label = 10;
          tbasic.source.lineIdx = 0;
          tbasic.parser.line = 'GOTO 30'
          tbasic.parser.pos = 5
          expect(function() { tbasic.operators.handlers.goto() }).to.throw(Error);
      });
  });
});
