/**
 * 执行Test
 *
 * 指定要跑的product，会打印出此次测试的相关配置信息，并执行测试过程。
 *
 * 打印配置信息可以通过onBeforeScript来实现？不一定，要看运行环境是node还是浏览器
 *
 */
const backstop = require('backstopjs');
const parseArgs = require('minimist');
const Workspace = require('../../core/workspace');
const logger = require('../../core/utils/logger')('command/test');

// command usage
const usage = ({ scriptName, run }) => `
Command Usage:
$ ${run} ${scriptName} test

Options:
  -c, --config          Specify a AutoCap test config file, instead of the
                        default location
  -R, --reference       Run reference testcases and save reference images
                        (equals to 'backstop reference'). If without this
                        parameter, run the normal testcases instead.

`;

const parseArgsOptions = {
  bool: ['reference'],
  string: ['config'],
  alias: {
    reference: 'R',
    config: 'c'
  },
  default: {
    config: 'test/autocap/config.json'
  }
};

/**
 * run test in workspace
 */
function test (options) {
  const {
    argv,
    currentPath
  } = options;

  const args = parseArgs(argv, parseArgsOptions);
  const workspace = Workspace.loadWorkspace({
    cwdPath: currentPath,
    configPath: args.config
  });
  const backstopAction = args.reference ? 'reference' : 'test';
  const backstopConfigPath = workspace.loadWorkspace(currentPath);

  logger.info('Start test job type:', backstopAction);

  // execute backstop test
  backstop(backstopAction, {
    config: backstopConfigPath
  });
}

module.exports = {
  usage,
  execute: test
};
