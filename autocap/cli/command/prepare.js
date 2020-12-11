/**
 * 准备数据
 *
 * 准备测试所需要的数据，保存到相应的config里面。
 *
 */
// const backstop = require('backstopjs');
const parseArgs = require('minimist');
const path = require('path');
const Workspace = require('../../core/workspace');
const FileUtils = require('../../core/utils/file');
const Validators = require('../../core/utils/validator');
const logger = require('../../core/utils/logger')('command/test');

// setup command usage
const usage = ({ scriptName, run }) => `
Command Usage:
$ ${run} ${scriptName} prepare

Options:
  -c, --config                Specify a config file for preparing data
  -R, --reference             prepare data for reference test
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
function prepare (options) {
  const {
    argv,
    currentPath
  } = options;

  const args = parseArgs(argv, parseArgsOptions);
  const workspace = Workspace.loadWorkspace({
    cwdPath: currentPath,
    configPath: args.config
  });
  const config = workspace.loadConfig();

  Validators.ensure(config.name, `Config file is missing or incorrect: ${workspace.configPath}`);

  const productPath = workspace.getProductPath(config.name);
  const preparePath = path.join(productPath, 'prepare');
  if (!FileUtils.exists(preparePath)) {
    logger.info('No prepare script found for this config. Skip data preparation.');
    return;
  }

  let prepareScript = () => {};
  try {
    prepareScript = require(preparePath);
  } catch (e) {
    logger.error('Prepare script is invalid:', preparePath, e.stack);
  }

  logger.info('Preparing data for current test...');

  return workspace.runAsync(() => {
    return prepareScript({
      ...config,
      isReference: !!args.reference,
      workspace
    });
  })
    .then(() => {
      logger.info('Prepare data done.');
    })
    .catch((e) => {
      logger.error('Prepare data failed:', e);
    });
}

module.exports = {
  usage,
  execute: prepare
};
