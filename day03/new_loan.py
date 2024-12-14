# 1. 完成登录操作（保持登录状态）
# 使用已经登录的驱动，完成新增贷款页面的脚本设计
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from admin_login import driver

# 打开贷款管理页面(左边导航栏)

# 1. 由于页面结构嵌套子页面，需要进入子页面才能完成元素定位
frame1 = driver.find_element(By.XPATH, '/html/frameset/frame[1]') # 定位子页面元素
driver.switch_to.frame(frame1) # 切换子页面元素
# 2. 定位贷款管理元素
driver.find_element(By.XPATH, '//*[@id"navs"]/u1/1i[2]/a').click()

# 找到新增贷款按钮
# 1. 子页面与子页面之间不能直接进行跳转，需要返回原始主页面才能再次进行切换子页面
driver.switch_to.default_content() # 切回主页面
sleep(1)
frame2 = driver.find_element(By.XPATH, '//*[@id="main-frame"]') # 切换新增按钮的子页面中
driver.switch_to.frame(frame2)
# 2. 点击新增贷款按钮
driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/input[1]').click()

# 进入新增贷款页面
# 完成新增贷款页面的元素定位及操作(输入新增贷款需要的信息)
# 颜色
driver.find_element(By.XPATH, '//*[@id="colorpickerField"]').send_keys("3fd134")
sleep(1)

# 借款编号
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[3]/td[2]/input').clear().send_keys("MER2024113")
sleep(1)

# 贷款名称
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[4]/td[2]/input').send_keys("借款100w买东西")
sleep(1)

# 简短名称
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[5]/td[2]/input').send_keys("借款100w")
sleep(1)

# 会员名称
driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[6]/td[2]/input[1]').send_keys("Thw")
sleep(1)
# 选择后台会员（xpath 会变化）
# 如果 xpath 变化了，除了重新复制xpath然后修改代码，还有更好的方式：通过手写 xpath 的方式来进行具体元素的定位
# 手写的 xpath ：//strong[text()="Thw"]
driver.find_element(By.XPATH, '//strong[text()="Thw"]').click()
# 复制的 xpath
# driver.find_element(By.XPATH, '/html/body/div[5]/ul/li/strong').click()
sleep(1)

# 所在城市
driver.find_element(By.XPATH, '//*[@id="citys_box"]/div[1]/div[2]/input[3]').send_keys("3fd134")
sleep(1)

# 分类：
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[8]/td[2]/select')
select1 = Select(sl1)
select1.select_by_value("4")
sleep(1)

# 担保机构：
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[9]/td[2]/select')
select1 = Select(sl1)
select1.select_by_index(2)
sleep(1)

# 担保范围：
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[10]/td[2]/select')
select1 = Select(sl1)
select1.select_by_visible_text("无")
sleep(1)

# 文件上传:
# 点击文件上传按钮
driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[14]/td[2]/span/div[1]/div/div/button').click()
sleep(1)
# 点击本地上传按钮         原本：'/html/body/div[5]/div[1]/div[2]/div/div[1]/ul/li[2]'
driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[2]/div/div[1]/ul/li[2]').click()
sleep(1)
# 点击浏览文件输入文件内容  原本：'/html/body/div[5]/div[1]/div[2]/div/div[3]/form/div/div/div/input'
# 复制的 xpath：'/html/body/div[6]/div[1]/div[2]/div/div[3]/form/div/div/div/input'
# driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[2]/div/div[3]/form/div/div/div/input').send_keys("./code_img.png")
# 手写的 xpath：'//input[@type="file"]'
driver.find_element(By.XPATH,'//input[@type="file"]').send_keys("./code_img.png")
sleep(1)
# 点击确定按钮            原本：'/html/body/div[5]/div[1]/div[3]/span[1]/input'
driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[3]/span[1]/input').click()
sleep(1)

# 借款用途：
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[15]/td[2]/select')
select1 = Select(sl1)
select1.select_by_visible_text("个人消费")
sleep(1)

# 还款方式：
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[16]/td[2]/select')
select1 = Select(sl1)
select1.select_by_visible_text("本金均摊，利息固定")
sleep(1)

# 借款合同范本：
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[17]/td[2]/select')
select1 = Select(sl1)
select1.select_by_visible_text("天天赢合作操盘协议")
sleep(1)

