# 封装前台登录页面类
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import day08.commons.utils as utils
from day08.commons.utils import is_front_login


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 定义一个类方法完成显式等待
    def wait(self,func):
        return WebDriverWait(self.driver, 5).until(func)

    # 重写(装饰)元素定位的方法，结合显示等待一起使用
    def find_element(self,by,value,need_text=False):
        def f(driver):
            if driver.find_element(by,value).text:
                msg = driver.find_element(by,value).text
                if need_text: # 元素需要获取文本属性就可以传递实参为 True 来返回文本内容
                    # 当获取元素的文本，该元素存在但是没有出现文本，那么将空文本替换直到有文本才返回
                    return msg.replace(" ","")
                else:
                    return True
            else:
                return True
        # 一旦调用重写的 find_element 方法，那么先触发显式等待
        self.wait(f)

        # 触发完显示等待之后，使用原生的 find_element() 定位元素
        return self.driver.find_element(by, value)


class FrontLoginPage(BasePage):
    # 验证码图片保存路径
    # code_img_path = '../../data/code_img.png'
    code_img_path = './data/code_img.png'
    # cookie 信息保存路径
    # cookie_path = '../../data/front_cookie.json'
    cookie_path = './data/front_cookie.json'


    # 将页面中所有需要被操作的元素定义为类属性
    # 1.登录
    # 点击登录按钮
    btn_login = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/a')
    # 输入账号
    ipt_username = (By.XPATH, '//*[@id="login-email-address"]')
    # 输入密码
    ipt_password = (By.XPATH, '//*[@id="login-password"]')
    # 点击登录
    btn_login_submit = (By.XPATH, '//*[@id="ajax-login-submit"]')
    # 点击提示框信息确认
    login_msg = (By.XPATH, '//*[starts-with(@id,"fanwe_")]/table/tbody/tr/td[2]/div[2]')
    # 提示登录成功的按钮
    btn_login_ok = (By.XPATH, '//*[starts-with(@id,"fanwe_")]/table/tbody/tr/td[2]/div[3]/input[1]')

    # 2.投标
    # ● 点击马上投标按钮
    btn_deal_submit = (By.XPATH, '/html/body/div[7]/div[2]/div[1]/div[1]/ul/li[1]/span[6]/a/span')
    # ● 点击立即投资
    btn_bid = (By.XPATH, '//*[@id="tz_link"]')
    # ● 输入支付密码
    ipt_pay_password = (By.XPATH, '//*[@id="J_bid_password"]')
    # ● 点击确定按钮
    btn_pay_submit = (By.XPATH, '//*[@id="J bindpassword_btn"]')
    # ● 关闭提示信息弹框(手写 xpath)
    pay_msg = (By.XPATH, '//*[starts-with(@id,"fanwe_")]/table/tbody/tr/td[2]/div[2]')
    # 获取提示信息的实际结果断言预期结果
    txt_deal_msg = (By.XPATH, '//*[starts-with(@id,"fanwe_")]/table/tbody/tr/td[2]/div[3]/input[1]')

    # 定义测试用例
    # 1. 登录前台
    def login(self,username,password,code=None):

        utils.load_cookies(self.driver, self.cookie_path)

        if not is_front_login(self.driver):

            # 获取验证码图片
            self.find_element(By.XPATH, '//*[@id="Jverify_img"]').screenshot(self.code_img_path)

            # ● 点击登录按钮
            self.find_element(*self.btn_login).click()
            # ● 输入账号
            self.find_element(*self.ipt_username).send_keys(username)
            # ● 输入密码
            self.find_element(*self.ipt_password).send_keys(password)
            # ● 点击登录
            self.find_element(*self.btn_login_submit).click()
            # ● 点击提示框信息确认
            msg = self.find_element(*self.login_msg, need_text=True)
            self.find_element(*self.btn_login_ok).click()

            # 保存 cookie 信息
            utils.sava_cookies(self.driver, self.cookie_path)

            return msg

    # 2. 新增投标
    def new_loan_bid(self,pay_passwd) -> str:
        # ● 点击马上投标按钮
        self.find_element(*self.btn_deal_submit).click()
        # ● 点击立即投资
        self.find_element(*self.btn_bid).click()
        # ● 输入支付密码
        self.find_element(*self.ipt_pay_password).send_keys(pay_passwd)
        # ● 点击确定按钮
        self.find_element(*self.btn_bid).click()
        # ● 获取提示信息的实际结果断言预期结果
        msg = self.find_element(*self.pay_msg, need_text=True)
        self.find_element(*self.txt_deal_msg).click()

        return msg

