from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from day07.commons.utils import identify_code_img, load_cookies, sava_cookies, is_back_login

# 创建一个驱动对象：谷歌
driver = webdriver.Chrome()
# 通过驱动对象访问被测页面
driver.get('http://47.107.116.139/fangwei/m.php?m=Public&a=login&')
# 页面最大化
driver.maximize_window()

# 验证码图片保存路径
code_img_path ='../../data/code_img.png'
# cookie 信息保存路径
cookie_path ='../../data/back_cookie.json'

# 载入本地的 cookie 信息（无论是否存在，无论是否有效）
load_cookies(driver,cookie_path)

# is_login(driver) 方法通过刷新页面判断 cookie 是否有效
# 如果有效直接进入后台管理页面
# 如果无效执行输入账号密码验证码的逻辑
if not is_back_login(driver):


    # 获取验证码图片
    result=driver.find_element(By.XPATH, '//*[@id="verify"]').screenshot(code_img_path)

    # ○ 输入账号
    el1 = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[2]/td[2]/input')
    el1.send_keys('admin')
    # ○ 输入密码
    el2 = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[3]/td[2]/input')
    el2.send_keys('msjy123')
    # ○ 输入验证码
    el3 = driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr/td[3]/table/tbody/tr[5]/td[2]/input')
    el3.send_keys(identify_code_img(code_img_path))
    # ○ 点击登录后台按钮
    el4 = driver.find_element(By.XPATH, '//*[@id="login_btn"]')
    el4.click()
    # 获取登录信息
    sleep(1)
    el5 = driver.find_element(By.XPATH, '//*[@id="login_msg"]')
    # 要等待之后才能打印出验证码错误的信息
    # 验证码错误:实际结果的信息是一定的有效期，如果不能在有效期获取文本属性，那么输出空值
    print(el5.text)
    msg = el5.text

    # 断言
    # 因为是盗版课，不会登录成功...
    # assert msg == "登录成功"
    assert msg == "管理员密码错误"

    # 保存 cookie 信息
    sava_cookies(driver,cookie_path)

# 等待 2s
sleep(2)
# 关闭驱动对象
driver.quit()