# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
from pynput.keyboard import Key, Controller
from framework.base_page import BasePage

class CreatProjectElement(object):
    ONES_Project = 'css=>svg[class$="roject "] +span'  #project产品线
    creat_project = 'css=>button[class$=ones-btn-primary]'   #新建项目
    input_project_name = 'css=>div[class$="module-content"] input'  #输入项目名称
    choose_tradition_project= 'css=>div[class="project-template-list"] div:nth-last-child(3) [role="presentation"]' #选择瀑布项目
    next_step = 'css=>div[class$=project_template] div:nth-child(2) button:nth-child(2)'  #下一步
    finish = 'css=>[class$=select-member]+div button:nth-child(2)' #完成
    get_creat_project_name = 'css=>span[class="main-card-title"]' #获取项目名称
    get_all_components = 'css=>[class$="tabs"] a' #获取所有组件


class CreatProjectOperate(BasePage):
    def __init__(self, driver):
        self.keyboard = Controller()
        super(CreatProjectOperate, self).__init__(driver)
        element = CreatProjectElement()
        self._element = element

    #进入project产品线
    def click_ONES_Project(self):
        self.click(self._element.ONES_Project)

    def click_add_project(self):
        self.click(self._element.creat_project)

    def input_project_name(self,project_name):
        self.click(self._element.input_project_name)
        self.type(self._element.input_project_name,project_name)

    #选择传统项目
    def choose_tradition_project(self):
        self.click(self._element.choose_tradition_project)

    def click_next_step(self):
        self.click(self._element.next_step)

    def click_finish(self):
        self.click(self._element.finish)

    #键盘操作弹框确认
    def key_enter(self):
        self.keyboard.press(Key.enter)

    def get_project_name(self):
        return self.text(self._element.get_creat_project_name)

    #获取所以组件展示
    def get_all_component_value(self,key):
        return self.get_attribute_elements(self._element.get_all_components,key)