# 转让合同范本：
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[18]/td[2]/select')
select1 = Select(sl1)
select1.select_by_visible_text("周周盈合作操盘协议")
sleep(1)

# 借款金额：
el1 = driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[19]/td[2]/input')
el1.click()
el1.send_keys("1000000")
sleep(1)

# 借款保证金[第三方托管]：
el1 = driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[20]/td[2]/input')
el1.click()
el1.send_keys("100000")
sleep(1)

# 投标类型：
sl1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[21]/td[2]/select')
select1 = Select(sl1)
select1.select_by_visible_text("按份额")
sleep(1)

# 分成多少份
el1 = driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[24]/td[2]/input')
el1.click()
el1.send_keys("100")
sleep(1)

# 最高买多少份
el1 = driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[25]/td[2]/input')
el1.click()
el1.send_keys("10")
sleep(1)

# 借款期限
# 数量
el1 = driver.find_element(By.XPATH,'//*[@id="repay_time"]')
el1.click()
el1.send_keys("365")
sleep(1)
# 单位
sl1 = driver.find_element(By.XPATH, '//*[@id="repay_time_type"]')
select1 = Select(sl1)
select1.select_by_visible_text("天")
sleep(1)

# 年利率
driver.find_element(By.XPATH,'/html/body/div[21/form/table[11/tbody/tr[271/td[21/input').send_keys("8")
sleep(1)

# 筹标期限：
driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[28]/td[2]/input').send_keys("30")
sleep(1)

# 是否使用红包：
sl1 = driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[29]/td[2]/select')
select1 = Select(sl1)
select1.select_by_visible_text("否")
sleep(1)

# 贷款描述：
frame1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[30]/td[2]/div/div/div[2]/iframe')
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH,'/html/body').send_keys("买车！")
sleep(1)

# 风险等级：
# 贷款描述切换了 frame 下面切换回来
driver.switch_to.default_content()
frame2 = driver.find_element(By.XPATH, '//*[@id="main-frame"]')
driver.switch_to.frame(frame2)
sl1 = driver.find_element(By.XPATH,'/html/body/div[2]/form/table[1]/tbody/tr[31]/td[2]/select')
select1 = Select(sl1)
select1.select_by_visible_text("中")
sleep(1)

# 风险控制
frame1 = driver.find_element(By.XPATH, '/html/body/div[2]/form/table[1]/tbody/tr[32]/td[2]/div/div/div[2]/iframe')
driver.switch_to.frame(frame1)
driver.find_element(By.XPATH,'/html/body').send_keys("没有风险！")
sleep(1)

# 借款状态
# 风险控制切换了 frame 下面切换回来
driver.switch_to.default_content()
frame2 = driver.find_element(By.XPATH, '//*[@id="main-frame"]')
driver.switch_to.frame(frame2)
driver.find_element(By.XPATH,'html/body/div[2]/form/table[1]/tbody/tr[33]/td[2]/label[1]').click()
sleep(1)
# 开始时间：选择时间
# 由于该元素比较特殊，需要通过js脚本进行强制输入完成
# 首先必须通过xpath 获取时间值，然后进行强制修改
# 定义一个js脚本然后用来接收时间值，进行修改
js_fun="function add_time(params){ console.log[arguments[0]] }"
driver.execute_script(js_fun)
el1=driver.find_element(By.XPATH,'//*[@id="start_time"]')
# 通过脚本输入内容
js='arguments[0].value="2025-6-10 11:11:11"'
driver.execute_script(js,el1)

# 排序：使用默认排序

# 点击新增按钮：
driver.find_element(By.XPATH,'/html/body/div[2]/form/table[6]/tbody/tr[2]/td[2]/input[4]').click()


driver.close()


# 请填写会员名称 弹框点击操作
# driver.switch_to.alert.accept()

# 一般在做 web 自动化过程中，经常会使用 input 内建函数进行调试
# 让程序挂起，比如代码报错前面添加上 input 调试，那么就可以看到当前页面属于的状态，以及元素具体的值，然后进行调试
# 由于在做 web 自动化过程中，程序一旦报错，页面会直接关闭，所以不方便调试，就会用input 使程序进入挂起状态
# input("程序挂起开启调试，按回车继续执行")