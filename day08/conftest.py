import pytest
from day07.commons.driver import get_webdriver
from day07.commons.pom import FrontLoginPage,BackgroundLoginPage


# 通过fixture实现前后置的处理
@pytest.fixture(scope='session',autouse=False)
def driver():
    return get_webdriver()

# 定义让前台页面保持自动登录的 fixture
@pytest.fixture(autouse=False)
def user_driver(driver):
    driver.get('http://47.187.116.139/fangwei')
    driver.maximize_window()
    page = FrontLoginPage(driver)
    # 通过页面类对象调用方法执行测试用例
    msg = page.login("admin", "msjy123")
    # 断言
    print(msg)
    assert msg == "成功登录"

    return driver


@pytest.fixture(autouse=False)
def clear_new_loan_bid_page(user_driver):
    user_driver.get('http://47.107.116.139/fangwei')


# 定义让后台页面保持自动登录的 fixture
@pytest.fixture(autouse=False)
def admin_driver(driver):
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
    # assert msg == "管理员密码错误"
    assert msg == " "