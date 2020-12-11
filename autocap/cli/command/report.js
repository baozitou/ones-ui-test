/**
 * 查看/导出不同类型的报告
 *
 * 查看上一次生成的报告，或者导出报告数据。
 *
 */
const backstop = require('backstopjs');
const parseArgs = require('minimist');
const Workspace = require('../../core/workspace');
const logger = require('../../core/utils/logger')('command/test');

// command usage
const usage = ({ scriptName, run }) => `
Command Usage:
$ ${run} ${scriptName} report

Options:
  None
`;

const parseArgsOptions = {
  string: ['config'],
  alias: {
    config: 'c'
  },
  default: {
    config: 'test/autocap/config.json'
  }
};

/**
 * run test in workspace
 */
function report (context) {
  const {
    argv,
    currentPath
  } = context;

  const args = parseArgs(argv, parseArgsOptions);
  const workspace = Workspace.loadWorkspace({
    cwdPath: currentPath,
    configPath: args.config
  });

  const backstopAction = 'report';
  const backstopConfigPath = workspace.getBackstopConfigPath(currentPath);

  logger.info('Start test job type:', backstopAction);

  // execute backstop test
  backstop(backstopAction, {
    config: backstopConfigPath
  });
}

module.exports = {
  usage,
  execute: report
};
