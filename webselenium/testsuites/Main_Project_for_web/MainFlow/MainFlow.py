# # coding=utf-8
# from selenium.common.exceptions import NoSuchElementException
# # from framework.setup import Checkmethod,Login
# from pynput.keyboard import Key, Controller
# import logging
#
# logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
#
# URL = "https://dev.myones.net/project/master/#/auth/login"
#
# class CoreTestCase:
#
#     # driver = webdriver.Chrome()
#     # keyboard = Controller()
#
#     def __init__(self,login):
#         self.keyboard = Controller()
#         # self.check = Checkmethod()
#         # self.login = Login()
#         # self.login.login()
#         self.driver = self.login.dr
#         self.driver.implicitly_wait(10)
#
#     def creat_project_quick(self):
#         """
#         新建敏捷模型项目
#         断言：项目名称
#         """
#         try:
#             creat_project_name = "UI自动化敏捷项目"
#             ONES_Project_element = 'svg[class$="index-Main_Project_for_web "]+span'
#             creat_project_element = 'button[class$=ones-btn-primary]'
#             input_project_name_element = 'div[class$=Main_Project_for_web-name] input'
#             next_step_element = 'div[class$=project_template] div:nth-child(2) button:nth-child(2)'
#             finish_creat_element = '[class$=select-member]+div button:nth-child(2)'
#             get_creat_project_name_element = 'a[class$="action"][target$="_blank"]'
#             self.driver.find_element_by_css_selector(ONES_Project_element).click()
#             self.driver.find_element_by_css_selector(creat_project_element).click()
#             self.driver.find_element_by_css_selector(input_project_name_element).click()
#             self.driver.find_element_by_css_selector(input_project_name_element).send_keys(creat_project_name)
#             self.driver.find_element_by_css_selector(next_step_element).click()
#             self.driver.find_element_by_css_selector(finish_creat_element).click()
#             self.driver.find_elements_by_css_selector()
#             self.keyboard.press(Key.enter)
#             get_project_name = self.driver.find_element_by_css_selector(get_creat_project_name_element).text
#             self.check.contrast_str(creat_project_name,get_project_name)
#         except NoSuchElementException:
#             logging.info("NoSuchElementException")
#
#     def check_quick_project_component(self):
#         """
#         新建敏捷模型校验点
#         断言：敏捷默认项目组件
#         """
#         try:
#
#             ONES_Project_element = 'svg[class$="index-Main_Project_for_web "]+span'
#             click_project_name = '.grid-lock-cell-inner div div div:nth-child(145) div div div:nth-child(1)'
#             project_all_component_element = '//div[@class="FoldableTabs-item FoldableTabs-item-actived"]/../div/a'
#             get_project_all_component_list = []
#             self.driver.find_element_by_css_selector(ONES_Project_element).click()                  #ONES Project
#             self.driver.find_element_by_css_selector(click_project_name).click()                  #选择一款项目
#             get_project_all_component_element = self.driver.find_elements_by_xpath(project_all_component_element)
#             for get_name in get_project_all_component_element:
#                 get_project_all_component_list.append(get_name.get_attribute("title"))
#             alist = ['项目概览','迭代','计划','需求','缺陷','任务','筛选器','文档','报表','成员','项目设置']
#             self.check.contrast_list(alist,get_project_all_component_list,"project_component_error")
#
#         except NoSuchElementException:
#             logging.info("NoSuchElementException")
#
#     def creat_tradition_project(self):
#         '''
#         新建瀑布模型验证点
#         断言：项目名称
#         '''
#         try:
#             creat_project_name = "UI自动化瀑布项目"
#             ONES_Project_element = 'svg[class$="index-Main_Project_for_web "]+span'
#             creat_project_element = 'button[class$=ones-btn-primary]'
#             input_project_name_element = 'div[class$=Main_Project_for_web-name] input'
#             choose_tradition_project_element = '//*[@class="ui-icon icon-scrum-Main_Project_for_web-select-small-color "]/../../../../div[2]/div[1]'
#             next_step_element = 'div[class$=project_template] div:nth-child(2) button:nth-child(2)'
#             finish_creat_element = '[class$=select-member]+div button:nth-child(2)'
#             get_creat_project_name_element = 'span[class="main-card-title"]'
#             self.driver.find_element_by_css_selector(ONES_Project_element).click()      #ONES Project
#             self.driver.find_element_by_css_selector(creat_project_element).click()
#             self.driver.find_element_by_css_selector(input_project_name_element).click()
#             self.driver.find_element_by_css_selector(input_project_name_element).send_keys(creat_project_name)
#             self.driver.find_element_by_xpath(choose_tradition_project_element).click()
#             self.driver.find_element()
#             self.driver.find_element_by_css_selector(next_step_element).click()
#             self.driver.find_element_by_css_selector(finish_creat_element).click()
#             self.keyboard.press(Key.enter)     #操作键盘回车键
#             get_project_name = self.driver.find_element_by_css_selector(get_creat_project_name_element).text
#             self.check.contrast_str(creat_project_name,get_project_name)
#
#         except NoSuchElementException:
#             logging.info("NoSuchElementException")
#
#
#     def check_tradition_project_component(self):
#         try:
#             ONES_Project_element = 'svg[class$="index-Main_Project_for_web "]+span'
#             click_project_name = '.grid-lock-cell-inner div div div:nth-child(157) div div div:nth-child(1)'
#             project_all_component_element = '//div[@class="FoldableTabs-item FoldableTabs-item-actived"]/../div/a'
#             get_project_all_component_list = []
#             self.driver.find_element_by_css_selector(ONES_Project_element).click()                  #ONES Project
#             self.driver.find_element_by_css_selector(click_project_name).click()                  #选择一款项目
#             get_project_all_component_element = self.driver.find_elements_by_xpath(project_all_component_element)
#             for get_name in get_project_all_component_element:
#                 get_project_all_component_list.append(get_name.get_attribute("title"))
#             alist = ['项目概览','甘特图','需求','缺陷','任务','筛选器','文档','报表','成员','项目设置']
#             self.check.contrast_list(alist,get_project_all_component_list)
#             self.driver.find_element_by_css_selector('[class$="component-tabs"] div:nth-child(5) a').click()
#             self.driver.find_element_by_css_selector('[class$=ComponentMain-top] div:nth-child(7) a').click()
#             deletel_project_element = '[class$=ComponentMain-main]  div[class$="middle "]'
#             self.driver.find_element_by_css_selector(deletel_project_element).click()
#
#         except NoSuchElementException:
#             logging.info("NoSuchElementException")
#
#     def select_delete_project(self,project_name):
#         '''
#         根据项目名称，删除项目
#         :param project_name: 项目名称（项目名称不能重复）
#         :return:
#         '''
#         try:
#             setting = '项目设置'
#             setting_more = "更多"
#             prompts_name ="删除成功"
#             ONES_Project_element = 'svg[class$="index-Main_Project_for_web "]+span'
#             all_project_name_elements = '.grid-lock-cell-inner div div div div div div[class="name"]'
#             all_components_elements = '[class$=component-tabs] a'
#             all_setting_elements ='[class$=ComponentMain-top] div a'
#             deletel_project_element = '[class$=ComponentMain-main]  div[class$="middle "]'
#             deletel_prompts_element = '[class="toastWrap "]'
#
#             self.driver.find_element_by_css_selector(ONES_Project_element).click()                  #ONES Project
#             all_project_name_element=self.driver.find_elements_by_css_selector(all_project_name_elements)
#             for project_name_element in all_project_name_element:
#                 if project_name_element.text == project_name:
#                     project_name_element.click()
#                     all_component_elements = self.driver.find_elements_by_css_selector(all_components_elements)
#                     for pcomponent_element in all_component_elements:
#                         if pcomponent_element.get_attribute('title') == setting:
#                             pcomponent_element.click()
#                             all_setting_elements = self.driver.find_elements_by_css_selector(all_setting_elements)
#                             for select_setting_more in all_setting_elements:
#                                 if select_setting_more.get_attribute('title') == setting_more:
#                                     select_setting_more.click()
#                                     self.driver.find_element_by_css_selector(deletel_project_element).click()
#                                     self.keyboard.press(Key.enter)  # 操作键盘回车键
#                                     get_prompts_name =self.driver.find_element_by_css_selector(deletel_prompts_element).text
#                                     self.check.contrast_str(get_prompts_name,prompts_name)
#
#         except NoSuchElementException:
#             logging.info("NoSuchElementException")
#
#
# if __name__ == '__main__':
#     CoreTestCase=CoreTestCase()
#     CoreTestCase.select_delete_project("UI自动化敏捷项目")
#     # CoreTestCase.check_tradition_project_component()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
