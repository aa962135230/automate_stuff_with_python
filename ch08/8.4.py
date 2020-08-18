import pprint, os
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))

if os.path.exists(os.path.abspath('./ch08/file/my_cats.py')):
    os.unlink(os.path.abspath('./ch08/file/my_cats.py'))

file_obj = open(os.path.abspath('./ch08/file/my_cats.py'), 'w')
file_obj.write('cats = ' + pprint.pformat(cats) + '\n')
file_obj.close()

