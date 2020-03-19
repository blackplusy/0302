#coding=utf-8
from selenium import  webdriver
import time
br=webdriver.Chrome()
'''
浏览器尺寸
br.set_window_size(480,800)
time.sleep(2)
br.get("http://localhost/ecshop")
time.sleep(2)
br.maximize_window()
time.sleep(2)
br.minimize_window()
'''
'''
浏览器的前进后退刷新
url1="https://www.baidu.com"
br.get(url1)
time.sleep(3)
url2="http://www.4399.com"
br.get(url2)
time.sleep(3)
br.back()
time.sleep(1)
br.forward()
time.sleep(1)
br.refresh()
'''
'''
截图和退出
br.get("https://www.baidu.com")
br.get_screenshot_as_file("D:\\abc.png")
br.quit()
'''
#切换句柄
br.get("http://192.168.7.247/1.html")
#点击文件中id是test1的标签
time.sleep(2)
br.find_element_by_id("test1").click()
#获取所有打开浏览器的窗口
windowstab=br.window_handles
print(windowstab)
#获取当前浏览器的窗口
currenttab=br.current_window_handle
print(currenttab)
br.switch_to.window(windowstab[1])
time.sleep(2)
br.switch_to.window(windowstab[0])





