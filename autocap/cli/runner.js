const fs = require('fs');
const path = require('path');
const parseArgs = require('minimist');
const logger = require('../core/utils/logger')('cli/runner');

const currentPath = () => process.cwd();

/**
 * Command Loader
 *
 * @return a map of existing commands
 */
const loadCommands = () => {
  const commandMap = fs.readdirSync(path.join(__dirname, 'command'))
    .filter(fileName =>
      fileName.substring(0, fileName.indexOf('.')))
    .reduce((cmdMap, fileName) => {
      const commandName = fileName.substring(0, fileName.indexOf('.'));
      const commandModule = require(path.join(__dirname, 'command', fileName));

      cmdMap[commandName] = commandModule;
      return cmdMap;
    }, {});

  return commandMap;
};

/*
  Command Execute Wrapper
 */
function executeCommand (commandName) {
  const command = this.commands[commandName];
  if (!command) {
    logger.error(`Command [${commandName}] not found.`);
    return Promise.reject(new Error('command not found.'));
  }

  // execute
  const result = command.execute(this);

  // ensure a promise is wrapped
  if (!result || !Object.prototype.hasOwnProperty.call(result, 'then')) {
    return Promise.resolve(result);
  }
  return result;
}

/*
  Create a context object for running commands.So command can references
 */
function makeContext () {
  const context = {
    argv: process.argv.slice(2)
  };
  const args = parseArgs(context.argv, {});

  context.command = args._[0];
  context.args = args; // default parse options
  context.argv = process.argv.slice(2); // origin argv without then command name itself
  context.currentPath = currentPath();
  context.commands = loadCommands();

  return context;
}

// command executor
function runner (version) {
  const context = makeContext(version);
  const { command, commands } = context;
  context.executeCommand = executeCommand.bind(context);

  const commandName = command && commands[command] ? command : 'help';

  return context.executeCommand(commandName);
}

module.exports = runner;
