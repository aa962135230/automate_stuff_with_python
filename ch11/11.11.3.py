from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
url = 'https://gabrielecirulli.github.io/2048'
browser.get(url)
#网站打开较慢,休眠等待网页完全加载
time.sleep(20)
game_elem = browser.find_element_by_tag_name('html')

for i in range(10):
    game_elem.send_keys(Keys.UP)
    time.sleep(0.5)
    game_elem.send_keys(Keys.RIGHT)
    time.sleep(0.5)
    game_elem.send_keys(Keys.DOWN)
    time.sleep(0.5)
    game_elem.send_keys(Keys.LEFT)
    time.sleep(0.5)
browser.quit()



