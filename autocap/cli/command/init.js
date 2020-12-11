// const fs = require('fs');
const fsExtra = require('fs-extra');
const backstop = require('backstopjs');
// const path = require('path');

const parseArgs = require('minimist');
const Workspace = require('../../core/workspace');
const FileUtils = require('../../core/utils/file');
const Validators = require('../../core/utils/validator');
const createProductBackstopConfig = require('../../product/common/backstop_config').createProductBackstopConfig;
const logger = require('../../core/utils/logger')('command/init');

// init command usage
const usage = ({ scriptName, run }) => `
Command Usage:
$ ${run} ${scriptName} init [productName] [options]...

Initialize the workspace settings and backstop files for a new project.

Options:
  -U, --baseUrl [url]         Setting project's base URL, default to "https://dev.ones.ai/"

  -B, --branch <branch_name>  Setting a testing branch (if it's in development environment)

  -D, --device <device>       Test routes for device type: "both", "desktop", "mobile".
                              Default is "both" (= "desktop" and "mobile").

  -V, --viewport <viewport>   Test for different viewport types(support multiple, comma separated):
                              "default" (= "desktop"),
                              "desktop,mobile",
                              "small,wide,android"

  -R, --referenceUrl [url]    Setting a reference comparing base URL for cross environment comparison

  -N, --referenceBranch       Setting a reference comparing branch for cross environment comparison.
                              If "--referenceUrl" option is not set, then "--baseUrl" is used as the
                              reference URL instead.

  -c, --config                Specify a config file to load options
`;

const parseArgsOptions = {
  string: ['baseUrl', 'device', 'config'],
  boolean: ['dev', 'saveConfig'],
  alias: {
    baseUrl: 'U',
    branch: 'B',
    device: 'D',
    referenceBranch: 'N',
    referenceUrl: 'R',
    config: 'c',
    createConfig: 'C'
  },
  default: {
    config: 'test/autocap/config.json'
  }
};

const initWorkspaceConfig = (cwdPath, args) => {
  // 初始化workspace
  const workspace = Workspace.loadWorkspace({
    cwdPath,
    configPath: args.config
  });
  const shouldCreateConfig = !FileUtils.exists(args.config);

  // fields from args
  const productName = args._[1];
  const useReference = !!(args.referenceUrl || args.referenceBranch);
  const {
    baseUrl, branch, device, viewport, referenceUrl, referenceBranch
  } = args;

  if (shouldCreateConfig) {
    // 创建config文件

    Object.assign(workspace.config, {
      name: productName,
      baseUrl: baseUrl || 'https://dev.myones.net/',
      branch: branch || '',
      device: device || 'both',
      viewport: viewport || 'default',
      referenceUrl: useReference ? (referenceUrl || baseUrl) : undefined,
      referenceBranch: referenceBranch || '',
      routeData: {} // default routeData,
    });
  } else {
    workspace.loadConfig();
    const updatedOptions = {
      name: productName,
      baseUrl,
      branch,
      device,
      viewport,
      referenceUrl: useReference ? (referenceUrl || baseUrl) : '', // use null instead of undefined to enable overwrite
      referenceBranch
    };
    // merge new values to config
    Object.keys(updatedOptions).forEach(field => {
      if (updatedOptions[field] !== undefined) {
        workspace.config[field] = updatedOptions[field];
      }
    });
  }

  // 校验config参数
  const config = workspace.config;
  Validators.ensure(config.name, 'please specify a "name" for the testing product');
  Validators.ensure(config.baseUrl, 'please specify a "baseUrl" for the product');

  // 设置要测试的suite（未来这里可以测试多个产品）
  config.suites = [productName];

  // 保存到config之前需检查，如果文件已存在则跳过。
  workspace.saveConfig(true);

  logger.info(`${shouldCreateConfig ? 'Created' : 'Updated'} config file at:`, workspace.configPath);

  return workspace.config;
};

/**
 * init project workspace to run test later
 */
function init (context) {
  const {
    argv,
    currentPath
  } = context;

  // reparse arguments
  const args = parseArgs(argv, parseArgsOptions);

  try {
    initWorkspaceConfig(currentPath, args);
  } catch (e) {
    if (e instanceof Validators.ValidationError) {
      logger.error(e.message);
    } else {
      logger.error(e.stack);
    }
    return;
  }

  // backstop init
  const workspace = Workspace.getWorkspace();
  const config = workspace.config;
  const backstopConfigPath = workspace.getBackstopConfigPath();
  const onesBackstopConfig = createProductBackstopConfig(config); // blank backstop config

  workspace.run(() => {
    backstop('init', {
      config: backstopConfigPath
    }).then(() => {
      // rewrite backstop config
      let backstopConfig = FileUtils.loadConfig(backstopConfigPath);
      backstopConfig = { ...backstopConfig, ...onesBackstopConfig };
      FileUtils.saveConfig(backstopConfigPath, backstopConfig);

      // copy necessary script files to backstop folder
      const engineScriptTemplatePath = workspace.getBackstopTemplatePath('engine_scripts');
      const workspaceEngineScriptPath = workspace.getBackstopRuntimePath('engine_scripts');
      fsExtra.copy(engineScriptTemplatePath, workspaceEngineScriptPath);
    })
      .catch((err) => {
        logger.error(err);
      });
  });
}

module.exports = {
  usage,
  execute: init
};
