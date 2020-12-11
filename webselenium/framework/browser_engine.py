# -*- coding:utf-8 -*-

from os import path
from selenium import webdriver
from utils.logger import Logger
import time
from config import settings


config = settings.GetConfig()


logger = Logger(logger=__name__).getlog()

class BrowserEngine(object):

    chrome_driver_path = path.join(settings.ROOT_PATH, '../tools/drivers/chromedriver')
    ie_driver_path = path.join(settings.ROOT_PATH, '../tools/drivesr/IEDriverServer')
    firefox_driver_path = path.join(settings.ROOT_PATH,'../tools/drivesr/firefox')

    def __init__(self, driver):
        self.driver = driver
        self.file_name = config.getconfig().get("FileName", "file_name")
        self.file_path = settings.ROOT_PATH
        self.cookies_file = path.join(self.file_path, self.file_name)

    def open_browser(self, url=False):

        browser = config.getconfig().get("browserType", "browserName")

        logger.info("You had select %s browser." % browser)
        if not url:
            url = config.getconfig().get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "Firefox":
            self.driver = webdriver.Firefox(self.firefox_driver_path)
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            self.driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            self.driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")
        else:
            raise RuntimeError('Unknown browser driver: {}'.format(browser))
        self.driver.get(url)
        open_browser_time = int(time.time())
        # 判断是否需要二维码校验
        self.execute_fun(self.driver,open_browser_time,url)
        logger.info("Open url: %s" % url)
        self.driver.maximize_window()
        logger.info("Maximize the current window.")
        self.driver.set_window_size(1280, 768)
        logger.info("current window is :1280 x 768")
        self.driver.implicitly_wait(5)
        logger.info("Set implicitly wait 10 seconds.")

        return self.driver

    # 方法一：
    # 终端下，执行以下命令，端口号自定义
    # win:chrome.exe --remote-debugging-port=9222
    # mac:/Applications/Google\Chrome.app/Contents/MacOS/Google\Chrome-remote-debugging-port=9222
    # driver = webdriver.Chrome()
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.debugger_address = "127.0.0.1:9222"
    # driver = webdriver.Chrome(options=chrome_options)
    # driver.get('https://dev.myones.net/project/master/#/workspace/home')
    # driver.implicitly_wait(3)

    # 方法二：使用cookies自动进行登陆
    def get_driver_cookies(self, driver, url, open_browser_time):
        '''
        扫码登录时的相关操作，获取或更新driver的cookies值，并写入到相关文件中
        :param driver: webdriver实例
        :param open_browser_time: 第一次打开浏览器的开始时间
        :return:
        '''
        while True:
            now_waiting_time = int(time.time())
            update_cookies = driver.get_cookies()
            if len(update_cookies) >= 5:
                config.operating_yaml_file("w+",self.file_path, self.file_name, write_file_content=update_cookies)
                self.update_driver_cookies(driver,url,update_cookies)
                break
            elif (now_waiting_time - open_browser_time) % 115 == 0:
                driver.get(url)
            elif now_waiting_time - open_browser_time >= 600:
                driver.close()
                break

    def update_driver_cookies(self, driver, url, update_cookies_list):
        """
        更新当前浏览器cookies
        :param dirver: webdriver实例
        :param update_cookies_list: 需要更新的cookies实际值
        """
        for cookie in update_cookies_list:
            driver.add_cookie({'domain': cookie.get("domain"),
                                    'expiry': cookie.get("expiry"),
                                    'httpOnly': cookie.get("httpOnly"),
                                    'name': cookie.get("name"),
                                    'path': cookie.get("path"),
                                    'secure': cookie.get("secure"),
                                    'value': cookie.get("value")})
        driver.get(url)

    def execute_fun(self,driver, open_browser_time, url):
        if "dev" in url:
            if path.exists(self.cookies_file):
                yaml_cookies = config.operating_yaml_file("r",self.file_path,self.file_name)
                if len(yaml_cookies) >= 5:
                    oauth_expires_time = int("".join([cookie.get("value") for cookie in yaml_cookies
                                                      if cookie["name"] == "OauthExpires"]))
                    if open_browser_time >= oauth_expires_time:
                        logger.info("Cookies have expired. Please scan the code again")
                        self.get_driver_cookies(driver, url, open_browser_time)
                    else:
                        logger.info("Cookies auto jump")
                        self.update_driver_cookies(driver,url,yaml_cookies)
            else:
                logger.info("Please scan the QR code and create cookies")
                self.get_driver_cookies(driver, url, open_browser_time)
        else:
            driver.get(url)

    def quit_browser(self):
        self.driver.quit()
        logger.info("Now, Close and quit the browser.")
