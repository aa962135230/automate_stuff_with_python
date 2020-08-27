import time

for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(1)


for i in range(30):
    print('休眠第%d秒' % (i + 1))
    time.sleep(1)
