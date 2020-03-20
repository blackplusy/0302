#coding=utf-8
from selenium import  webdriver
from selenium.webdriver.support.select import Select
br=webdriver.Chrome()

# br.get("http://127.0.0.1/11.html")
#1.通过send_keys
#bbb是options中内容
# br.find_element_by_id("select").send_keys("bbb")
#2.通过二次操作
# br.find_element_by_id("select").find_element_by_xpath("//option[@value='30']").click()
br.get("http://127.0.0.1/12.html")
#实例化select类对象
selector=Select(br.find_element_by_id("selectdemo"))
#1.通过index索引进行选择，索引从0开始
# selector.select_by_index("2")
#2.通过value值进行选择
# selector.select_by_value("210103")
#3.通过标签显示的text进行选择
selector.select_by_visible_text("乒乓球员")

