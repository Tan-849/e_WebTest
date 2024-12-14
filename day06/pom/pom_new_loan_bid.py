from selenium.webdriver import Chrome
from day06.pom import FrontLoginPage

driver = Chrome()
driver.get("http://47.187.116.139/fangwei")
driver.maximize_window()

# 实例化一个页面类对象：page
page = FrontLoginPage(driver)

# 通过页面对象调用实例方法去执行测试用例
# 用例执行完成后获取实际结果
# 1. 登录前台
msg = page.login("admin","msjy123")
# 断言返回的结果
assert msg == "成功登录"

# 2. 新增投标
msg = page.new_loan_bid("msjy123")
assert msg == "投标成功"

driver.quit()
