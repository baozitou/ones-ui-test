import os
import configparser
import yaml
#安装pip3 install ruamel.yaml
from ruamel import yaml

# 项目运行的根路径

ROOT_PATH =  os.path.dirname(os.path.abspath(__file__))
# 项目相关路径
CONFIG_PATH = os.path.join(ROOT_PATH, 'config.ini')
REPORT_PATH = os.path.join(ROOT_PATH, '../test_reports') # 测试报告路径
CASE_PATH = os.path.join(ROOT_PATH, '../testsuites') # 测试用例路径
LOG_PATH = os.path.join(ROOT_PATH, '../logs/') # 日志路径
SCREENSHOT_PATH = os.path.join(ROOT_PATH, '../screenshots/') # 截屏路径

class GetConfig:

    def operating_yaml_file(self, mode, file_path, file_name, write_file_content=None):
        """
        读取或写入yaml文件
        :param mode: 使用模式（目前只提供两种“r”或“w+”）
        :param file_name: 读取或写入的文件名称
        :param write_file: 写入的内容
        :return: read_yaml_data具体内容
        """
        cookies_file_path = os.path.join(file_path,file_name)
        if mode == "w+":
            with open(cookies_file_path, mode, encoding="UTF-8") as wf:
                yaml.dump(write_file_content, wf, Dumper=yaml.RoundTripDumper)
        elif mode == "r":
            with open(cookies_file_path, mode, encoding="UTF-8") as rf:
                read_file = rf.read()
                read_yaml_data = yaml.load(read_file, Loader=yaml.Loader)

            return read_yaml_data

    def getconfig(self):
        '''
        获取config.ini文件对象，此文件存全局变量内容
        :return:config对象
        '''
        config = configparser.ConfigParser()
        config.read(CONFIG_PATH, encoding='UTF-8')
        return config

# config = getConfig()