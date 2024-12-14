from selenium.webdriver.common.by import By

# 1. 完成登录操作（保持登录状态）
# 使用已经登录的驱动，完成新增贷款页面的脚本设计
from frontend_login import driver

# 2. 新增投标
# ● 点击马上投标按钮
driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[1]/div[1]/ul/li[1]/span[6]/a/span').click()
# ● 点击立即投资
driver.find_element(By.XPATH, '//*[@id="tz_link"]').click()

# ● 输入支付密码
# 正例
driver.find_element(By.XPATH, '//*[@id="J_bid_password"]').send_keys("msjy123")
# 反例
# driver.find_element(By.XPATH, '//*[@id="J_bid_password"]').send_keys("1234")

# ● 点击确定按钮
driver.find_element(By.XPATH, '//*[@id="J bindpassword_btn"]').click()
# 获取提示信息的实际结果断言预期结果
# 正例
msg = driver.find_element(By.XPATH, '//[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[2]').click()
assert msg == "投标成功"
driver.find_element(By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()
# 反例
# msg = driver.find_element(By.XPATH, '//[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[2]').click()
# assert msg == "支付密码错误"
# driver.find_element(By.XPATH, '//*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()
# ● 关闭提示信息弹框
driver.find_element(By.XPATH, '//*[@id="fanwe_success_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()