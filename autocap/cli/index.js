#!/usr/bin/env node

require('@babel/register')({
  presets: [
    '@babel/preset-env'
  ],
  ignore: [
    /node_modules\/(?!@ones-ai)/ // ignore node_modules except @ones-ai packages
  ]
});

const runner = require('./runner');
const logger = require('../core/utils/logger')('cli');

// program info
const version = require('../package.json').version;
//
// // parse arguments
// const argsOptions = parseArgs(process.argv.slice(2), {});

// execute program
let exitCode = 0;
// const commandName = argsOptions._[0] || 'help';

runner(version).catch(function () {
  exitCode = 1;
});

/**
 * Program end handling
 */
process.on('exit', (code) => {
  process.exit(code || exitCode);
});

process.on('uncaughtException', (err) => {
  logger.error('Uncaught exception:', err.message, err.stack);
  throw err;
});
