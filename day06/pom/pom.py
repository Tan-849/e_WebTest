# 封装前台登录页面类
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import day06.utils as utils

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
                    return msg
                else:
                    return True
            else:
                return True
        # 一旦调用重写的 find_element 方法，那么先触发显式等待
        self.wait(f)

        # 触发完显示等待之后，使用原生的 find_element() 定位元素
        return self.driver.find_element(by, value)


class FrontLoginPage(BasePage):

    # 将页面中所有需要被操作的元素定义为类属性
    # 登录
    # 点击登录按钮
    btn_login = (By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/a')
    # 输入账号
    ipt_username = (By.XPATH, '//*[@id="login-email-address"]')
    # 输入密码
    ipt_password = (By.XPATH, '//*[@id="login-password"]')
    # 点击登录
    btn_login_submit = (By.XPATH, '//*[@id="ajax-login-submit"]')
    # 点击提示框信息确认
    login_msg = (By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]')
    # 提示登录成功的按钮
    btn_login_ok = (By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]')

    # 投标
    # ● 点击马上投标按钮
    btn_deal_submit = (By.XPATH, '/html/body/div[7]/div[2]/div[1]/div[1]/ul/li[1]/span[6]/a/span')
    # ● 点击立即投资
    btn_bid = (By.XPATH, '//*[@id="tz_link"]')
    # ● 输入支付密码
    ipt_pay_password = (By.XPATH, '//*[@id="J_bid_password"]')
    # ● 点击确定按钮
    btn_pay_submit = (By.XPATH, '//*[@id="J bindpassword_btn"]')
    # ● 关闭提示信息弹框 获取提示信息的实际结果断言预期结果
    pay_msg = (By.XPATH, '//[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]')
    txt_deal_msg = (By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]')

    # 定义测试用例
    # 1. 登录前台
    def login(self,username,password):
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

        return msg

    # 2. 新增投标
    def new_loan_bid(self,pay_passwd):
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

    def login(self,username,password):
        # 获取验证码图片
        self.find_element(*self.img_code).screenshot("code_img.png")

        # ○ 输入账号
        self.find_element(*self.ipt_username).send_keys(username)
        # ○ 输入密码
        self.find_element(*self.ipt_password).send_keys(password)
        # ○ 输入验证码
        self.find_element(*self.ipt_code).send_keys(utils.identify_code_img())
        # ○ 点击登录后台按钮
        self.find_element(*self.btn_login_submit).click()
        # ○ 获取登录信息
        msg = self.find_element(*self.login_msg,need_text=True).text

        # 保存 cookie 信息
        utils.sava_cookies(self.driver)

        return msg


class NewLoan:
    pass


# 当前项目需要进行自动化测试的页面或者流程用例有多少个，那么就定义多少个类