class BackgroundLoginPage(BasePage):
    # 验证码图片保存路径
    # code_img_path = '../../data/code_img.png'
    code_img_path = './data/code_img.png'
    # cookie 信息保存路径
    # cookie_path = '../../data/back_cookie.json'
    cookie_path = './data/back_cookie.json'

    # ○ 账号输入框
    ipt_username = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/input')
    # ○ 密码输入框
    ipt_password = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]/input')
    # ○ 验证码输入框
    ipt_code = (By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]/input')
    # ○ 验证码图片
    img_code =(By.XPATH,'//*[@id="verify"]')
    # ○ 点击登录后台按钮
    btn_login_submit = (By.XPATH, '//*[@id="login_btn"]')
    # 登录信息弹窗
    login_msg = (By.XPATH, '//*[@id="login_msg"]')

    def login(self,username,password,code=None):



        utils.load_cookies(self.driver, self.cookie_path)

        # 如果没登陆
        if not utils.is_back_login(self.driver):
            # 获取验证码图片
            self.find_element(*self.img_code).screenshot(self.code_img_path)

            # ○ 输入账号
            self.find_element(*self.ipt_username).send_keys(username)
            # ○ 输入密码
            self.find_element(*self.ipt_password).send_keys(password)
            # ○ 输入验证码
            self.find_element(*self.ipt_code).send_keys(utils.identify_code_img(self.code_img_path) if code is None else code)
            # ○ 点击登录后台按钮
            self.find_element(*self.btn_login_submit).click()
            # ○ 获取登录信息
            msg = self.find_element(*self.login_msg,need_text=True).text

            # 保存 cookie 信息
            utils.sava_cookies(self.driver,self.cookie_path)

            return msg
        else:
            self.driver.refresh()


class NewLoanPage():
    # 1. 完成登录操作（通过 fixture）

    # 2. 打开贷款管理页面
    # 2.1 定位【贷款管理】按钮（上侧导航栏）
    frame_up = (By.XPATH, '/html/frameset/frame[1]')
    # 贷款管理按钮
    btn_loan_manage = (By.XPATH, '//*[@id"navs"]/u1/1i[2]/a')

    # 2.2 定位【新增贷款】按钮（左侧导航栏）
    frame_left = (By.XPATH, '//*[@id="main-frame"]')
    # 【新增贷款】按钮
    btn_new_loan = (By.XPATH, '/html/body/div[2]/div[3]/input[1]')

    # 2.3 进入【新增贷款】页面(右侧填写信息)
    # 完成新增贷款页面的元素定位及操作(输入新增贷款需要的信息)
    # 颜色
    ipt_color = (By.XPATH, '//*[@id="colorpickerField"]')
    # 借款编号
    ipt_loan_number = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[3]/td[2]/input')
    # 贷款名称
    ipt_loan_name = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input')
    # 简短名称
    ipt_short_name = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[5]/td[2]/input')
    # 会员名称
    ipt_member_name = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[6]/td[2]/input[1]')
    # 选择后台会员（xpath 会变化）
    select_member_name = (By.XPATH, '//strong[text()="Thw"]')
    # 所在城市
    ipt_city=(By.XPATH, '//*[@id="citys_box"]/div[1]/div[2]/input[3]')
    # 分类：
    select_loan_type = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[8]/td[2]/select')
    # 担保机构：
    select_guarantee_org = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[9]/td[2]/select')
    # 担保范围：
    select_guarantee_scope=(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[10]/td[2]/select')
    # 文件上传:
    # 点击文件上传按钮
    btn_up_file = (By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[14]/td[2]/span/div[1]/div/div/button')
    # 点击浏览文件输入文件内容
    btn_select_file = (By.XPATH, '//input[@type="file"]')
    # 点击确定按钮
    btn_enter_file = (By.XPATH, '/html/body/div[6]/div[1]/div[3]/span[1]/input')
    # 借款用途：
    select_loan_purpose = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[15]/td[2]/select')
    # 还款方式：
    select_repay_way = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[16]/td[2]/select')
    # 借款合同范本：
    select_loan_model_contract=(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[17]/td[2]/select')
    # 转让合同范本：
    select_transfer_model_contract=(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[18]/td[2]/select')
    # 借款金额：
    ipt_loan_account = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[19]/td[2]/input')
    # 借款保证金[第三方托管]：
    ipt_bond=(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[20]/td[2]/input')
    # 投标类型：
    select_bid_type = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[21]/td[2]/select')
    # 分成多少份
    ipt_bid_copies_num=(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[24]/td[2]/input')
    # 最高买多少份
    ipt_buy_max_count = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[25]/td[2]/input')
    # 借款期限
    # 数量
    ipt_repay_time_count = (By.XPATH, '//*[@id="repay_time"]')
    # 单位
    select_repay_time_type = (By.XPATH, '//*[@id="repay_time_type"]')
    # 年利率
    ipt_annual_rate = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[27]/td[2]/input')
    # 筹标期限：
    ipt_bid_deadline=(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[28]/td[2]/input')
    # 是否使用红包：
    select_use_red_bag = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[29]/td[2]/select')
    # 贷款描述：
    frame_loan_dec = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[30]/td[2]/div/div/div[2]/iframe')
    ipt_loan_dec =(By.XPATH, '/html/body')
    # 风险等级：
    # 贷款描述切换了 frame 下面切换回来
    frame_risk_level = frame_left
    select_risk_level = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[31]/td[2]/select')
    # 风险控制
    frame_risk_control = (By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[32]/td[2]/div/div/div[2]/iframe')
    ipt_risk_control = (By.XPATH, '/html/body')

    # 借款状态
    # 风险控制切换了 frame 下面切换回来
    frame_loan_status = frame_left
    ipt_loan_status = (By.XPATH, 'html/body/div[2]/form/table[1]/tbody/tr[33]/td[2]/label[1]')

    # 开始时间：选择时间
    js_fun = "function add_time(params){ console.log[arguments[0]] }"
    ipt_start_time = (By.XPATH, '//*[@id="start_time"]')
    js = 'arguments[0].value="2025-6-10 11:11:11"'

    # 排序：使用默认排序

    # 点击新增按钮：
    btn_enter_new_loan = (By.XPATH, '/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/input[4]')

    def new_loan(self):
        pass