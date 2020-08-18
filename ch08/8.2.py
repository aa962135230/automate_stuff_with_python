import os
print('****8.2.1****')
#在automate_stuff_with_python文件夹下执行该程序
hello_file = open(os.path.abspath('./ch08/file/hello.txt'))

print('****8.2.2****')
hello_content = hello_file.read()
hello_file.close()
print(hello_content)

sonnet_file = open(os.path.abspath('./ch08/file/sonnet29.txt'))
print(sonnet_file.readlines())
sonnet_file.close()

print('****8.2.3****')

if os.path.exists(os.path.abspath('./ch08/file/bacon.txt')):
    os.unlink(os.path.abspath('./ch08/file/bacon.txt'))

bacon_file = open(os.path.abspath('./ch08/file/bacon.txt'), 'w')
bacon_file.write('Hello world: \n')
bacon_file.close()

bacon_file = open(os.path.abspath('./ch08/file/bacon.txt'), 'a')
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()

bacon_file = open(os.path.abspath('./ch08/file/bacon.txt'))
content = bacon_file.read()
bacon_file.close()
print(content)


