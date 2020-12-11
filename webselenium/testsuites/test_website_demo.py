# coding=utf-8
import unittest
from config import settings
from pageobjects.demo.ones_demo import OnesDemoPage
from pageobjects.demo.ones_demo_login import OnesDemoLoginPage
from pageobjects.demo.ones_progress_manage import OnesProgressManagePage
from framework.browser_engine import BrowserEngine


class WebsiteDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(settings.GetConfig().getconfig().get('testServer', 'DEMO_URL'))
        cls.onesDemoPage = OnesDemoPage(cls.driver)
        cls.onesDemoLoginPage = OnesDemoLoginPage(cls.driver)
        cls.onesProgressManagePage = OnesProgressManagePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_agoto_demo(self):
        '''
        从官网进入到「通用项目」demo
        '''
        self.onesDemoPage.click_progress_manage()
        demo_login_form_head_text = self.onesDemoLoginPage.demo_login_form_head_text()
        if demo_login_form_head_text:
            self.assertEqual(demo_login_form_head_text,
                             '验证手机号，体验 Demo', '没有进入到登陆页')
            self.onesDemoLoginPage.input_mobile_phone()
            self.onesDemoLoginPage.input_verification_code()
            self.onesDemoLoginPage.click_demo_button()
        progress_manage_below_text = self.onesProgressManagePage.progress_manage_above_text()
        self.assertEqual(progress_manage_below_text,
                         '通用项目管理场景支持', '没有进入到「通用项目」demo')

    def test_requirement_manage(self):
        '''
        测试「需求管理」
        '''
        self.onesProgressManagePage.refresh()
        show = self.onesProgressManagePage.demo_feature_tips_is_show()
        if not show == 'show':
            self.onesProgressManagePage.click_function_prompts()
        #点击「需求管理」
        self.onesProgressManagePage.click_demo_feature_manage(1)
        # 校验文案
        self.assertEqual(self.onesProgressManagePage.progress_manage_below_text(1
        ), '你可以在 ONES Project 对项目需求进行管理，为需求添加来源，设置优先级、指定负责人等。', '「需求管理」文案不正确')
        #
        # 点击”去试试“
        self.onesProgressManagePage.click_have_try()
        self.onesProgressManagePage.switch_to_demo_frame()
        #校验团队
        self.assertEqual(
            self.onesProgressManagePage.team_name_text(), '通用项目管理 Demo', '团队不正确')
        # 校验项目
        self.assertEqual(
            self.onesProgressManagePage.project_name_text(), '贷款审核后台Web', '项目不正确')
        #校验「全部需求」名称
        self.assertEqual(self.onesProgressManagePage.requirement_view_name_text(), '全部需求', '「全部需求」名字不正确')
        #校验视图「全部需求」是否被选中
        self.assertEqual(self.onesProgressManagePage.requirement_view_is_actived(
        ), 'FoldableTabs-item FoldableTabs-item-actived', '「全部需求」没有被选中')



    def test_dev_pipeline_manage(self):
        '''
        测试「研发流程管理」
        '''
        self.onesProgressManagePage.refresh()
        show = self.onesProgressManagePage.demo_feature_tips_is_show()
        if not show == 'show':
            self.onesProgressManagePage.click_function_prompts()
        # 点击「研发流程管理」
        self.onesProgressManagePage.click_demo_feature_manage(2)
        # 校验文案
        self.assertEqual(self.onesProgressManagePage.progress_manage_below_text(2
        ), '通过使用「前端研发任务」组件来管理所有研发任务。你也可以创建想要的视图来快速定位关注的任务，例如“我关注的研发任务”。', '「研发流程管理」文案不正确')
        #点击”去试试“
        self.onesProgressManagePage.click_have_try()
        self.onesProgressManagePage.switch_to_demo_frame()
        #校验视图名
        self.assertEqual(self.onesProgressManagePage.requirement_view_name_text(), '我关注的前端研发任务', '视图名称不正确')
        #校验视图「我关注的前端研发任务」是否被选中
        self.assertEqual(self.onesProgressManagePage.requirement_view_is_actived(
        ), 'FoldableTabs-item FoldableTabs-item-actived', '「我关注的前端研发任务」没有被选中')

    def test_project_statement(self):
        '''
        测试「项目报表」
        '''
        self.onesProgressManagePage.refresh()
        show = self.onesProgressManagePage.demo_feature_tips_is_show()
        if not show == 'show':
            self.onesProgressManagePage.click_function_prompts()
        # 点击「项目报表」
        self.onesProgressManagePage.click_demo_feature_manage(3)
        # 校验文案
        self.assertEqual(self.onesProgressManagePage.progress_manage_below_text(3
        ), '通过使用「报表」组件对数据进行收集与整理，生成所需报表以便跟踪项目进度以及成员的绩效指标等信息。', '「项目报表」文案不正确')
        #点击”去试试“
        self.onesProgressManagePage.click_have_try()
        self.onesProgressManagePage.switch_to_demo_frame()
        #校验报表名
        self.assertEqual(self.onesProgressManagePage.default_statement_text(), '常用报表', '报表名称不正确')
        #校验报表「常用报表」是否被选中
        self.assertEqual(self.onesProgressManagePage.default_statement_is_actived(
        ), 'item active', '「常用报表」没有被选中')


    def test_progress_manage(self):
        '''
        测试「进度管理」
        '''
        self.onesProgressManagePage.refresh()
        show = self.onesProgressManagePage.demo_feature_tips_is_show()
        if not show == 'show':
            self.onesProgressManagePage.click_function_prompts()
        # 点击「进度管理」
        self.onesProgressManagePage.click_demo_feature_manage(4)
        # 校验文案
        self.assertEqual(self.onesProgressManagePage.progress_manage_below_text(4
        ), '通过使用「甘特图」组件对项目进度进行把控。你可以通过同步项目中的任务、新建里程碑等可视化操作来监控项目进度。', '「进度管理」文案不正确')
        #点击”去试试“
        self.onesProgressManagePage.click_have_try()
        self.onesProgressManagePage.switch_to_demo_frame()
        #校验组件「甘特」名
        self.assertEqual(self.onesProgressManagePage.gantt_module_text(), '甘特图', '组件名称不正确')
        #校验视图「我关注的前端研发任务」是否被选中
        self.assertEqual(self.onesProgressManagePage.gantt_module_is_actived(
        ), 'FoldableTabs-item FoldableTabs-item-actived', '「甘特图」没有被选中')


    def test_manhour_statement(self):
        '''
        测试「工时报表」
        '''
        self.onesProgressManagePage.refresh()
        show = self.onesProgressManagePage.demo_feature_tips_is_show()
        if not show == 'show':
            self.onesProgressManagePage.click_function_prompts()
        # 点击「工时报表」
        self.onesProgressManagePage.click_demo_feature_manage(5)
        # 校验文案
        self.assertEqual(self.onesProgressManagePage.progress_manage_below_text(5
        ), '通过查看「报表」组件中的工时报告对成员工时进行管控与追溯。', '「工时报表」文案不正确')
        #点击”去试试“
        self.onesProgressManagePage.click_have_try()
        self.onesProgressManagePage.switch_to_demo_frame()
        #校验「工时日志总览」报表名
        self.assertEqual(self.onesProgressManagePage.manhour_log_statement_text(), '工时日志报表', '报表名称不正确')
        #校验报表「常用报表」是否被选中
        self.assertEqual(self.onesProgressManagePage.manhour_log_statement_is_actived(
        ), 'item active', '「常用报表」没有被选中')

