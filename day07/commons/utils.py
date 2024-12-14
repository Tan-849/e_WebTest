import json

import requests
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def identify_code_img(code_img_path):
    # 通过老鹰网识别图片 开发文档：https://www.chaojiying.com/api-5.html
    url = "https://upload.chaojiying.net/Upload/Processing.php"
    # 设置请求参数
    data = {
        "user": "tanhaowei",
        "pass": "tanhaowei849849X",
        "softid": "965865",
        "codetype": 1902,
    }

    files = {"userfile": open(code_img_path, "rb")}

    res = requests.post(url, data=data, files=files)
    res_json = res.json()

    if res_json["err_no"] == 0:
        code_img = res_json["pic_str"]
        print(f"识别成功，验证码为：{code_img}")
    else:
        print("识别失败")

    return code_img

def sava_cookies(driver):
    # 将获取到的 cookie 信息保存再本地文件
    cookies = driver.get_cookies()
    with open("cookies.json", "w") as f:
        f.write(json.dumps(cookies))

def load_cookies(driver):
    # 当页面没有 cookie 信息时，需要先正常登录然后再保持 cookie
    # 在下次页面进行访问的时候再使用 cookie 信息
    try:
        # 将保存在本地的 cookie 信息读取出来并使用
        with open("cookies.json", "r") as f:
            cookies = json.loads(f.read())
            for cookie in cookies:
                # 读取json文件里面所有的 cookie 信息
                driver.add_cookie(cookie)
            else:
                # 添加所有 cookie 信息完成之后 刷新页面
                driver.refresh()
    except Exception as e:
        print(f"目前本地不存在 cookie 信息，需要输入账号密码登录以获取有效 cookie 信息：{e}")

def is_login(driver):
    # 根据元素【立即登录】是否存在来判断登录状态
    driver.refresh()
    try:
        driver.find_element(By.XPATH,'//*[@id="user_head_tip"]/a[1]')
    except NoSuchElementException as e1:
        print("已登录")
        return True
    except Exception as e2:
        print(f"出现意料之外的异常：{e2}")
    else:
        print(f"cookie 信息不存在或已失效，输入账号密码验证码进行登录")
        return False

