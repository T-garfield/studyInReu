/**
 * Created by alykoshin on 20.09.16.
 */

'use strict';

const fs = require('fs');
//const readline = require('readline');
//const readlineSync = require('readline-sync');
const PromptSync = require('prompt-sync');
const PromptSyncHistory = require('prompt-sync-history');

const packageJson  = require('./package.json');
const debug  = require('./lib/debug.js');
const ERRORS = require('./lib/errors.json');
const Tbasic = require('./lib/tbasic.js');

// for future use
//var ErrorHandler = require('./lib/errorHandler.js');


(function() {

  const tbasic = new Tbasic();
  //console.log(`TinyBasic (js) v.${packageJson.version}`);
  console.log(`TinyBasic (js)`);

  //const opNames = Object.getOwnPropertyNames(tbasic.operators);
  //const opNames = Object.(Object.getPrototypeOf(tbasic.operators));
  const opNames = Object.keys(tbasic.operators.handlers);
  debug('Available operators: '+ opNames.join(', '));

  // load file if provided in command line
  if (process.argv[2]) {
    tbasic.source.load(process.argv[2]);
  }

  const HISTORY_FILE = '.tbasic.history';

  function autocomplete(commands) {
    return function (str) {
      return commands.sort().filter(c => c.indexOf(str) === 0);
    };
  }
  const operators = Object.keys(tbasic.operators.handlers);
  const completions =  operators.map(o => o+' ');

  const promptSync = PromptSync({
    history: PromptSyncHistory(HISTORY_FILE, 100),
    autocomplete: autocomplete(completions),
    sigint: true,
  });

  let cont = true;
  do {
    const line = promptSync('> ');

    // 'prompt-sync' package recommended for INPUT is pausing stdin
    // we need to resume it
    //process.stdin.resume();
    //process.stdout.resume();

    promptSync.history.save();

    try {
      cont = !line || tbasic.do_line_interactive(line);

    } catch(e) {
      console.log(`ERROR AT LINE ${tbasic.source.label} POS ${tbasic.parser.pos}`);
      console.log(`${tbasic.parser.line}`);
      let s = '';
      for (let i=0; i<tbasic.parser.pos; i++) s += ' ';
      s += '^';
      console.log(s);
      debug(`line: "${tbasic.parser.line}", pos: ${tbasic.parser.pos}`);
      console.log(e);
    }
  } while (cont);

  //function exit() {
  //  process.exit(0);
  //}

})();
