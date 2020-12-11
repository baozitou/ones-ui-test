# coding=utf-8
from framework.base_page import BasePage

class OnesProgressManageElement(object):
    #弹窗是否显示
    demo_feature_tips = 'id=>demo-feature-tips'
    #功能提示
    function_prompts = 'xpath=>/html/body/div[3]/div[2]/div[1]'
    #更多 Demo
    more_demo = 'xpath=>/html/body/div[3]/div[2]/div[2]' 
    #文案："通用项目管理场景支持"
    progress_manage_above_text = 'xpath=>//*[@id="demo-feature-tips"]/div/div[1]' 
    #5个tips，从1-5分别是：需求管理，研发流程管理，项目报表，进度管理，工时报表
    demo_feature_manage = 'xpath=>//*[@id="demo-feature-tips"]/div/div[2]/div[{}]'
    #卡片的文案
    progress_manage_below_text = 'xpath=>//*[@id="demo-feature-tips"]/div/div[3]/div/div[{}]/div'
    #去试试
    have_try = 'xpath=>//*[@id="demo-feature-tips"]/div/div[4]/div'

    #demo中，具体项目需要定位的元素
    #通用项目管理 Demo
    team_name = 'xpath=>/html/body/div[1]/div/div/div/div[1]/div[2]/div'
    #贷款审核后台Web
    project_name = 'xpath=>/html/body/div[1]/div/div/div/div[2]/div[1]/div[1]/header/div[1]/div[2]/div/div/a[1]'
    #「全部需求」视图
    requirement_view = 'xpath=>/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[1]/div[1]/div/div[1]'
    #常用报表
    default_statement = 'xpath=>/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div[1]'
    #甘特图组件
    gantt_module = 's=>#null > div.FoldableTabs-item.FoldableTabs-item-actived'
    #工时总览报表
    manhour_log_statement = 'xpath=>/html/body/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div[7]'
    #frame
    frame_id = 'demo-frame'

class OnesProgressManagePage(BasePage):
    def __init__(self, driver):
        super(OnesProgressManagePage, self).__init__(driver)
        element = OnesProgressManageElement()
        self._element = element
    
    def click_function_prompts(self):
        self.click(self._element.function_prompts)

    def click_more_demo(self):
        self.click(self._element.more_demo)
    
    def click_demo_feature_manage(self, index):
        self.click(self._element.demo_feature_manage.format(index))

    def click_have_try(self):
        self.click(self._element.have_try)

    def progress_manage_below_text(self, index):
        #获取弹窗下方的文案
        return self.text(self._element.progress_manage_below_text.format(index))
    
    def progress_manage_above_text(self):
        #获取弹窗上方的文案
        return self.text(self._element.progress_manage_above_text)
    
    def demo_feature_tips_is_show(self):
        return self.get_attribute(self._element.demo_feature_tips, 'class')

    def team_name_text(self):
        team_name = self.text(self._element.team_name)
        return team_name
    
    def project_name_text(self):
        return self.text(self._element.project_name)

    def requirement_view_name_text(self):
        return self.text(self._element.requirement_view)
    
    def requirement_view_is_actived(self):
        return self.get_attribute(self._element.requirement_view, 'class')

    def default_statement_text(self):
        return self.text(self._element.default_statement)

    def default_statement_is_actived(self):
        return self.get_attribute(self._element.default_statement, 'class')
    
    def gantt_module_text(self):
        print(self._element.gantt_module)
        return self.text(self._element.gantt_module)
    
    def gantt_module_is_actived(self):
        return self.get_attribute(self._element.gantt_module, 'class')

    def manhour_log_statement_text(self):
        return self.text(self._element.manhour_log_statement)
    
    def manhour_log_statement_is_actived(self):
        return self.get_attribute(self._element.manhour_log_statement, 'class')

    def switch_to_demo_frame(self):
        self.switch_to_frame(self._element.frame_id)