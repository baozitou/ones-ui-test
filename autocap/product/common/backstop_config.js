import * as BasicInfo from './basic_info';
import * as Viewports from './viewports';
import * as AppRouteUtils from './app_route_utils';

const Workspace = require('../../core/workspace');

// import * as RouteGenerator from './route_generator';

const logger = require('../../core/utils/logger')('product/common/backstop_config');

const getScenarioScriptPath = (productName) => `${productName}/index.js`;

export const createProductBackstopConfig = (options) => {
  const {
    name = 'project',
    baseUrl,
    branch = '',
    device = 'default', // 'default', 'desktop', 'mobile'
    viewport = 'default', // multiple, "default", "desktop,mobile", "small,wide,android",
    referenceUrl = '',
    referenceBranch = '',
    suites = []
    // readySelector = 'div.app-container'
  } = options;

  logger.debug('Generating scenarios with options: ',
    options
  );

  const workspace = Workspace.getWorkspace();
  const routeData = AppRouteUtils.getRouteData(options.routeData, options);
  const referenceRouteData = AppRouteUtils.getRouteData(
    options.referenceRouteData || options.routeData, options); // if referenceRouteData not defined, use routeData instead

  const viewports = Viewports.getViewports(device, viewport);

  // 读取产品的测试用例构造脚本，并生成用例列表（scenarios）
  const scenarios = suites.reduce((scenarioList, suiteName) => {
    const scenarioScript = getScenarioScriptPath(name);
    const generatorPath = workspace.getWorkspacePath(scenarioScript);

    let scenarios = [];
    let scenarioGenerator;
    try {
      scenarioGenerator = require(generatorPath);

      // use referenceUrl if one of the references is provided
      const referenceBaseUrl = referenceUrl || referenceBranch
        ? BasicInfo.getBaseUrl(referenceUrl || baseUrl, name, referenceBranch) : '';

      scenarios = scenarioGenerator({
        device,
        routeData,
        referenceRouteData,
        baseUrl: BasicInfo.getBaseUrl(baseUrl, name, branch),
        referenceBaseUrl
      });
    } catch (e) {
      logger.error(`Cannot load test scripts for product [${name}]`);
      throw e;
    }

    return [...scenarioList, ...scenarios];
  }, []);

  logger.info(`Generated ${scenarios.length} scenarios.`);

  return {
    id: BasicInfo.getConfigId(name, branch),
    viewports,
    scenarios
  };
};
