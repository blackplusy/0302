#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
br=webdriver.Chrome()
# br.get("https://www.baidu.com")
# element=br.find_element_by_link_text("设置")
#perform代表执行的意思
#1.单击元素
# ActionChains(br).click(element).perform()
#2.元素上面按下左键不放
# ActionChains(br).click_and_hold(element).perform()
#3.右键元素
# ActionChains(br).context_click(element).perform()
#4.双击元素
# ActionChains(br).double_click(element).perform()
#5.拖拽
br.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
br.maximize_window()
br.switch_to.frame("iframeResult")
source=br.find_element_by_id("draggable")
target=br.find_element_by_id("droppable")
actions=ActionChains(br)
actions.drag_and_drop(source,target)
actions.perform()

