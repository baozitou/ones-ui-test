# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
from pynput.keyboard import Key, Controller
from framework.base_page import BasePage

class DeleteProjectElement(object):
    ONES_Project = 'css=>svg[class$="roject "] +span'  #project产品线
    all_project_name_elements = 'css=>.grid-lock-cell-inner div div div div div div[class="name"]'   #获取所有项目名称
    all_components_elements = 'css=>[class$=component-tabs] a'   #获取所有组件
    all_setting_elements = 'css=>[class$=ComponentMain-top] div a'   #获取所有项目设置名称
    deletel_project_element = 'css=>[class$=ComponentMain-main]  div[class$="middle "]'  #"删除项目"按钮
    deletel_prompts_element = 'css=>[class="toastWrap "]'


class deleteprojectOperate(BasePage):
    def __init__(self, driver):
        self.keyboard = Controller()
        super(deleteprojectOperate, self).__init__(driver)
        element = DeleteProjectElement()
        self._element = element


    def click_operate(self):
        self.click(self._element.ONES_Project)

    def click_delete(self):
        self.click(self._element.deletel_project_element)

    #获取所有项目名称element，返回列表
    def get_all_project_element(self):
        all_project_name_elements = self.find_elements(self._element.all_project_name_elements)
        print(all_project_name_elements)
        return all_project_name_elements

    #获取所有组件element，返回列表
    def get_all_components_elements(self):
        all_components_elements = self.find_elements(self._element.all_components_elements)
        return all_components_elements

    #获取所有项目设置element，返回列表
    def get_all_setting_elements(self):
        all_setting_elements = self.find_elements(self._element.all_setting_elements)
        return all_setting_elements

    def get_text_select_element_click(self,elements,name):
        for element in elements:
            if self.get_text(element) == name:
                self.get_click(element)
                break

    def get_attribute_select_element_click(self,elements,name,key):
        for element in elements:
            if self.get_attribute_element(element,key) == name:
                self.get_click(element)
                break
