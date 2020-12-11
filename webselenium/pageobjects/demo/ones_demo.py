# coding=utf-8
from framework.base_page import BasePage
from config import settings

class OnesDemoElement(object):
    progress_manage = 'xpath=>//*[@id="demo"]/div[1]/div[2]/div[2]/div[2]/span[2]'#通用项目管理
    agile_dev_manage = 'xpath=>//*[@id="demo"]/div[1]/div[3]/div[2]/div[2]/span[2]'#敏捷研发管理
    devops = 'xpath=>//*[@id="demo"]/div[1]/div[4]/div[2]/div[2]/span[2]'#DevOps 持续交付
    pmo = 'xpath=>//*[@id="demo"]/div[2]/div[2]/div[2]/div[2]/span[2]'#PMO办公室/管理者
    product_team = 'xpath=>//*[@id="demo"]/div[2]/div[3]/div[2]/div[2]/span[2]'#产品团队
    dev_team = 'xpath=>//*[@id="demo"]/div[2]/div[4]/div[2]/div[2]/span[2]'#研发团队
    test_team = 'xpath=>//*[@id="demo"]/div[2]/div[5]/div[2]/div[2]/span[2]'#测试团队
    ops_team = 'xpath=>//*[@id="demo"]/div[2]/div[6]/div[2]/div[2]/span[2]'#运维团队


class OnesDemoPage(BasePage):
    def __init__(self, driver):
        super(OnesDemoPage, self).__init__(driver)
        element = OnesDemoElement()
        self._element = element

#多种研发场景Demo
    def click_progress_manage(self):
        #通用项目管理
        self.click(self._element.progress_manage)
    
    def click_agile_dev_manage(self):
        #敏捷研发管理
        self.click(self._element.agile_dev_manage)

    def click_devops(self):
        #DevOps 持续交付
        self.click(self._element.devops)

#多种团队 Demo
    def click_pmo(self):
        #PMO办公室/管理者
        self.click(self._element.pmo)

    def click_product_team(self):
        #产品团队
        self.click(self._element.product_team)
    
    def click_dev_team(self):
        #研发团队
        self.click(self._element.dev_team)
    
    def click_test_team(self):
        #测试团队
        self.click(self._element.test_team)
    
    def click_ops_team(self):
        #运维团队
        self.click(self._element.ops_team)
