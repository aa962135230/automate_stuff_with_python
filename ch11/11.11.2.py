import os, sys, time, requests
from  selenium import webdriver

#从百度图片网站保存图片

os.makedirs('picture', exist_ok=True)

url = "https://image.baidu.com/"

browser = webdriver.Firefox()
browser.get(url)

#定位网页关键字输入框
keys_elem = browser.find_element_by_name('word')
#输入关键字
keys_elem.send_keys("test")
#提交查找表单
keys_elem.submit()

#休眠10s,让网页加载完毕
time.sleep(10)

#查找图像元素
img_elems = browser.find_elements_by_xpath('//div//ul//li//div//a/img')

img_count = 1;
for img_elem in img_elems[6:]:
    #获取图片的url地址,准备下载到本地
    print(img_elem.get_attribute('src'))
    res = requests.get(img_elem.get_attribute('src'))
    
    img_path = os.path.abspath('.') + os.sep +'picture' + os.sep + str(img_count) + '.jpg'
    # print(img_path)
    img_count += 1
    img_file = open(img_path, 'wb')
    for chunk in res.iter_content(100000):
        img_file.write(chunk)
    img_file.close()
browser.quit()
print(img_count)