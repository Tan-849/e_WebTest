# 使用封装的页面类进行用例的执行
import pytest
from selenium import webdriver

from day06.pom.pom import FrontLoginPage, BackgroundLoginPage


def test_user_new_loan_bid_ok(user_driver,clear_new_loan_bid_page):
    page = FrontLoginPage(user_driver)
    # 2. 贷款投标用例执行
    msg = page.new_loan_bid("123456")
    print(msg)
    assert msg == "投标成功"

def test_user_new_loan_bid_fail(user_driver,clear_new_loan_bid_page):
    page = FrontLoginPage(user_driver)
    # 2. 贷款投标用例执行
    msg = page.new_loan_bid("xxxxx")
    print(msg)
    assert msg == "支付密码错误"


# 以 pytest 默认用例格式来定义用例
# 函数用例为主
# def test_user_login(driver):
#     driver.get('http://47.187.116.139/fangwei')
#     driver.maximize_window()
#
#     # 执行测试用例
#
#     # 1. 登录用例执行
#     # 创建页面类对象
#     page = FrontLoginPage(driver)
#     # 通过页面类对象调用方法执行测试用例
#     msg = page.login("admin", "msjy123")
#     # 断言
#     print(msg)
#     assert msg == "成功登录"
#
#     # 2. 贷款投标用例执行
#     msg = page.new_loan_bid("123456")
#     print(msg)
#     assert msg == "投标成功"


def test_admin_login(driver):
    # 测试用例初始化：打开浏览器（后期封装到固件里）
    driver = webdriver.Chrome()
    driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login&')
    driver.maximize_window()

    # 1. 登录用例执行
    # 创建页面类对象
    page = BackgroundLoginPage(driver)
    # 通过页面类对象调用方法执行测试用例
    msg = page.login("admin", "msjy123")
    # 断言
    print(msg)
    assert msg == "管理员密码错误"
