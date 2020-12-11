# coding=utf-8
from framework.base_page import BasePage
from config import settings

class OnesDemoLoginElement(object):
    demo_login_form_head = 'xpath=>//*[@id="demo-login-main"]/div/div[2]/div[1]'#登陆表单的标题，用来确认进入了登陆页面
    mobile_phone = 'xpath=>//*[@id="demo-login-main"]/div/div[2]/div[2]/div[2]/input'#手机号输入框
    verification_code = 'xpath=>//*[@id="demo-login-main"]/div/div[2]/div[2]/div[5]/input'#验证码输入框
    verifi_button = 'xpath=>//*[@id="demo-login-main"]/div/div[2]/div[2]/div[3]'#发送验证码按钮
    demo_button = 'xpath=>//*[@id="demo-login-main"]/div/div[2]/div[2]/div[6]/span[2]'#「进入demo」按钮


class OnesDemoLoginPage(BasePage):
    config = settings.GetConfig().getconfig()
    def __init__(self, driver):
        super(OnesDemoLoginPage,self).__init__(driver)
        element = OnesDemoLoginElement()
        self._element = element

    def input_mobile_phone(self):
        self.click(self._element.mobile_phone)
        self.type(self._element.mobile_phone, self.config.get('demoAccount','mobile_phone'))

    def input_verification_code(self):
        self.click(self._element.verification_code)
        self.type(self._element.verification_code, self.config.get('demoAccount','verification_code'))
    
    def click_verifi_button(self):
        self.click(self._element.verifi_button)
    
    def click_demo_button(self):
        self.click(self._element.demo_button)
    
    def demo_login_form_head_text(self):
        return self.text(self._element.demo_login_form_head)