from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from day08.commons.utils import identify_code_img, load_cookies, sava_cookies, is_front_login

# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()
# 通过驱动对象访问被测页面
driver.get('http://47.107.116.139/fangwei/')
# 页面最大化
driver.maximize_window()

# 验证码图片保存路径
code_img_path ='../../data/code_img.png'
# cookie 信息保存路径
cookie_path ='../../data/front_cookie.json'

# 载入本地的 cookie 信息（无论是否存在，无论是否有效）
load_cookies(driver,cookie_path)

# is_login(driver) 方法通过刷新页面判断 cookie 是否有效
# 如果有效直接进入功能页面
# 如果无效执行输入账号密码验证码的逻辑
if not is_front_login(driver):

    # ○ 点击登录按钮
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/div/a').click()
    # ○ 输入账号
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="login-email-address"]').send_keys("tanhaowei")
    # ○ 输入密码
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys("msjy123")
    # 获取验证码图片
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="Jverify_img"]').screenshot(code_img_path)
    # ○ 输入验证码
    el3 = driver.find_element(By.XPATH, '//*[@id="Jverify"]')
    el3.send_keys(identify_code_img(code_img_path))

    # ○ 点击记住我
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="ajax_login_form"]/div/ul/li[4]/label').click()
    # ○ 点击登录按钮
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="ajax-login-submit"]').click()
    # 获取登录信息
    sleep(1)
    # 正例
    msg = driver.find_element(By.XPATH, '//*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[2]').text
    assert msg == "用户不存在"
    driver.find_element(By.XPATH, '//*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()
    # 反例：密码错误
    # 当获取提示框信息时，正反例的 xpath 值的ID属性不一致
    # 解决方式：1.直接替换 2.手写 xpath 保持一致
    # msg = driver.find_element(By.XPATH, '//*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[2]').text
    # assert msg == "密码错误"
    # driver.find_element(By.XPATH, '//*[@id="fanwe_error_box"]/table/tbody/tr/td[2]/div[3]/input[1]').click()

    # 保存 cookie 信息
    sava_cookies(driver,cookie_path)

# 等待 2s
sleep(2)
# 关闭驱动对象
driver.quit()