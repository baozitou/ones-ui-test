# coding=utf-8
import time
import os.path
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from framework.utils import local_expected_conditions, formart_selector
from utils.logger import Logger
from config import settings

# create a logger instance
logger = Logger(logger=__name__).getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 关闭浏览器，结束测试
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")


    # 浏览器刷新操作
    def refresh(self):
        self.driver.refresh()
        logger.info("Refreshes the current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    # 保存图片
    def get_windows_img(self):
        """
         在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹screenshots下
        """
        file_path = settings.SCREENSHOT_PATH
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info(
                "Had take screenshot and save to folder : {}".format(settings.SCREENSHOT_PATH))
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    
    #定位复数元素（一批相同元素）
    def find_elements(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: elements 列表
        login_lnk = "xpath => //*[@id='u1']/a[7]
        """
        if '=>' not in selector:
            return logger.info("Please add '=>' symbol")
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]
        if selector_by == "x" or selector_by == 'xpath':
            try:
                elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, selector_value)))
                logger.info("Had find the elements \' %s \' successful by %s via value: %s " % (elements,selector_by, selector_value))
                return elements
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'css':
            try:
                elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, selector_value)))
                logger.info("Had find the elements \' %s \' successful "
                            "by %s via value: %s " % (elements, selector_by, selector_value))
                return elements
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()

    #找到元素才点击
    def found_element_click(self,selector):
        # if '=>' not in selector:
        #     return  logger.info("Lack {}".format("=>"))
        # selector_by = selector.split('=>')[0]
        # selector_value = selector.split('=>')[1]
        # if selector_by == "i"
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
                                            '//*[@id="login"]/div[1]/div[1]/input')))
        logger.info(element)
        # if element:
        #     self.find_element(selector)
        # else:
        #     logger.info("Element is None<{}>".format(element))

    def find_element(self, selector, ec_func="presence_of_element_located", time_out = 10):
        """定位元素方法

        Args:
            selector (str): 定位元素的字符串
            ec_func（str）:预先设定的条件的方法名称
        Returns:
            result: 默认方法是定位到的单个元素，其余的方法则看具体返回什么
        """
        selector_by, selector_value = formart_selector(selector)
        try:
            result = WebDriverWait(self.driver, time_out).until(local_expected_conditions(ec_func=ec_func)((selector_by, selector_value)))
            if result:
                logger.info("The result is success. by %s , value: %s " % (selector_by, selector_value))
            else:
                logger.info("The result is false. by %s , value: %s " % (selector_by, selector_value))
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)
            self.get_windows_img()
        return result

    # 输入
    def type(self, selector, text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # 移动鼠标到元素上
    def move_to_element(self, selector):
        el = self.find_element(selector)
        eltext = el.text
        actions = ActionChains(self.driver)
        try:
            actions.move_to_element(el)
            logger.info("Has moved to element :{}".format(eltext))
        except NameError as e:
            logger.error("Faild to move to element with {}".format(e))
            self.get_windows_img()

    # 滚动到元素可见
    def scroll_into_view(self, selector):
        el = self.find_element(selector)
        eltext = el.text
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", el)
            logger.info("Had scroll into element with {}".format(eltext))
        except NameError as e:
            logger.error("Faild to scroll to element with {}".format(e))
            self.get_windows_img()

    def get_attribute_elements(self,selector,key):
        '''
        获取所以元素的属性名称
        :return:
        '''
        els = self.find_elements(selector)
        values =[]
        try:
            for el in els:
                value = el.get_attribute(key)
                values.append(value)
                logger.info('element has atrribute key:{} value:{}'.format(key, value))
            return values
        except NameError as e:
            logger.error("element has no attribute key:{}, error with {}".format(key, e))
            self.get_windows_img()


    def get_attribute(self, selector, key):
        '''
        获取元素的属性值
        '''
        el = self.find_element(selector)
        try:
            value = el.get_attribute(key)
            logger.info('element has atrribute key:{} value:{}'.format(key, value))
            return value
        except NameError as e:
            logger.error("element has no attribute key:{}, error with {}".format(key, e))
            self.get_windows_img()

    def get_attribute_element(self, selector, key):
        '''
        获取元素的属性值
        '''
        try:
            value = selector.get_attribute(key)
            logger.info('element has atrribute key:{} value:{}'.format(key, value))
            return value
        except NameError as e:
            logger.error("element has no attribute key:{}, error with {}".format(key, e))
            self.get_windows_img()

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            eltext = el.text
            ActionChains(self.driver).move_to_element(el).click().perform()
            logger.info("The element \' %s \' was clicked." % eltext)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)


    # 获取元素的文本
    def text(self, selector):
        el = self.find_element(selector)
        try:
            eltext = el.text
            logger.info("The element text is : %s" % eltext)
            return eltext
        except NameError as e:
            logger.error("Failed to get the element text with %s" % e)

    def get_text(self, selector):
        try:
            eltext = selector.text
            logger.info("The element text is : %s" % eltext)
            return eltext
        except NameError as e:
            logger.error("Failed to get the element text with %s" % e)

    # 点击元素
    def get_click(self, selector):
        try:
            eltext = selector.text
            ActionChains(self.driver).move_to_element(selector).click().perform()
            logger.info("The element \' %s \' was clicked." % eltext)
            return eltext
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    # 获取所有元素文本返回列表
    def get_elements_text(self, selector):
        els = self.find_elements(selector)
        els_text = []
        try:
            for el in els:
                els_text.append(el.text)
            logger.info("The element text is : %s" % els_text)
            return els_text
        except NameError as e:
            logger.error("Failed to get the element text with %s" % e)

    # 获得网页标题
    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # 切换frame、iframe相关

    def switch_to_frame(self, frame):
        '''
        frame:frame的id或者name
        '''
        self.driver.switch_to.frame(frame)
        logger.info("Had switch to frame:{}".format(frame))

    def switch_to_default_content(self):
        '''
        切换到默认的frame
        '''
        self.driver.switch_to.default_content()
        logger.info("Had switch to default content!")

    def switch_to_parent_frame(self):
        '''
        切换到上一层的frame
        '''
        self.driver.switch_to.parent_frame()
        logger.info("Had switch to parent frame")


    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
