const urlJoin = require('url-join');

// 生成backstop config的id
export const getConfigId = (name, branch) => {
  return branch ? `${name}_${branch}` : name;
};

// 生成backstop config的baseUrl
export const getBaseUrl = (baseUrl, name, branch) => {
  const productUrl = urlJoin(baseUrl, name);
  return branch ? urlJoin(productUrl, branch) : productUrl;
};
