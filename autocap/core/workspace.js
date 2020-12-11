const fs = require('fs');
const path = require('path');
const FileUtils = require('./utils/file');
const logger = require('./utils/logger')('core/workspace');

/*
  Workspace的Config，跟Backstop的Config文件作用不一样。

  Workspace的主要是用来记录目前测试项目的一些配置，最终会用来生成backstop的配置。

  Backstop的配置则是按照BackstopJS的要求，把所有要跑的用例写在里面，最终通过执行BackstopJS
  的任务来运行测试。
 */

const WORKSPACE_BASE_PATH = 'test/autocap';

let workspace = null; // global instance

/**
 * Workspace类主要用来管理当前工作区里面的配置信息。
 *
 * 在Workspace下面主要有积累配置信息
 *
 */

class Workspace {
  constructor ({ cwdPath, configPath }) {
    this.basePath = path.join(cwdPath, WORKSPACE_BASE_PATH);
    this.configPath = configPath || this.getDefaultConfigPath(); // use custom config path maybe
    this.config = {};
  }

  // workspace config
  getWorkspacePath (subPath = '.') {
    return path.join(this.basePath, subPath);
  }

  getDefaultConfigPath () {
    return this.getWorkspacePath('config.json');
  }

  loadConfig () { // workspace config
    if (FileUtils.exists(this.configPath)) {
      try {
        this.config = FileUtils.loadConfig(this.configPath);
      } catch (e) {
        logger.error('Cannot load config file:', this.configPath);
        throw e;
      }
    }
    return this.config;
  }

  saveConfig (checkExist) {
    if (checkExist && FileUtils.exists(this.configPath)) {
      throw new Error(`The config file already exists at: ${this.configPath}. Will not overwrite it.`);
    }
    return FileUtils.saveConfig(this.configPath, this.config);
  }

  // get backstop config path
  getBackstopConfigPath () {
    return this.getBackstopRuntimePath('backstop_config.json');
  }

  // get custom test case scripts
  getProductPath (product) {
    return path.join(this.basePath, product.toLowerCase());
  }

  getTestCaseScriptsByProduct (product) {
    const productPath = this.getProductPath(product);
    return require(productPath);
  }

  // get backstop data
  getBackstopRuntimePath (subPath = '.') {
    // 由于backstop内部就是使用process.cwd()来获取projectPath的，所以这里与backstop保持一致
    return path.join(process.cwd(), 'backstop_data', subPath);
  }

  getBackstopTemplatePath (subPath = '.') {
    return path.resolve(__dirname, `../product/backstop/${subPath}`);
  }

  // a wrapper to run backstop command, because need to change cwd
  runAsync (scriptFunc) {
    return new Promise((resolve, reject) => {
      resolve(scriptFunc());
    });
  }
}

/**
 * Initialized a workspace instance using constructor options
 *
 * @param  {[type]} options pass directly to class Workspace
 * @return {[type]}         [description]
 */
const loadWorkspace = (options) => {
  if (workspace) {
    throw new Error('Workspace should not be initialized twice!');
  }
  workspace = new Workspace(options);
  return workspace;
};

const getWorkspace = () => {
  if (!workspace) {
    throw new Error('Workspace has not yet initialized.');
  }
  return workspace;
};

module.exports = {
  loadWorkspace,
  getWorkspace
};
