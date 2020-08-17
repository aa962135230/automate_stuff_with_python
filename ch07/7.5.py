import re
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())
print(phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

