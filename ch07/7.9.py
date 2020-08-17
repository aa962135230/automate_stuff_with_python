import re
at_regex = re.compile(r'.at')

print(at_regex.findall('The cat in the hat sat on the flat mat.'))


print('****7.9.1****')
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search('First Name: A1 Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))

nongredy_regex = re.compile(r'<.*?>')

mo = nongredy_regex.search('<To serve man> for dinner.')
print(mo.group())

greedy_regex = re.compile(r'<.*>')
mo = greedy_regex.search('<To serve man> for dinner.')
print(mo.group())


print('****7.9.2****')
no_newline_regex = re.compile('.*')
print(no_newline_regex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())

newline_regex = re.compile('.*', re.DOTALL)
print(newline_regex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())


