import pytest
from selenium import webdriver

from day06.pom.pom import FrontLoginPage


# 通过fixture实现前后置的处理
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    # driver.get(url)
    # driver.maximize_window()
    return driver


# 定义让前台页面保持自动登录的 fixture
@pytest.fixture(scope='session')
def user_driver():
    driver = webdriver.Chrome()
    driver.get('http://47.187.116.139/fangwei')
    driver.maximize_window()
    page = FrontLoginPage(driver)
    # 通过页面类对象调用方法执行测试用例
    msg = page.login("admin", "msjy123")
    # 断言
    print(msg)
    assert msg == "成功登录"

    return driver


@pytest.fixture
def clear_new_loan_bid_page(user_driver):
    user_driver.get('http://47.107.116.139/fangwei')
