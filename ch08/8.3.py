import shelve, os
shelf_file = shelve.open(os.path.abspath('./ch08/file/mydata'))
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cats'] = cats

shelf_file.close()

shelf_file = shelve.open(os.path.abspath('./ch08/file/mydata'))
print(type(shelf_file))
print(shelf_file['cats'])
shelf_file.close()

shelf_file = shelve.open(os.path.abspath('./ch08/file/mydata'))
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
shelf_file.close()


