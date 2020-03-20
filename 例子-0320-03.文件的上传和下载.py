#coding=utf-8
from selenium import  webdriver
import time
browser=webdriver.Chrome()
#文件的上传
# browser.get("http://192.168.7.247/ecshop/admin")
#
# browser.find_element_by_name("username").send_keys("admin")
# browser.find_element_by_name("password").send_keys("admin888")
# browser.find_element_by_class_name("btn-a").click()
# time.sleep(3)
# browser.switch_to.frame("menu-frame")
# browser.find_element_by_link_text("添加新商品").click()
# browser.switch_to.default_content()
# time.sleep(3)
# browser.switch_to.frame("main-frame")
# time.sleep(3)
# browser.find_element_by_name("goods_name").clear()
# browser.find_element_by_name("goods_name").send_keys("aaa12")
# time.sleep(3)
# browser.find_element_by_name("cat_id").send_keys("大家电")
# browser.find_element_by_name("shop_price").send_keys("800")
# browser.find_element_by_name("goods_img").send_keys("D:\\abc.png")
# time.sleep(5)
# browser.find_element_by_xpath("//*[@value=' 确定 ']").click()
#文件的下载
browser.get("https://pypi.org/project/selenium/3.6.0/#files")
browser.find_element_by_link_text("selenium-3.6.0.tar.gz").click()
time.sleep(10)
print('ok')