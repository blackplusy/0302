#coding=utf-8
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
br=webdriver.Chrome()
#打开浏览器
br.get("https://www.baidu.com")
time.sleep(3)
#搜索框中输入内容
br.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)
#搜索框中输入空格
br.find_element_by_id("kw").send_keys(Keys.SPACE)
time.sleep(3)
#搜索框中输入空格
br.find_element_by_id("kw").send_keys("python")
time.sleep(3)
#输入回车
br.find_element_by_id("kw").send_keys(Keys.ENTER)
time.sleep(3)
#组合按键 ctl+a全选
br.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(2)
#组合按键 ctl+x剪切
br.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(2)
#组合按键ctl+v
br.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(2)
br.find_element_by_id("kw").send_keys(Keys.ENTER)
