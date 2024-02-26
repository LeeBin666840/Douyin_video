"""
-*- coding: utf-8 -*-
@Time    : 2023/10/18 14:35
@Author  : 无言
@FileName: 超级鹰点选.py
@Software: PyCharm
"""
from selenium import webdriver
import time
from chaojiying import Chaojiying_Client
from info import account,password
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
driver.get('https://www.douyin.com/user/MS4wLjABAAAAEVF2BDh0uaFuyksZLnKNgHnctLqeA6LuwI8gGyPLBMI?vid=7284166744086711586')
# driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(2)
'''获取验证码元素'''
img_label=driver.find_element_by_css_selector('.captcha_verify_container')
# 截图保存验证码图片
img_label.screenshot('yzm.png')
'''识别验证码图片，获取文字坐标轴'''
chaojiying=Chaojiying_Client(account,password,'96001')
# 读取验证码图片
img=open('yzm.png','rb').read()
# 识别验证码图片
result=chaojiying.PostPic(img,9004)['pic_str']
for res in result.split('|'):
    x=res.split(',')[0]
    y=res.split(',')[1]
    print(x,y)
    ActionChains(driver).move_to_element_with_offset(img_label,int(x),int(y)).click().perform()

driver.find_element_by_css_selector('.verify-captcha-submit-button').click()
driver.implicitly_wait(10)
time.sleep(1)
driver.find_element_by_css_selector('.dy-account-close').click()
driver.implicitly_wait(10)
# 往下滑保证所有数据都加载出来
def main():
    for i in range(1, 100, 5):
        # 死等
        time.sleep(1)
        j = i / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)  # 执行我们js的语法
main()
time.sleep(5)
driver.quit()