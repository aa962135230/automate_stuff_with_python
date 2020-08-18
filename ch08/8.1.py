import os

print('****8.1.1****')
print(os.path.join('usr', 'bin', 'spam'))
my_files = ['accounts', 'details.csv', 'invite.doxc']
for filename in my_files:
    print(os.path.join('/home/kindleeldnik/', filename))


print('****8.1.2****')
print(os.getcwd())
#/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python
os.chdir('/home/kindleeldnik/CodeWorkSpace/')
print(os.getcwd())

print('****8.1.4****')
if not os.path.exists:
    os.makedirs('/tmp/test')
os.chdir('/tmp/test')
print(os.getcwd())

print('****8.1.6****')
print(os.path.abspath('.'))
print(os.path.abspath('../'))
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('/tmp', '/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python'))
print(os.getcwd())

os.chdir('/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/')
print(os.getcwd())

py_path = '/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/ch08/8.1.py'
print(os.path.basename(py_path))
print(os.path.dirname(py_path))
print(os.path.split(py_path))

print((os.path.dirname(py_path), os.path.basename(py_path)))

print(py_path.split(os.path.sep))
print('/usr/bin'.split(os.path.sep))


print('****8.1.7****')
print(os.path.getsize(py_path))
print(os.listdir('/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/'))

total_size = 0
for filename in os.listdir('/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/'):
    total_size += os.path.getsize(os.path.join('/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/', filename))

print(total_size)

print('****8.1.8****')
print(os.path.exists('/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/'))
print(os.path.exists('/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/sdf'))
print(os.path.isdir('/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/'))

py_path = '/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/ch08/8.1.py'
print(os.path.isfile('/home/kindleeldnik/CodeWorkSpace/automate_stuff_with_python/ch08/'))
print(os.path.isdir(py_path))
print(os.path.isfile(py_path))





