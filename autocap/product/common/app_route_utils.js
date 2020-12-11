const FileUtils = require('../../core/utils/file');
const Workspace = require('../../core/workspace');

/**
 * 获取一个用来生成route url的数据参数集。
 *
 * @param  {[type]} device 要测试的是desktop还是mobile还是全部
 *                        "both", "desktop", "mobile"
 * @param  {[type]} name   产品的名字
 */
export const getRouteData = (routeData, options) => {
  // 以后可能是用外部数据源，所以接口先写在这。
  const workspace = Workspace.getWorkspace();

  if (typeof routeData === 'string') { // need to load
    const appDataFile = workspace.getWorkspacePath(routeData);
    if (routeData.match(/.js$/)) {
      return require(appDataFile)(options);
    } else if (routeData.match(/.json$/)) {
      return FileUtils.loadConfig(appDataFile);
    }
  } else if (typeof routeData === 'object') {
    return routeData;
  }

  // example
  return {};
};

/**
 * 根据device选择所需要的routes
 *
 * @param  {[type]} device        "desktop", "mobile", "both" = "desktop" + "mobile"
 * @param  {[type]} desktopRoutes
 * @param  {[type]} mobileRoutes
 * @return {[type]}
 */
export const getAppRoutes = (device, desktopRoutes, mobileRoutes) => {
  let appRoutes = {};

  if (device === 'both' || device === 'desktop') {
    appRoutes = { ...appRoutes, ...desktopRoutes };
  }
  if (device === 'both' || device === 'mobile') {
    appRoutes = { ...appRoutes, ...mobileRoutes };
  }

  return appRoutes;
};
