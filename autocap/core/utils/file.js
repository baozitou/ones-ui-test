const fs = require('fs');

const loadConfig = (configPath) => {
  const configString = fs.readFileSync(configPath);
  return JSON.parse(configString);
};

const saveConfig = (configPath, config) => {
  const configString = JSON.stringify(config, null, '  ');
  fs.writeFileSync(configPath, configString);
};

const createDir = (dirPath) => {
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath);
  }
};

const exists = (path) => {
  return fs.existsSync(path);
};

module.exports = {
  loadConfig,
  saveConfig,
  createDir,
  exists
};
