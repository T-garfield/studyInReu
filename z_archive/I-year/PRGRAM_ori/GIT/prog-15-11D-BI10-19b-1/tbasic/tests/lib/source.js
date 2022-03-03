/* globals describe, before, beforeEach, after, afterEach, it */

'use strict'

const chai = require('chai')
//var assert = chai.assert
const expect = chai.expect
//var should = chai.should()


// declaring global vars
let source
let lineParser


describe('source', function () {

  before('before', function () {
    const LineParser = require('../../lib/lineParser.js');
    const Source = require("../../lib/source.js");
    lineParser = new LineParser();
    source = new Source(lineParser);
  })

  beforeEach('beforeEach', function () {
  })

  afterEach('afterEach', function () {
  })

  after('after', function () {
  })

  describe('insert new line', function() {
    //Сапронова, Фонина
    it('is a function', function () {
    expect(source.save).to.be.a('function')})

    it('working test 1', function(){
    source.lines=[
      '10 string1',
      '20 string2'
    ]

    source.insert('15 string3')
    expect(source.lines[0]).to.equal('10 string1')
    expect(source.lines[1]).to.equal('15 string3')
    expect(source.lines[2]).to.equal('20 string2')
  })

    it('working test 2', function(){
      source.lines=[]
      source.insert('15 string3')
      expect(source.lines[0]).to.be.equal('15 string3')
    })

    it('working test 3', function(){
      source.lines=['10 string1']
      source.insert('15 string3')
      expect(source.lines[0]).to.equal('10 string1')
      expect(source.lines[1]).to.equal('15 string3')
    })
  }) 

  describe('source.save', function() { 
    //  Горбачев, Калинин
    it('is a function', function () { 
    expect(source.save).to.be.a('function'); 
    }); 
    
    it('file', function(){ 
    source.lines = ['- Привет, как делишки?', '- Да не плохо, вот на работу иду ', '- Какаие планы на вечер?', '- Никаких. А что? Есть предложения?', "*******"] 
    source.save('lib/testSuperWowCoolATTENTIONpls.txt') 
    expect(source.speclines).to.equal(`- Привет, как делишки?\r\n- Да не плохо, вот на работу иду \r\n- Какаие планы на вечер?\r\n- Никаких. А что? Есть предложения?\r\n*******`) 
    }); 
    
    })

  
    describe('source.load', function() {;

  })

  describe('source.save', function () {
    

    it('file', function () {
      source.lines = ['- Привет, чем занят?', '- Я пожарiв окорочёк ', '- Ну и как?', '- Пааахнет як - вкуусно', "*******"]
      source.save('SuperWowCoolATTENTIONpls.txt')
      expect(source.lines).to.equal(`- Привет, чем занят?\r\n- Я пожарiв окорочёк \r\n- Ну и как?\r\n- Пааахнет як - вкуусно\r\n*******`)
    });
          //Горбачев, Калинин
      it('is a function', function () {
        expect(source.save).to.be.a('function');
      });

      it('file', function () {
        source.lines = ['- Привет, какие планы на вечер?', '- Я пожарю окорочок ', '- А завтра ты свободен? ', '- Нет, завтра иду в барбершоп.', "*******"]
        source.save('Okorochek.txt')
        expect(source.lines).to.equal(`- Привет, какие планы на вечер?\r\n- Я пожарю окорочок \r\n- А завтра ты свободен? \r\n- Нет, завтра иду в барбершоп.\r\n*******`)
      });
    })

    describe('source.load', function () {
      it('filename', function () {
        source.load("lib/lol.txt");
        expect(source.line[0]).to.equal("aaaaaaaa");
      })

      describe('clear', function () {

      })

      describe('_find', function () {
        //Пояркова, Дьячков, Назаров
        it('is a function', function () {
          expect(source._find).to.be.a('function');
        });

        it('num == label (only labels at lines)', function () {

          const label = 1234;
          source.lines = [
            '1234',
            '3456',
          ];
          source.lineIdx = 0;
          source.label = 0;

          source._find(label);

          //console.log(num);
          expect(source._find(label)).to.equal(true);
        });

        it('num == label (labels with some text)', function () {

          const label = 1234;
          source.lines = [
            '1234 AAA',
            '3456 BBB',
          ];
          source.lineIdx = 0;
          source.label = 0;

          source._find(label);

          //console.log(num);
          expect(source._find(label)).to.equal(true);
        });

        it('num !== label', function () {
          const label = 1234;
          source.lines = [
            '7890',
            '3456'
          ];
          source.lineIdx = 0;
          source._find(label);
          expect(source._find(label)).to.equal(false);
        });
      });

      describe('gotoIdx', function () {

      });

      describe('_findNext', function () {
        // выполнено: Хайретдинова, Голованова, Нгуен Нгок Ань
        it('is a function', function () {
          expect(source._findNext).to.be.a('function');
        });
        it('findNext works true', function () {
          source.lines = ['10 str1','20 str2', '30 str3'];
          source.lineIdx = 1;
          source.label = 1020;
          expect(source._findNext()).to.equal(true);
        });

        it('works wrong', function () {
          source.lines = ['10 str1','20 str2', '30 str3'];
          source.lineIdx = 9;
          source.label = 40;
          expect(source._findNext()).to.equal(false);
        });
        it('var for label', function() {
          source.lines = ['10 str1','20 str2', '30 str3'];
          source.lineIdx = 1;
          source.label = 10;
          source._findNext()
          expect(source.label).to.equal(30)
        });

      });


      describe('goto', function () { //dyachkov-nazarov-poyarkova
        it('is a function', function () {
          expect(source.goto).to.be.a('function');
        });

        it('if this._find(label) = true', function () {
          source.lines = ['1010 dvatri','1020 shest']
          expect(source.goto(1010)).to.equal(true)
          expect(source.label).to.equal(1010)
        });

        /* alykoshin >>> */
        it('if this._find(label) = true (2)', function () {
          source.lines = [
            '1010 ten',
            '1020 twenty',
            '1030 thirty',
          ];
          source.lineIdx = 0;
          const result = source.goto(1030);
          expect(result).to.equal(true)
          expect(source.label).to.equal(1030)
          expect(source.lineIdx).to.equal(2)
        });

        it('if this._find(label) != true', function () {
          source.lines = ['1010 dvatri','1020 shest']
          expect(function(){source.goto(2110);}).to.throw('error')
        });

      });


    });

  });


describe('gotoNext', function () {
  it('is a function', function () {
    expect(source.gotoNext).to.be.a('function');
  });

  it("Lable is null ", function () {
    const label = '1230';
    const lines = ['1000 Hello', '1001 World'];
    source._findNext(label);
    source.gotoNext(label);
    expect(source.gotoNext(label)).to.equal(true);
  });

  it("Label is not null ", function () {
    const label = '1010';
    const lines = ['1010 Hello', '1020 World'];
    source._findNext(label);
    source.gotoNext(label);
    expect(source.gotoNext(label)).to.equal(true);
  });

});


