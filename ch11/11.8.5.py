from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('http://nostarch.com')
# browser.get('https://mail.163.com/')

time.sleep(10)
print("sleep end")

html_file = browser.find_element_by_tag_name('html')

html_file.send_keys(Keys.END)
time.sleep(10)
html_file.send_keys(Keys.HOME)
time.sleep(10)
browser.quit()
