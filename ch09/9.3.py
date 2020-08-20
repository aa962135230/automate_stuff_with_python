import zipfile, os

print("****9.3.1****")
example_zip = zipfile.ZipFile('example.zip')
print(example_zip.namelist())
spam_info = example_zip.getinfo('vue-master/vue.config.js')
print(spam_info.file_size)
print(spam_info.compress_size)
print("Compressed file is %sx smaller!" % (round(spam_info.file_size / spam_info.compress_size, 2)))
example_zip.close()

print("****9.3.2****")
example_zip = zipfile.ZipFile('example.zip')
example_zip.extractall()
example_zip.close()

print("****9.3.3****")
new_zip = zipfile.ZipFile('new.zip', 'w')
new_zip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
new_zip.close()