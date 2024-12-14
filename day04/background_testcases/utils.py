import json

import requests


def identify_code_img():
    # 通过老鹰网识别图片 开发文档：https://www.chaojiying.com/api-5.html
    url = "https://upload.chaojiying.net/Upload/Processing.php"
    # 设置请求参数
    data = {
        "user": "tanhaowei",
        "pass": "tanhaowei849849X",
        "softid": "965865",
        "codetype": 1902,
    }

    files = {"userfile": open("code_img.png", "rb")}

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
    with open("./cookies.json", "w") as f:
        f.write(json.dumps(cookies))

def load_cookies(driver):
    # 当页面没有 cookie 信息时，需要先正常登录然后再保持 cookie
    # 在下次页面进行访问的时候再使用 cookie 信息
    try:
        # 将保存在本地的 cookie 信息读取出来并使用
        with open("./cookies.json", "r") as f:
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
    # 通过判断页面的标题来确定是否登录成功
    print(driver.title)
    if "管理员登录"  in driver.title:
        print("载入的 cookie 信息无效或者过期，通过输入账号密码验证码登录")
        return False
    else:
        print("已登录")
        return True