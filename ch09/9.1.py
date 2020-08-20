import shutil, os

#本段代码最好在与本文件同级目录下执行
print('****9.1.1****')
print(os.path.abspath('.'))
shutil.copy('spam.txt', os.path.abspath('.') + '/file')

shutil.copy('eggs.txt', os.path.abspath('.') + '/file')

if not os.path.exists(os.path.abspath('.') + '/fileback'):
    shutil.copytree(os.path.abspath('.') + '/file', os.path.abspath('.') + '/fileback')

print('****9.1.2****')
shutil.move(os.path.abspath('.') + '/file/eggs.txt', os.path.abspath('.') + '/file/eggs_move.txt')


print('****9.1.3****')
for file_name in os.listdir():
    if file_name.endswith('.txt'):
        print(file_name)
        # os.unlink(file_name)

print('****9.1.4****')
import send2trash
bacon_file = open('bacon.txt', 'a')
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()

send2trash.send2trash('bacon.txt')
