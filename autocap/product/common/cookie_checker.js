const RequestUtils = require('../../core/utils/request');

export const CookiePath = {
  DEFAULT: 'backstop_data/engine_scripts/cookies.json', // empty cookies
  AUTH: 'backstop_data/engine_scripts/auth_cookies.json'
};

/**
 * 对于需要登录才能访问的页面，获取已登陆所需的cookie.
 * 这里做一个简单的检查，就是按前缀过滤掉那些不需要auth cookies的route path。
 *
 * @param  {[type]} routePath                  [description]
 * @param  {Array}  [authPrefixList=['/auth']] [description]
 * @return {[type]}                            [description]
 */
export const createAuthCookieChecker = (authPrefixList = ['/auth']) => (routePath) => {
  if (!authPrefixList.some(prefix => routePath.indexOf(prefix) >= 0)) {
    return CookiePath.AUTH;
  }

  return CookiePath.DEFAULT;
};

/**
 * 获取ONES账号的登录cookies并设到工作区的auth cookies文件里。可用于每次测试开始之前刷新token。
 *
 * @param  {[type]} username [description]
 * @param  {[type]} password [description]
 * @return {[type]}          [description]
 */
export const requestONESAuthCookies = (username, password) => {
  console.log('not implemented');
};


/**
 * 校验当前的cookie里是否已经包含了可用的验证信息，如果是ok的话，则不需要重新请求auth cookies了
 */
export const verifyONESAuthCookies = () => {
  console.log('not implemented');
}
