from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from day01.utils import identify_code_img

# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()
# 通过驱动对象访问被测页面
driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login&')
# 页面最大化
driver.maximize_window()

# 获取验证码图片
driver.find_element(By.XPATH, '//*[@id="verify"]').screenshot("code_img.png")


# ○ 输入账号
el1 = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/input')
el1.send_keys('admin')
# ○ 输入密码
el2 = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]/input')
el2.send_keys('msjy123')
# ○ 输入验证码
el3 = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]/input')
el3.send_keys(identify_code_img())
# ○ 点击登录后台按钮
el4 = driver.find_element(By.XPATH, '//*[@id="login_btn"]')
el4.click()
# 获取登录信息
el5 = driver.find_element(By.XPATH, '//*[@id="login_msg"]')
sleep(1)
# 要等待之后才能打印出验证码错误的信息
# 验证码错误:实际结果的信息是一定的有效期，如果不能在有效期获取文本属性，那么输出空值
print(el5.text)
msg = el5.text

# 断言
# 因为是盗版课，不会登录成功...
# assert msg == "登录成功"
assert msg == "管理员密码错误"

# 等待 2s
sleep(2)
# 关闭驱动对象
driver.quit()