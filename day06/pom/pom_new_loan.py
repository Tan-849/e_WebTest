from selenium.webdriver import Chrome
from day06.pom import BackgroundLoginPage

driver = Chrome()
driver.get("http://47.107.116.139/fangwei/m.php?m=Public&a=login&")
driver.maximize_window()


page=BackgroundLoginPage(driver)

msg = page.login("admin","123456")
print(msg)