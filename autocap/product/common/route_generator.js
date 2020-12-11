const path = require('path');
const isEqual = require('lodash').isEqual;
const logger = require('../../core/utils/logger')('product/common/route_generator');

const nameDataRegex = /:(\w+)\??/;

const stringMatch = (str, stringOrRegex) => {
  if (stringOrRegex instanceof RegExp) {
    return stringOrRegex.test(str);
  }
  return str === stringOrRegex;
};

const createFullUrl = (baseUrl, url) => {
  return path.posix.join(baseUrl, `/#${url}`);
};

class RouteFiller {
  constructor (name, routeData) {
    this.name = name;
    this.routeData = routeData;
    this.missingRouteData = {};
  }

  getUrlFromRoute (route) {
    let url = route;
    let match = url.match(nameDataRegex);
    while (match) {
      const dataName = match[1];
      const dataValue = this.routeData[dataName];

      // check data by name
      if (dataValue == null) {
        logger.error(`cannot find value for url parameter: ${dataName}`);
        this.missingRouteData[dataName] = '';
      }

      // replace parameter with dataValue
      url = url.replace(new RegExp(match[0], 'g'), dataValue);

      // repeat parameter search after replacement
      match = url.match(nameDataRegex);
    }
    return url;
  };

  logMissingRouteData () {
    if (Object.keys(this.missingRouteData).length > 0) {
      logger.info(`Please add below fields to ${this.name} in your config file:\n`,
        JSON.stringify({
          routeData: this.missingRouteData
        }, null, '  '));
    }
  }
}

/* Route Geneerator所需要到一些helper方法，也可以用来自己构造scenario。 */

// 创建一条scnario的记录，并且有默认参数设置。
export const createScenario = (label, url, options = {}) => {
  return {
    label,
    url,
    readySelector: 'div[data-reactroot]',
    hideSelectors: ['.loading', '.app-loading'],
    delay: 10000,
    ...options
  };
};

// 把 RouteConstants 里面的routes按前缀列表过滤。当route是以prefixList里面任意一个前缀打
// 头的时候，就会被加到最终的列表里，其余不符合prefixList的被过滤掉。
export const filterRouteWithAllowPrefix = (routeConstants, prefixList) => {
  const filteredRoutes = {};
  Object.keys(routeConstants)
    .forEach(routeName => {
      const route = routeConstants[routeName];
      if (route && prefixList.some(prefix => route.indexOf(prefix) === 0)) {
        filteredRoutes[routeName] = route;
      }
    });

  return filteredRoutes;
};

/* Route Generator 主方法，固定的构造scenario流程 */
/**
 * 根据传入预定义数据（Route Data），以及RouteConstants生成对应的
 * @param  {[type]} routeData      [description]
 * @param  {[type]} routeConstants [description]
 * @return {[type]}                [description]
 */
export const generateScenarios = (routeConstants, options) => {
  const {
    baseUrl = '',
    referenceBaseUrl = '',
    routeData = {},
    referenceRouteData = {},
    ignoredList = [],
    getCookiePath,
    baseScenarioOptions = {}
  } = options;

  const scenarios = [];
  const routeFiller = new RouteFiller('routeData', routeData);
  const referenceRouteFiller = new RouteFiller('referenceRouteData', referenceRouteData);
  Object.keys(routeConstants)
    .forEach((routeName, idx) => {
      const route = routeConstants[routeName];
      const routeLogStr = `[${idx}:${routeName}] ${route}`; // for logger

      // skip route if it is in the ignored list
      for (const ignoreUrl of ignoredList) {
        if (stringMatch(route, ignoreUrl)) {
          return;
        }
      }

      // try adding scenario by route
      try {
        const url = routeFiller.getUrlFromRoute(route);

        // add scenario to the list
        const scenarioOptions = { ...baseScenarioOptions };
        if (getCookiePath) { scenarioOptions.cookiePath = getCookiePath(url); };
        if (referenceBaseUrl) {
          const referenceUrl = referenceRouteFiller.getUrlFromRoute(route);
          scenarioOptions.referenceUrl = createFullUrl(referenceBaseUrl, referenceUrl);
        }
        scenarios.push(
          createScenario(
            routeName,
            createFullUrl(baseUrl, url),
            scenarioOptions
          ));
      } catch (e) {
        const errMsg = `${routeLogStr} - error: ${e.stack ? e.stack : e.message}`;
        throw new Error(errMsg);
      }
    });

  // output useful route data missing information
  routeFiller.logMissingRouteData();
  if (referenceBaseUrl && !isEqual(routeData, referenceRouteData)) {
    referenceRouteFiller.logMissingRouteData();
  }

  return scenarios;
};
