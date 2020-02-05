
from selenium import webdriver
import time
drive = webdriver.Chrome(executable_path='./chromedriver.exe')
time.sleep(2)
url = 'https://www.jd.com/'
drive.get(url)
# 1. 获取输入 输入关键字
key_button = drive.find_element_by_css_selector('#key')
key_button.clear()
key_button.send_keys('固态')
# 2. 点击搜索 #search button.button
click_button = drive.find_element_by_css_selector('#search button.button')
click_button.click()
# 阻塞之后 在浏览器中进行
print(drive.get_cookies())
input()
# selenium 开发简单

# 爬虫 爬取数据   采集数据
# selenium 自动化 模拟人为操作
# cookie

drive.quit()
