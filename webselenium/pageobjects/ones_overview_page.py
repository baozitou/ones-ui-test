# coding=utf-8
from framework.base_page import BasePage

class OverviewPageElement(object):
    first_team = "s=>body > div:nth-child(12) > div > div.ant-modal-wrap.organization-select-team > div > div.ant-modal-content > div > div.scroll-div.organization-select-team-list.ps-container.ps-theme-default.ps-active-y > div:nth-child(2) > div.organization-select-team-single-name"
    target_team = "s=>body > div:nth-child(12) > div > div.ant-modal-wrap.organization-select-team > div > div.ant-modal-content > div > div.scroll-div.organization-select-team-list.ps-container.ps-theme-default.ps-active-y > div:nth-child(23) > div.organization-select-team-single-name"


class OverviewPage(BasePage):
    #多团队，选择团队
    def __init__(self, driver):
        super(OverviewPage, self).__init__(driver)
        element = OverviewPageElement()
        self._element = element

    def select_team(self):
        self.move_to_element(self._element.first_team)
        self.scroll_into_view(self._element.target_team)
        self.click(self._element.target_team)

    def get_team_name(self):
        el = self.find_element(self._element.target_team)
        return el.text