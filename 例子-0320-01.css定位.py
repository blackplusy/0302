#coding=utf-8
from selenium import webdriver

br=webdriver.Chrome()

br.get("https://www.baidu.com")
#单一属性定位
# br.find_element_by_css_selector("input").send_keys("abc")

# br.find_element_by_css_selector("#kw").send_keys("黑哥GaGa")

# br.find_element_by_css_selector(".s_ipt").send_keys("葫芦娃！")

# br.find_element_by_css_selector("[name='wd']").send_keys("意大利疫情")

# br.find_element_by_css_selector("[autocomplete='off']").send_keys("taobao")

#组合属性定位
# br.find_element_by_css_selector("input#kw").send_keys("不戴口罩")

# br.find_element_by_css_selector("input.s_ipt").send_keys("钟南山")

# br.find_element_by_css_selector("input[name='wd']").send_keys("方舟子")

# br.find_element_by_css_selector("input[maxlength]").send_keys("123")

# br.find_element_by_css_selector("[name='wd'][autocomplete='off']").send_keys("aaa")

# br.find_element_by_css_selector("input[class^='bg']").click()
