/**
 * 生成测试用例
 *
 * 根据Config里面的配置和样例数据，生成要跑的测试用例
 *
 */
const parseArgs = require('minimist');
const Workspace = require('../../core/workspace');
const FileUtils = require('../../core/utils/file');
const Validators = require('../../core/utils/validator');
const createProductBackstopConfig = require('../../product/common/backstop_config').createProductBackstopConfig;

const logger = require('../../core/utils/logger')('command/test');

// setup command usage
const usage = ({ scriptName, run }) => `
Command Usage:
$ ${run} ${scriptName} make [options]

Options:
  -c, --config          Autocap config file for generating testcases.
                        (Default: 'test/autocap/config.json')
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
function make (options) {
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

  // default script generator
  let generateScripts;
  try {
    generateScripts = workspace.getTestCaseScriptsByProduct(config.name);
  } catch (e) {
    logger.error(`Test scripts for product ${config.name} doesn't exist.`);
    throw e;
  }

  // generate scripts
  generateScripts(config);

  // rewrite backstop config
  const backstopConfigPath = workspace.getBackstopConfigPath();
  let backstopConfig = FileUtils.loadConfig(backstopConfigPath);
  const onesBackstopConfig = createProductBackstopConfig(config);

  backstopConfig = { ...backstopConfig, ...onesBackstopConfig };
  FileUtils.saveConfig(backstopConfigPath, backstopConfig);

  // // copy necessary script files to backstop folder
  // const engineScriptTemplatePath = workspace.getBackstopTemplatePath('engine_scripts');
  // const workspaceEngineScriptPath = workspace.getBackstopRuntimePath('engine_scripts');
  // fsExtra.copy(engineScriptTemplatePath, workspaceEngineScriptPath);
}

module.exports = {
  usage,
  execute: make
};
