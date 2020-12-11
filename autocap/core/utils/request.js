const axios = require('axios');
const cookie = require('cookie');

const logger = require('./logger')('core/utils/request');

// Axios default options
const defaultOptions = {
  method: 'get',
  dataType: 'json'
};

// base request
const baseRequest = (options) => {
  const finalOptions = { ...defaultOptions, ...options };
  logger.info(`[request] ${finalOptions.method} ${finalOptions.url}`);
  return axios.request(finalOptions);
};

// exporting different request methods
const request = baseRequest;

const parseCookie = cookie.parse;

module.exports = {
  request,
  parseCookie
};
