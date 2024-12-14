# 使用封装的页面类进行用例的执行
from time import sleep
from day07.commons.pom import FrontLoginPage, BackgroundLoginPage, NewLoanPage


def test_user_login_ok(driver):
    # 测试用例初始化：打开浏览器（后期封装到固件里）
    driver.get('http://47.187.116.139/fangwei')
    driver.maximize_window()

    # 1. 登录用例执行
    # 创建页面类对象
    page = BackgroundLoginPage(driver)
    # 通过页面类对象调用方法执行测试用例
    msg = page.login("admin", "msjy123")
    # 断言
    print(msg)
    assert msg == "管理员密码错误"

def test_user_login_fail(driver):
    # 测试用例初始化：打开浏览器（后期封装到固件里）
    driver.get('http://47.187.116.139/fangwei')
    driver.maximize_window()

    # 1. 登录用例执行
    # 创建页面类对象
    page = BackgroundLoginPage(driver)
    # 通过页面类对象调用方法执行测试用例
    msg = page.login("fsdfasfc", "fsdfsaf")
    # 断言
    print(msg)
    assert msg == "管理员密码错误"


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


def test_admin_login_ok(driver):
    # 测试用例初始化：打开浏览器（后期封装到固件里）
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
    sleep(1)
    # assert msg == " "

def test_admin_login_fail(driver):
    # 测试用例初始化：打开浏览器（后期封装到固件里）
    driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login&')
    driver.maximize_window()

    # 1. 登录用例执行
    # 创建页面类对象
    page = BackgroundLoginPage(driver)
    # 通过页面类对象调用方法执行测试用例
    msg = page.login("dfacsadfasdfcs", "fscascqwfdcsdcqw")
    # 断言
    print(msg)
    assert msg == "管理员账号错误"
    sleep(1)

    # assert msg == " "

def test_new_loan(admin_driver):
    page = NewLoanPage()
    page.new_loan()