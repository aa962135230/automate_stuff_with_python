from selenium import webdriver
browser = webdriver.Firefox()

browser.get('http://inventwithpython.com')
link_elem = browser.find_element_by_link_text('Read Online for Free')
print(type(link_elem))
link_elem.click()