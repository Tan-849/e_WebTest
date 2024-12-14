from selenium.webdriver import Chrome, Firefox, Edge, Safari, Ie

# 自定义函数获取对应的浏览器驱动
def get_webdriver(name:str="Chrome"):
    # 根据调用获取浏览器的实参来返回对应的驱动
    # 将具体浏览器实参名字进行整理
    # 将所有浏览器的名字转化成小写
    # 将所有浏览器的名字中的空格去除
    # 再返回驱动
    name=name.lower()
    name=name.replace(" ","")
    match name:
        case "chrome":
            return Chrome()
        case "firefox":
            return Firefox()
        case "ie":
            return Ie()
        case "safari":
            return Safari()
        case "edge":
            return Edge()
