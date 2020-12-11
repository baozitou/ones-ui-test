const chalk = require('chalk');

const plain = (string) => string;

const levelColor = {
  error: plain,
  warn: plain,
  log: plain,
  info: plain,
  debug: plain,
  success: plain
};

const subjectColor = chalk.grey;

const levelTitleColor = {
  error: chalk.red,
  warn: chalk.yellow,
  log: chalk.white,
  info: chalk.white,
  debug: chalk.blue,
  success: chalk.green
};

function message (level, logSubject, string, ...args) {
  if (!Object.prototype.hasOwnProperty.call(levelColor, level)) {
    level = 'info';
  }

  const levelStr = levelTitleColor[level](`${level.toUpperCase()}`);
  const subjectStr = subjectColor(`[${logSubject}]`);

  console.log(levelStr + ' ' + subjectStr, string, ...args);
}

module.exports = (subject) => {
  return {
    error: message.bind(null, 'error', subject),
    warn: message.bind(null, 'warn', subject),
    log: message.bind(null, 'log', subject),
    info: message.bind(null, 'info', subject),
    debug: message.bind(null, 'debug', subject),
    success: message.bind(null, 'success', subject)

  };
};
