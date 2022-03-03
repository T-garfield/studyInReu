/**
 * Created by alykoshin on 20.09.16.
 */

'use strict';

var util = require('util');

const debug      = require('./debug.js');
const ERRORS     = require('./errors.json');

const LineParser = require('./lineParser.js');
const Source     = require('./source.js');
const Variables  = require('./variables.js');
const Operators  = require('./operators.js');
const Expression = require('./expression.js');

// for future use
//var ErrorHandler = require('./errorHandler.js');



class Tbasic {

  constructor() {
    this.dataStack = []; // PUSH() / POP() stack

    this.variables  = new Variables();
    this.parser     = new LineParser();
    this.source     = new Source(this.parser);
    this.operators  = new Operators(this);
    this.expression = new Expression(this);

    this.stack     = []; // GOSUB / RETURN stack
    this.loopStack = []; // FOR / NEXT stack

    // Init the object
    this.source.clear();
    //this.operators.handlers.clear();

    this.operators.handlers.dump = () => {
      console.log(util.inspect(this, {depth:5}));
    };

  }


  _debugParser(s) {
    function padNum(number, count=2, char='0') {
      return (''+number).padStart(count, char);
    }
    //s += ': ' + `this.parser.pos: ${this.parser.pos}, line[${this.source.lineIdx}]: \'`;
    //s += `: line[${this.source.lineIdx},${this.parser.pos}/${this.source.label}]: \'`;
    const s1 = `[${padNum(this.source.lineIdx,2)},${padNum(this.parser.pos,2)}/${padNum(this.source.label,3)} '`;
    //const s2 = `${this.parser.line}`.padEnd(30);
    const s2 = this.parser.line;
    const s3 = `'] ${s}: `;
    debug(s1 + s2 + s3);
    debug('-'.repeat(s1.length+this.parser.pos) + '^');
  }


  _inter_statement() {
    //debug(`_inter_statement: this.parser.pos: ${this.parser.pos}`);

    // skip spaces if any
    this.parser.getSpaces();
    //debug(`_inter_statement: this.parser.pos: ${this.parser.pos}`);

    // check if we are at the end of line
    if (this.parser.isEOL()) {    // We are at the end of current line and
      if (this.source.label != 0) {  // ... we are interpreting the text, not single line in interactive mode
        debug(`_inter_statement: we had label at current line: non-interactive mode (label:${this.source.label}), moving to next line`);

        if (!this.source.gotoNext()) { // go to next line if possible
          debug('_inter_statement: stopping: this.source.gotoNext() returned false');
          return false;                         // if not - interrupt
        }
        // in case getSpaces() was not called inside gotoNext()
        this.parser.getSpaces();

      } else { // interactive mode: (this.source.label === 0)
        debug(`_inter_statement: stopping: we had no label at current line: interactive mode (label:${this.source.label})`);
        return false;                         // if not - interrupt

      }

      //return true;
    }
    this._debugParser(`_inter_statement: continue`);
    return true;
  }


  _pre_statement() {
    if (! this._inter_statement()) {
      return false;
    }
    return true;
  }


  _post_statement() {
    //debug(`_post_statement: this.parser.pos: ${this.parser.pos}`);
    if (! this._inter_statement()) {
      debug(`_post_statement: stopping: _inter_statement() returned false`);
      return false; // stop interpretation
    }
    if (this.parser.getString(':')) {
      debug(`_post_statement: found \':\', continue same line`);
      // do nothing - proceed to next statement
    }

    return true;
  }


  do_statement() {
    if (!this._pre_statement()) { return false; }

    this._debugParser(`do_statement: after _pre_statement `);
    for (let name in this.operators.handlers) { if (typeof this.operators.handlers[name] === 'function') {
      //this._debugParser(`do_statement: after _pre_statement ${name}`);
      if (this.parser.getString(name)) {
        this.parser.getSpaces();

        this._debugParser(`do_statement('${name}'): in `);
        const res = this.operators.handlers[name]();
        this._debugParser(`do_statement('${name}'): out res: ${res}`);

        // STOP/END operators
        if (res === false) {
          this._debugParser(`do_statement('${name}'): stopping`);
          return false;
        }

        return this._post_statement();
      }

    } } // for

    ///*
    let OPTION_DEFAULT_LET = false;
    if (OPTION_DEFAULT_LET) {
      this._debugParser(`do_statement/default`);
      this.operators.handlers.let(); // by default do LET
      return this._post_statement();

    } else {
      //*/
      // unable to interpret
      throw new Error(ERRORS.BAD_SYNTAX);
      ///*
    }
    //*/
  };

  do_line_interactive(line) {
    // init parser with this line
    this.parser.setLine(line);
    // check if line starts with a number
    if (this.parser.getNumber() !== null) {  // if line starts with a number
      debug('line starts with a number - store it');
      this.source.insert(line);              // store it in array of source lines
      debug('stored');

    } else {                                 // otherwise, execute it
      this.source.label = 0;
      let cont;
      do {
        cont = this.do_statement();
      } while (cont);

      if (this.source.label) console.log(`STOPPED AT LINE ${this.source.label}`)
    }
    return true;
  };

}


module.exports = Tbasic;
