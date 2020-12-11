# -*- coding: utf-8 -*-#
from framework.base_page import BasePage
from config import settings
from utils.logger import Logger


logger = Logger(logger=__name__).getlog()

config = settings.GetConfig().getconfig()


class OnesLoginElement(object):
    ones_email = config.get("testAccount", "email")
    ones_password = config.get("testAccount", "password")
    email = 'css=>input[placeholder$="邮箱"]'  #账号
    password = 'css=>input[placeholder$="密码"]' #密码
    login_button = 'css=>button[type="submit"]' #登陆
    # new_product_tips='css=>button[class$="btn-lg"]'  #上线功能提示
    # new_plan_tips = 'css=>button[class$="btn-small"]'  #新功能了解
    # one_team = 'css=>div[class^="scroll-div organization"] div:nth-of-type(1) div:nth-child(1)' #第一个团队
    # get_organization = 'css=>div[class$=team-or]+a' # 获取"组织管理"


class OnesLoginOperate(BasePage):

    def __init__(self, driver):
        super(OnesLoginOperate,self).__init__(driver)
        element = OnesLoginElement()
        self._element = element


    def click_email(self):
        logger.info("Starting login ONES {}".format(self._element.ones_email))
        self.click(self._element.email)
        self.type(self._element.email, self._element.ones_email)

    def click_password(self):
        self.click(self._element.password)
        self.type(self._element.password, self._element.ones_password)

    def click_login_button(self):
        self.click(self._element.login_button)

    # def get_organization_text(self):
    #     return self.text(self._element.get_organization)
    #
    # def click_one_team(self):
    #     self.click(self._element.one_team)
    #
    # def click_new_product_tips(self):
    #     self.click(self._element.new_product_tips)
    #
    # def click_new_plan_tips(self):
    #     self.click(self._element.new_plan_tips)




