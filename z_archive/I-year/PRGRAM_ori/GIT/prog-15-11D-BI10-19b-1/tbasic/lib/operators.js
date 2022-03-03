/**
 * Created by alykoshin on 18.10.16.
 */

'use strict';

const PromptSync = require('prompt-sync');

const debug = require('./debug.js');
const ERRORS = require('./errors.json');

const promptSync = require('prompt-sync')({
  sigint: true,
});


const _print = function (s) {
  // fix to avoid ERR_STREAM_NULL_VALUES error
  // if function was called with null value
  if (s === null) return;
  process.stdout.write(s);
};

const _input = function (question = '?') {
  return promptSync(question);
}


class Operators {

  constructor(tbasic) {
    this.tbasic = tbasic;
    this.stack = []; // GOSUB / RETURN stack
    this.loopStack = []; // FOR / NEXT stack

    // use `self` to access `this` inside handlers
    const self = this;

    this.handlers = {

      // File I/O

      //
      load() {
        //Горбачев, Калинин
        var t = self.tbasic.parser.getQuotedString()
        self.tbasic.source.load(t)
        self.tbasic.variables.reset()
      },


      //Горбачев, Калинин
      save(string) {
        fs.writeFileSync(string, self.tbasic);
      },
      //

      clear() {
        self.tbasic.source.clear();
      },

      list() {
        //  throw new Error('Not implemented');
        // Дьячков, Назаров, Пояркова
        for (var i = 0; i <= self.tbasic.source.lines.length - 1; i++) {
          console.log(self.tbasic.source.lines[i]);
        }
      },
      //
      //

      rem() { //Хайретдинова, Голованова
        self.tbasic.parser.pos = self.tbasic.parser.line.length - 1
      },

      //
      //


      goto() {
        if (self.tbasic.parser.testSpace()) {
            self.tbasic.parser.getSpaces()
        }
        let specialLabel = self.tbasic.expression.get_expression()
        for (let i = 0; i < self.tbasic.source.lines.length; i++) {
            self.tbasic.parser.pos = 0;
            if (self.tbasic.parser.testSpace()) {
                self.tbasic.parser.getSpaces()
            }

            self.tbasic.parser.line = self.tbasic.source.lines[i]
            let linesLabel = self.tbasic.parser.getNumber()
            if (linesLabel === specialLabel) {
                self.tbasic.source.label = specialLabel;
                self.tbasic.source.lineIdx = i
                return
            }
        }
       
    },


      run() {
        let nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9'];
        if (this.line === nums) {
          self.tbasic.source.run();
        } else {
          this.line <= this.line[0];
          self.tbasic.source.run();
        };
      },

      //
      // print() {
      //   throw new Error('Not implemented');
      // };
      //
      input() {
        do {
          self.tbasic.parser.getSpaces()
          var t = self.tbasic.parser.getVariable()
          if (t !== null) {
            let h = _input()
            h = Number(h)
            self.tbasic.variables.set(t, h)
          }
        } while (self.tbasic.parser.getChar(','))
      },
      //
      // let() {
      //   throw new Error('Not implemented');
      //};
      //
      if() {
        //throw new Error('Not implemented');
        // Дьячков, Назаров, Пояркова
        let strings = ['>', '<', '=', '<>', '<=', '>=', '><'];
        self.tbasic.parser.getSpaces();
        //let y = self.tbasic.parser.getNumber();
        let y = self.tbasic.expression.get_expression();
        let compare = self.tbasic.parser.getStrings(strings);
        
        //let z = self.tbasic.parser.getNumber();
        let z = self.tbasic.expression.get_expression();
        console.log('>>>', y, compare, z);
        if ((compare === '<' && y < z) || (compare === '>' && y > z) ||
          (compare === '=' && y === z) || (compare === '<>' && y !== z) ||
          (compare === '><' && y !== z) || (compare === '<=' && y <= z) || 
          (compare === '>=' && y >= z)) {
            self.tbasic.parser.pos++;
          self.tbasic.parser.getSpaces();
          if (self.tbasic.parser.getString('THEN')) {
            self.tbasic.parser.getSpaces();
          } else {
            throw new Error('не найден THEN');
          }
        } else {
          //self.parser.source.goToNext()
          //но из-за того, что она не готова
          return 'следующая строка'
        }

      },
      //
      
      else() { //Хайретдинова, Голованова, Сапронова, Фонина
        self.tbasic.parser.getSpaces()
        if (self.tbasic.parser.getString('IF')) {
            this.if()
        }
      },

      gosub() { //Хайретдинова, Голованова
        self.tbasic.parser.getSpaces();
        const label = self.tbasic.parser.getNumber();
        self.stack.push({ lineIdx: self.tbasic.source.lineIdx, pos: self.tbasic.parser.pos });
        const MAX_STACK_LENGTH = 100
        if (self.stack.length <= MAX_STACK_LENGTH) {
          self.tbasic.source.goto(label);
        }
        else {
          throw new Error('Error!');
        }
      },

      return() { // Ибрагимова, Бутова
        if (self.stack.size === 0) { throw new Error('Нет парного оператора') }
        const dic = self.stack.pop();
        self.tbasic.source.lineIdx = dic.lineIdx
        self.tbasic.parser.pos = dic.pos
        return dic

      },
      end() {
        return false
      },

      print() { // Ибрагимова, Бутова 
        for (let i = self.tbasic.parser.pos; i < self.tbasic.parser.line.length; i++) {
          if (self.tbasic.parser.testSpace()) {
            self.tbasic.parser.getSpaces();
            i = self.tbasic.parser.pos;
          }
          if (self.tbasic.parser.line[i] === '"') {
            _print(self.tbasic.parser.getQuotedString());
            i = self.tbasic.parser.pos + 1;
          }
          if (self.tbasic.parser.line[i] === ';' || self.tbasic.parser.line[i] === ',') {
            i++;
            self.tbasic.parser.pos = i;
          }
          self.tbasic.parser.pos = i;
          if (self.tbasic.parser.testNumber()) {
            let x = self.tbasic.parser.getNumber().toString();
            _print(x);
          }
        }
      },
    };
  }

}


module.exports = Operators;
