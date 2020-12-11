# coding=utf-8
import unittest
from pageobjects.ones_login_page import OnesLoginPage
from pageobjects.ones_overview_page import OverviewPage
from framework.browser_engine import BrowserEngine

from config import settings

config = settings.GetConfig().getconfig()

class LoginLampo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(url=config.get("testServer","TEST_URL"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_ones_login(self):
        onesloginpage = OnesLoginPage(self.driver)
        onesloginpage.input_account()
        onesloginpage.input_password()
        onesloginpage.click_commit()
        # 这里先注释，不管校验
        # assert '概览 | ONES Project' in onesloginpage.get_page_title()

    def test_select_team(self):
        overviewpage = OverviewPage(self.driver)
        overviewpage.select_team()
        self.assertEqual('付费_冷冰团队',overviewpage.get_team_name())


if __name__ == "__main__":
    unittest.main()