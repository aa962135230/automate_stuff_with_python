from selenium import webdriver
import time

browser = webdriver.Firefox()
account = "****"
password = "****"

#因gmail被墙,改用163邮件做示例
browser.get('https://mail.163.com/')
time.sleep(5)
print("sleep end")
browser.switch_to.frame(browser.find_element_by_xpath('//div[@id="loginDiv"]/iframe'))
# browser.switch_to.frame(browser.find_element_by_xpath('//div[@id="loginDiv"]/iframe'))

email_elem = browser.find_element_by_name('email')

email_elem.send_keys('wanggaozhi1992')
password_elem = browser.find_element_by_name('password')
password_elem.send_keys('gaozhi1992')

browser.find_element_by_id('dologin').click()
time.sleep(10)
browser.quit()

