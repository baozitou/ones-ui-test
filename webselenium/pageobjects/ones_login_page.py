# coding=utf-8
from framework.base_page import BasePage

from config import settings

config = settings.GetConfig().getconfig()

class OnesLoginPageElement(object):
    ones_account = config.get("testAccount","email")
    ones_password = config.get("testAccount","password")
    account_box = "xpath=>//*[@id='login']/div[1]/div[2]/input"
    password_box = "xpath=>//*[@id='login']/div[1]/div[4]/div/input"
    commit_btn = "xpath=>//*[@id='login']/div[2]/button"


class OnesLoginPage(BasePage):
    def __init__(self, driver):
        super(OnesLoginPage, self).__init__(driver)
        element = OnesLoginPageElement()
        self._element = element

    def input_account(self):
        self.click(self._element.account_box)
        self.type(self._element.account_box, self._element.ones_account)

    def input_password(self):
        self.click(self._element.password_box)
        self.type(self._element.password_box, self._element.ones_password)

    def click_commit(self):
        self.click(self._element.commit_btn)
        self.sleep(2)
