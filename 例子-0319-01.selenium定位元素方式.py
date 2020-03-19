#coding=utf-8
#导入selenium模块
from selenium import webdriver
#驱动设置为chrome
br=webdriver.Chrome()
#通过驱动打开网页
# br.get("https://www.baidu.com")
br.get("https://www.taobao.com")
br.find_element_by_id("q").clear()
br.find_element_by_id("q").send_keys("nike")
br.find_element_by_class_name("btn-search").click()
#1.通过id定位
# br.find_element_by_id('kw').send_keys("55开")
# br.find_element_by_id('su').click()
#2.通过name定位
# br.find_element_by_name('wd').send_keys("巧碧螺")
# br.find_element_by_id('su').click()
#3.通过class定位
# br.find_element_by_class_name('s_ipt').send_keys("醉叮当")
# br.find_element_by_id('su').click()
#4.tag定位
#br.find_element_by_tag_name("input").send_keys("aaa")
#5.通过link定位
# br.find_element_by_link_text("新闻").click()
#6.通过partial_link定位
# br.find_element_by_partial_link_text('闻').click()
#7.xpath定位
# br.find_element_by_xpath("//*[@id='kw']").send_keys("虎牙醉叮当")
# br.find_element_by_id('su').click()
#8.css定位
br.find_element_by_css_selector("#kw").send_keys("哎！~")
br.find_element_by_id('su').click()
