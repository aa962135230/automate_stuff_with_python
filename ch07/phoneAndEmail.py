import re, pyperclip
phone_regex = re.compile(r'''
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?''', re.VERBOSE)


email_regex = re.compile(r'''
    [a-zA-z0-9._%+-]+ #username
    @                 #@ symbol
    [a-zA-Z0-9.-]+    #domail name
    (\.[a-zA-Z]{2,4})''', re.VERBOSE)


text = str(pyperclip.paste())
matches = []

for groups in phone_regex.findall(text):
    phone_number = '-'.join([groups[1], groups[2], groups[3]])
    if groups[8] != '':
        phone_number += 'x' + groups[8]
    matches.append(phone_number)

for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email addresses found.')
