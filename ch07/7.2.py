import re

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())

