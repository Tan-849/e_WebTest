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

    files = {"userfile": open("./code_img.png", "rb")}

    res = requests.post(url, data=data, files=files)
    res_json = res.json()

    if res_json["err_no"] == 0:
        code_img = res_json["pic_str"]
        print(f"识别成功，验证码为：{code_img}")
    else:
        print("识别失败")

    return code_img