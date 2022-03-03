/**
 * Created by alykoshin on 27.09.16.
 */

"use strict";

const fs = require('fs');

const debug = require('./debug.js');
const ERRORS = require('./errors.json');
//const LineParser = require('./lineParser.js');


class Source {

  constructor(parser) {
    this.parser = parser;
    this.clear();
  }

  clear() {
    this.lines = [];
    this.label = 0;
    this.lineIdx = 0;
  };

  insert(line) {
    // Сапронова, Фонина
    if (this.lines.length > 0) {
      var i = 0
      while (line[i] != ' ') {
        i += 1
      }
      var curnum = Number(line.slice(0, i + 1))
      i = 0
      while (1) {
        var k = 0
        while (this.lines[i][k] != ' ') {
          k += 1
        }
        var arrnum = Number(this.lines[i].slice(0, k + 1))
        if (arrnum > curnum) {
          this.lines.splice(i, 0, line)
          break
        } else if (arrnum === curnum) {
          this.lines[i] = line
          break
        } else if ((arrnum < curnum) && (i === this.lines.length - 1)) {
          this.lines.push(line)
          break
        }
        i += 1
      }
    } else { this.lines.push(line) }
  };

  load(filename) {
    let x = fs.readFileSync(`${filename}`, "utf8", function (error, data) { });
    this.line = x.split(/\r?\n/);
  };

  save(filename) {

    this.speclines = this.lines.join(`\r\n`); 
   fs.writeFileSync(`${filename}`, this.speclines.toString());

    // igorbachev_mkalinin-74-75
    this.lines = this.lines.join(`\r\n`);
    fs.writeFileSync(`lib/${filename}`, this.lines.toString());

  };

  //Горбачев, Калинин



  _indexByNo(label) {
    throw new Error('Not implemented');
  };

  // функции find, _findNext не должны изменять значения label, lineIdx !!!
  _find(label) {
    //Пояркова, Дьячков, Назаров
    for (var i = 0; i < this.lines.length; i++) {
      this.parser.setLine(this.lines[i]);
      let num = this.parser.getNumber();

      if (num == label) {
        this.lineIdx = i;
        this.label = label;
        return true;
      };
    };

    return false;

  };


  // функции find, _findNext не должны изменять значения label, lineIdx !!!
  _findNext(label) {
    if (this.lines.length > this.lineIdx + 1) {
      var pos = this.parser.pos;
      ++this.lineIdx;
      this.parser.setLine(this.lines[this.lineIdx], 0);
      var label = this.parser.getNumber();
      this.label = label;
      this.parser.setLine(this.lineIdx[this.lineIdx - 1], pos);
      return true;
    }
    return false;
  };

  gotoIndexPos(lineIdx, pos) {
    throw new Error('Not implemented');
  };

  goto(label) { //dyachkov-nazarov-poyarkova
    if (this._find(label)) {
      this.parser.setLine(this.lines[this.lineIdx], String(this.label).length);
      return true;
    } else {
      throw new Error('error');
    };

  };



  gotoNext(label) {
    if (this._findNext(label) != null) {
      this.parser.setLine(this._findNext(label), label);
      return true;
    }
    else {
      return false;
    }
  };


}


module.exports = Source;
