
const SCRIPT_NAME = 'autocap';
const BIN_CMD = 'yarn run'; // you can also use 'npx'

const helpCommandUsage = ({ scriptName, run }) => `
Usage: ${run} ${scriptName} [command] [command options]

Commands:
  - init              initialize a config file (test/autocap/config.json)
                      and copy the backstop files to the workspace
  - make              generate testcases according a config file
  - prepare           prepare test data, cookies, etc.
  - tests             execute tests
  - report            open previous report
  - help              display this help.
                      You can also use 'help [command]' to see each command's
                      options with more details
`;

/**
 * Help Command functions
 */
function help (context) {
  const { args, commands } = context;

  let helpCommand = 'help';
  const params = args._;

  if (params.length > 1 &&
    Object.prototype.hasOwnProperty.call(commands, params[1])) {
    helpCommand = params[1];
  }

  console.log(commands[helpCommand].usage({
    scriptName: SCRIPT_NAME,
    run: BIN_CMD
  }));
}

module.exports = {
  usage: helpCommandUsage,
  execute: help
};
