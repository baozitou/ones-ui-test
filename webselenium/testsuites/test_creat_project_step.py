# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
import unittest,time
from config import settings
from pageobjects.ones_project_for_web.Project_home_page.creat_projrct import CreatProjectOperate
from pageobjects.ones_project_for_web.Project_home_page.delete_project import deleteprojectOperate
from pageobjects.ones_project_for_web.ones_login import OnesLoginOperate
from framework.browser_engine import BrowserEngine

class WebsiteProject(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(settings.GetConfig().getconfig().get('testServer','URL'))
        cls.OnesLogin = OnesLoginOperate(cls.driver)
        # cls.creatProject = CreatProjectOperate(cls.driver)
        # cls.deleteProject = deleteprojectOperate(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

    def test_01alogin_ONES(self):
        """
        正常登陆ONES系统
        """
        print("组织管理")
        self.OnesLogin.click_email()
        self.OnesLogin.click_password()
        self.OnesLogin.click_login_button()
        # time.sleep(15)
        # organization_text = self.OnesLogin.get_organization_text()
        # self.assertEqual(organization_text,"组织管理")
        # self.OnesLogin.click_one_team()
        # # self.OnesLogin.click_new_product_tips()
        # # self.OnesLogin.click_new_plan_tips()

    # def test_02creat_quick_project(self):
    #     '''
    #     正常创建敏捷项目
    #     '''
    #     quick_project_name = "UI自动化敏捷项目"
    #     self.creatProject.click_ONES_Project()    #进入ONES Project 产品线
    #     self.creatProject.click_add_project()     #新建项目
    #     self.creatProject.input_project_name(quick_project_name)  #点击输入项目名称
    #     self.creatProject.click_next_step()       #点击下一步
    #     self.creatProject.click_finish()          #点击完成
    #     self.creatProject.key_enter()             #回车
    #     self.assertEqual(self.creatProject.get_project_name(),quick_project_name)  #断言新项目名称
    #
    # def test_03check_quick_project_component(self):
    #     all_component_text = self.creatProject.get_all_component_value("title")
    #     all_quick_component_list = ['项目概览','迭代','计划','需求','缺陷','任务','筛选器','文档','报表','成员','项目设置']
    #     self.assertEqual(all_component_text,all_quick_component_list)
    #
    # def test_04creat_tradition_project(self):
    #     '''
    #     正常创建传统项目
    #     '''
    #     tradition_project_name = "UI自动化传统项目"
    #     self.creatProject.click_ONES_Project()    #进入ONES Project 产品线
    #     self.creatProject.click_add_project()     #新建项目
    #     self.creatProject.input_project_name(tradition_project_name)  #点击输入项目名称
    #     self.creatProject.choose_tradition_project()   #选择传统项目
    #     self.creatProject.click_next_step()       #点击下一步
    #     self.creatProject.click_finish()          #点击完成
    #     self.creatProject.key_enter()             #回车
    #     self.assertEqual(self.creatProject.get_project_name(),tradition_project_name)  #断言新项目名称
    #
    # def test_05check_tradition_project_component(self):
    #     all_component_text = self.creatProject.get_all_component_value("title")
    #     all_quick_component_list = ['项目概览','甘特图','需求','缺陷','任务','筛选器','文档','报表','成员','项目设置']
    #     self.assertEqual(all_component_text,all_quick_component_list)
    #
    # def test_06delete_project(self):
    #     '''
    #     删除项目名称
    #     '''
    #     project_name = "UI自动化传统项目"
    #     setting_name = "项目设置"
    #     setting_more_name = "更多"
    #     # prompts_name = "删除成功"
    #     self.deleteProject.click_operate()
    #     all_project_element = self.deleteProject.get_all_project_element()  #获取所有的project_elements
    #     self.deleteProject.get_text_select_element_click(all_project_element,project_name)
    #     all_components_elements = self.deleteProject.get_all_components_elements()  #获取所有的component_elements
    #     self.deleteProject.get_attribute_select_element_click(all_components_elements,setting_name,"title")
    #     all_setting_elements = self.deleteProject.get_all_setting_elements()    #获取所有的setting_elements
    #     self.deleteProject.get_attribute_select_element_click(all_setting_elements,setting_more_name,"title")
    #     self.deleteProject.click_delete()         #点击删除按钮
    #     self.creatProject.key_enter()             #回车




