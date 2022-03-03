/* globals describe, before, beforeEach, after, afterEach, it */

'use strict';

const chai = require('chai');
//const assert = chai.assert;
const expect = chai.expect;
//const should = chai.should();


// declaring global vars
let lineScanner;


describe('LineScanner', function () {

  before('before', function () {
    // initializing common test data
    const LineScanner = require('../../lib/lineScanner.js');
    lineScanner = new LineScanner();
  });

  beforeEach('beforeEach', function () {
  });

  afterEach('afterEach', function () {
  });

  after('after', function () {
  });

  //

  describe('isBOL', function () {
    //кем выполнено: Хайретдинова, Голованова
    it('is a function', function () {
      expect(lineScanner.isBOL).to.be.a('function');
    });

    it('if pos = 0 true?', function () {
      const line = 'this is a line';
      const pos = 0;
      lineScanner.setLine(line, pos);

      console.log(lineScanner.pos);
      console.log(lineScanner.isBOL());
      lineScanner.isBOL();
      expect(lineScanner.isBOL()).to.equal(true);
    });

    it('if pos != 0 false?', function () {
      const line = 'this is a line';
      const pos = 5;
      lineScanner.setLine(line, pos);

      console.log(lineScanner.pos);
      console.log(lineScanner.isBOL());
      lineScanner.isBOL();
      expect(lineScanner.isBOL()).to.equal(false);
    });

  });

  describe('setLine', function () {

    it('(line, pos) sets both properties', function () {
      const line = 'abcdef';
      const pos = 3;
      lineScanner.setLine(line, pos);
      expect(lineScanner.line).to.equal(line);
      expect(lineScanner.pos).to.equal(pos);

    });
  });


  describe('getChars', function () {
    //кем выполнено: Хайретдинова, Голованова
    it('is a function', function () {
      expect(lineScanner.getChars).to.be.a('function');
    });

    it('coincided', function () {
      const line = '123ABC';
      const pos = 1;
      lineScanner.setLine(line, pos);

      const res = lineScanner.getChars('0123456789');

      expect(res).to.equal('2');
      expect(lineScanner.pos).to.equal(2);
    });

    it('did not coincide', function () {
      const line = 'ABC';
      const pos = 1;
      lineScanner.setLine(line, pos);

      const res = lineScanner.getChars('0123456789');

      expect(res).to.equal(null);
    });
  });

 

   describe('isEOL', function() {
      it('is a function', function() {
        expect(lineScanner.isEOL).to.be.a('function');
      });

      it('end of line', function() {
        const line = 'abcdef'
        const pos = 6
        lineScanner.setLine(line, pos)
        expect(lineScanner.isEOL()).to.equal(true)
      });

      it('not end of line', function() {
        const line = 'dfgh';
        lineScanner.setLine(line);
        expect(lineScanner.isEOL()).to.equal(false)
      })

    })
})


  describe('testSpace', function () {

    it('is a function', function () {
      expect(lineScanner.testSpace).to.be.a('function');
    });

    it('has space', function () {
      const line = ' hello';
      const pos = 0;
      lineScanner.setLine(line, pos);

      console.log(lineScanner.pos);
      console.log(lineScanner.testSpace());
      lineScanner.testSpace();
      expect(lineScanner.testSpace()).to.equal(true);
    });

    it('has not space', function () {
      const line = 'hello';
      const pos = '0';
      lineScanner.setLine(line, pos);

      console.log(lineScanner.pos);
      console.log(lineScanner.testSpace());
      lineScanner.testSpace();
      expect(lineScanner.testSpace()).to.equal(false);
    });
  });


  describe('peekChar', function () {
    it('is a function', function () {
      expect(lineScanner.peekChar).to.be.a('function');
    });
    it('if char is not undefined', function () {
      const line = '1234'
      const pos = 1;
      lineScanner.setLine(line, pos);
      lineScanner.peekChar()
      expect(lineScanner.peekChar()).to.equal('2');
    });
    it('char is undefined', function () {
      const line = '';
      const pos = 0;
      lineScanner.setLine(line, pos);
      lineScanner.peekChar()
      expect(lineScanner.peekChar()).to.equal(null);
    });
  });





  describe('getNumber', function () {

    // выпполнено Калининым и Горбачевым
    it('is a function', function () {
      expect(lineScanner.getNumber).to.be.a('function');
    });

    it('Number', function () {
      const line = 'abc123def'
      const pos = 3
      lineScanner.setLine(line, pos)
      const res = lineScanner.getNumber()
      expect(res).to.equal(123)
      expect(lineScanner.pos).to.equal(6)
    });
    it('Number', function () {
      const line = 'abc123def'
      const pos = 0
      lineScanner.setLine(line, pos)
      const res = lineScanner.getNumber()
      expect(res).to.equal(null)
      expect(lineScanner.pos).to.equal(0)
    });
  });

  describe('getCharNot', function () {

    it('is a function', function () {
      expect(lineScanner.getCharNot).to.be.a('function');
    });

    it('doesn\'t match', function () {
      const line = 'abcdef';
      const pos = 3;
      lineScanner.setLine(line, pos);

      const res = lineScanner.getCharNot('0123456789');

      expect(res).to.equal('d');
      expect(lineScanner.pos).to.equal(4);
    });

    it('match', function () {
      const line = 'abcdef';
      const pos = 3;
      lineScanner.setLine(line, pos);

      const res = lineScanner.getCharNot('abcdef');

      expect(res).to.equal(null);
      expect(lineScanner.pos).to.equal(3);

    });

  });


  describe('getSpaces', function () {

    it('is a function', function () {
      expect(lineScanner.getSpaces).to.be.a('function');
    });

    it('Space or tab', function () {
      const line = 'good night'
      const pos = 5
      lineScanner.setLine(line, pos)
      const res = lineScanner.getSpaces()
      expect(res).to.equal(null)
      expect(lineScanner.pos).to.equal(5)
    });

    it('Space or tab', function () {
      const line = 'good night'
      const pos = 0
      lineScanner.setLine(line, pos)
      const res = lineScanner.getSpaces()
      expect(res).to.equal(null)
      expect(lineScanner.pos).to.equal(0)
    });

  });

  describe('getSpace', function () {

    it('is a function', function () {
      expect(lineScanner.getSpace).to.be.a('function');
    });

    it('Space or tab', function () {
      const line = 'We did it together'
      const pos = 2
      lineScanner.setLine(line, pos)
      const res = lineScanner.getSpace()
      expect(res).to.equal(' ')
      expect(lineScanner.pos).to.equal(3)
    });

    it('Space or tab', function () {
      const line = 'We did it together'
      const pos = 0
      lineScanner.setLine(line, pos)
      const res = lineScanner.getSpace()
      expect(res).to.equal(null)
      expect(lineScanner.pos).to.equal(0)
    });

  });

  describe('testString', function () {

    it('is a function', function () {
      expect(lineScanner.testString).to.be.a('function');
    });
    it('string is in a line', function () {
      const str = 'let';
      const line = 'let it snow';
      const pos = 0;
      lineScanner.setLine(line, pos);
      lineScanner.testString(str);
      expect(lineScanner.testString(str)).to.equal(true);
    });

    it('string is not in a line', function () {
      const str = 'sun';
      const line = 'let it snow';
      const pos = 0;
      lineScanner.setLine(line, pos);
      lineScanner.testString(str);
      expect(lineScanner.testString(str)).to.equal(false);
    });

  });

  describe('testStrings(strings)', function () {
    // Пояркова, Дьячков, Назаров
    it('is a function', function () {
      expect(lineScanner.testStrings).to.be.a('function');
    });

    it('есть такая строка', function () {
      const line = 'hey';
      const strings = ['h', 'a', 'n', 'h', '7'];
      lineScanner.setLine(line);
      lineScanner.testStrings(strings);
      expect(lineScanner.testStrings(strings)).to.equal(true);
    });

    it('нет такой строки', function () {
      const line = 'hey';
      const strings = ['a', 'n', '7'];
      lineScanner.setLine(line);
      lineScanner.testStrings(strings);
      expect(lineScanner.testStrings(strings)).to.equal(null);
    });

    it('есть такая строка, если строки больше одного символа', function () {

      const line = 'hey';
      const strings = ['hey', 'abc', 'nono', 'hai', '756'];
      lineScanner.setLine(line);
      lineScanner.testStrings(strings);
      expect(lineScanner.testStrings(strings)).to.equal(true);
    });

    it('нет такой строки, если строки больше одного символа', function () {

      const line = 'hey';
      const strings = ['abc', 'nono', '756'];
      lineScanner.setLine(line);
      lineScanner.testStrings(strings);
      expect(lineScanner.testStrings(strings)).to.equal(null);
    });

  });

  describe('getChar', function () {
    it('is a function', function () {
      expect(lineScanner.getChar).to.be.a('function');
    });

    it('ch is in a line', function () {
      const line = 'summer';
      const pos = 0;
      const ch = 's';
      lineScanner.setLine(line, pos);
      expect(lineScanner.getChar(ch)).to.equal(ch);
      expect(lineScanner.pos).to.equal(pos + 1)
    });

    it('ch is not in a line', function () {
      const line = 'summer';
      const pos = 0;
      const ch = 'w';
      lineScanner.setLine(line, pos);
      expect(lineScanner.getChar(ch)).to.equal(null);
    });

    it('pos > line', function () {
      const line = 'summer';
      const pos = 8;
      const ch = 's';
      lineScanner.setLine(line, pos);
      expect(lineScanner.getChar(ch)).to.equal(null);
    });
  });

  describe('testNumber', function () {
    // Пояркова, Ибрагимова, Бутова
    it('is a function', function () {
      expect(lineScanner.testNumber).to.be.a('function');
    });

    it('typeof this.line[this.pos] = number', function () {
      const line = '12345';
      const pos = 0;
      lineScanner.setLine(line, pos);
      lineScanner.testNumber();
      expect(lineScanner.testNumber()).to.equal(true);
    });

    it('typeof this.line[this.pos] != number', function () {
      const line = 'abcdef';
      const pos = 0;
      lineScanner.setLine(line, pos);
      lineScanner.testNumber()
      expect(lineScanner.testNumber()).to.equal(false);

    });

  });

  describe('testCharNot', function () {
    // Пояркова, Ибрагимова, Бутова
    it('is a function', function () {
      expect(lineScanner.testCharNot).to.be.a('function');
    });

    it('ch == line[pos]', function () {
      const ch = 'n';
      const line = 'nanana';
      const pos = 0;
      lineScanner.setLine(line, pos);
      lineScanner.testCharNot(ch);
      expect(lineScanner.testCharNot(ch)).to.equal(false);
    });

    it('ch !== line[pos]', function () {
      const ch = 'f';
      const line = 'nanana';
      const pos = 0;
      lineScanner.setLine(line, pos);
      lineScanner.testCharNot(ch);
      expect(lineScanner.testCharNot(ch)).to.equal(true);
    });

    it('pos > line.length', function () {
      const ch = 'f';
      const line = 'nanana';
      const pos = 7;
      lineScanner.setLine(line, pos);
      lineScanner.testCharNot(ch);
      expect(lineScanner.testCharNot(ch)).to.equal('выход за пределы строки');
    });

  });

  describe('testChar', function () { //dyachkov-nazarov-treznyuk

    it('is a function', function () {
      expect(lineScanner.testChar).to.be.a('function');
    });

    it('true if line[pos] === ch', function () {
      const line = 'aaaaa';
      const pos = 1;
      const ch = 'a';
      lineScanner.setLine(line, pos)
      lineScanner.testChar(ch);
      expect(lineScanner.testChar(ch)).to.equal(true);
    });

    it('false if line[pos] !== ch', function () {
      const line = 'bbbaa';
      const pos = 1;
      const ch = 'a';
      lineScanner.setLine(line, pos)
      lineScanner.testChar(ch);
      expect(lineScanner.testChar(ch)).to.equal(false);
    });

    it('Index out if pos > line.length - 1', function () {
      const line = 'bbbaa';
      const pos = 7;
      const ch = 'a'
      lineScanner.setLine(line, pos)
      lineScanner.testChar(ch);
      expect(lineScanner.testChar(ch)).to.equal('Index is out of the range');
    });
  });

  describe('shift', function () { //dyachkov-nazarov-treznyuk

    it('is a function', function () {
      expect(lineScanner.shift).to.be.a('function');
    });

    it('true if pos <= line.length - 1 && num is defined', function () {
      const line = 'aaaaaaaaa';
      const pos = 1;
      const num = 2;
      lineScanner.setLine(line, pos);
      lineScanner.testChar(num);
      expect(lineScanner.shift(num)).to.equal(true);
    });

    it('false if pos > line.length - 1 && num is defined', function () {
      const line = 'aaa';
      const pos = 1;
      const num = 3;
      lineScanner.setLine(line, pos);
      lineScanner.testChar(num);
      expect(lineScanner.shift(num)).to.equal(false);
    });

    it('true if pos > line.length - 1 && num is undefined', function () {
      const line = 'aaaa';
      const pos = 1;
      const num = undefined;
      lineScanner.setLine(line, pos);
      lineScanner.testChar(num);
      expect(lineScanner.shift(num)).to.equal(true);
    });

    it('true if pos > line.length - 1 && num is undefined', function () {
      const line = 'aa';
      const pos = 5;
      const num = undefined;
      lineScanner.setLine(line, pos);
      lineScanner.testChar(num);
      expect(lineScanner.shift(num)).to.equal(false);
    });
  });

  describe('testChars', function () {  //dyachkov-nazarov-treznyuk

    it('is a function', function () {
      expect(lineScanner.testChar).to.be.a('function');
    });

    it('true if line[pos] = chars[i]', function () {
      var line = 'aaaaaaaaa';
      var pos = 1;
      var chars = 'abcdefg';
      lineScanner.setLine(line, pos);
      lineScanner.testChar(chars);
      expect(lineScanner.testChars(chars)).to.equal(true);
    });

    it('false if line[pos] != chars[i]', function () {
      var line = '123qpd';
      var pos = 1;
      var chars = 'abcdefg';
      lineScanner.setLine(line, pos);
      lineScanner.testChar(chars);
      expect(lineScanner.testChars(chars)).to.equal(false);
    });

    it('Index is out of the range if line[pos] > chars.length - 1', function () {
      var line = '123qpd';
      var pos = 10;
      var chars = 'abcdefg';
      lineScanner.setLine(line, pos);
      lineScanner.testChar(chars);
      expect(lineScanner.testChars(chars)).to.equal('Index is out of the range');
    });
  });




  describe('getStrings(strings)', function () {
    it('is a function', function () {
      expect(lineScanner.getStrings).to.be.a('function');
    });

    it('есть такая строка', function () {
      const line = 'yes';
      const strings = ["yes", "no", "789"];
      const pos = 0;
      lineScanner.setLine(line, pos);
      const res = lineScanner.getStrings(strings);
      expect(res).to.equal('yes');
      expect(lineScanner.pos).to.equal(1);
    });

    it('нет такой строки', function () {
      const line = 'hi';
      const strings = ["yes", "no", "789"];
      const pos = 1;
      lineScanner.setLine(line, pos);
      lineScanner.getStrings(strings);
      expect(lineScanner.getStrings(strings)).to.equal(null);
    });
  });


  describe('isEOL', function () {

    it('is a function', function () {
      expect(lineScanner.isEOL).to.be.a('function');
    });

    it('end of line to be true', function () {
      const line = 'abcdef'
      const pos = 5
      lineScanner.setLine(line, pos)
      expect(lineScanner.isEOL()).to.equal(true);
    });

    it('not end of line', function () {
      const line = 'dfgh'
      lineScanner.setLine(line);
      expect(lineScanner.isEOL()).to.equal(false);
    });
  });

  describe('getString', function () {
    // Ибрагимова, Бутова

    it('is a function', function () {
      expect(lineScanner.getString).to.be.a('function');
    });

    it('test for normal working', function () {
      const line = 'string'
      lineScanner.setLine(line)
      expect(lineScanner.getString('str')).to.equal('str')
    });

    it('test for differ working', function () {
      const line = 'string'
      lineScanner.setLine(line)
      expect(lineScanner.getString('tr')).to.equal(null)
    });

    it('test for differ working - non-zero pos', function () {
      const line = 'string'
      lineScanner.setLine(line, 1)
      expect(lineScanner.getString('tr')).to.equal('tr')
    });

    it('test for normal working number 2', function () {
      const line = 'string'
      lineScanner.setLine(line)
      lineScanner.getString('str')
      expect(lineScanner.pos).to.equal(3)
    });

  });



  describe('getSpace', function () {

    it('is a function', function () {
      expect(lineScanner.getSpace).to.be.a('function');
    })


    it('test for null working', function () {
      const line = 'abc def'
      const pos = 1
      lineScanner.setLine(line, pos)
      expect(lineScanner.getSpace()).to.equal(null)
    })


    it('test for normal working', function () {
      const line = 'abc def'
      const pos = 3
      lineScanner.setLine(line, pos)
      expect(lineScanner.getSpace()).to.equal(' ')
    })

  });

  describe('getSpaces', function() { // Ибрагимова, Бутова, Нгуен Нгок Ань

    it('is a function', function() {
    expect(lineScanner.getSpaces).to.be.a('function');
    })
    
    it('test for normal working', function() {
    const line = 'abc def'
    const pos = 3
    lineScanner.setLine(line, pos)
    expect(lineScanner.getSpaces()).to.equal(' ')
    })
    
    it('test for null working', function() {
    const line = 'abc def'
    const pos = 1
    lineScanner.setLine(line, pos)
    expect(lineScanner.getSpaces()).to.equal(null)
    })
  });

  describe('testSpace', function() { // Ибрагимова, Бутова, Нгуен Нгок Ань

    it('is a function', function() {
    expect(lineScanner.testSpace).to.be.a('function');
    });
    
    it('in line(pos) exist a tab, return true', function() {
    const line = 'sometext\tsometext';
    lineScanner.setLine(line, 8);
    
    expect(lineScanner.testSpace()).to.equal(true);
    });
    
    it('in line(pos) exist a space, return true', function() {
    const line = 'sometext sometext';
    const pos = 8;
    lineScanner.setLine(line, pos);
    expect(lineScanner.testSpace()).to.equal(true);
    });
    
    it('in line(pos) do not exist a tab or space, return false', function() {
    const line = 'sometextsometext';
    lineScanner.setLine(line, 8);
    
    expect(lineScanner.testSpace()).to.equal(false);
    });
    
    it('pos > line.length', function() {
    const line = 'sometextsometext';
    lineScanner.setLine(line, 100);
    
    expect(lineScanner.testSpace()).to.equal(false);
    });
});

describe('getStrings', function() { // Ибрагимова, Бутова, Нгуен Нгок Ань

  it('is a function', function() {
  expect(lineScanner.getStrings).to.be.a('function');
  });
  
  it('return null if no substr', function() {
  const line = 'foobar';
  lineScanner.setLine(line);
  expect(lineScanner.getStrings(['rrrrr', 'aaaaa', 'baz'])).to.equal(null);
  expect(lineScanner.pos).to.equal(0);
  });
  
  it('returns correct substr', function() {
  const line = 'foobar';
  lineScanner.setLine(line)
  expect(lineScanner.getStrings(['aaa', 'foo', 'dssd'])).to.equal('foo');
  expect(lineScanner.pos).to.equal(3);
  });
  
  it('returns correct longest substr', function() {
  const line = 'foobar';
  lineScanner.setLine(line)
  expect(lineScanner.getStrings(['aaa', 'foo', 'fooba'])).to.equal('fooba');
  expect(lineScanner.pos).to.equal(5);
  });
});
  
