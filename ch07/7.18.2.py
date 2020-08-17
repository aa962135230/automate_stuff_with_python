import re

def py_re_strip(text, chars = ''):
    if chars:
        regex = re.compile(chars)
        # print(regex.sub('', text))
    else:
        regex = re.compile(r'^\s*|\s*$')
        # print(regex.sub('', text))
    print(regex.sub('', text))

py_re_strip(' sdafdsaga ')
py_re_strip(' sdafdsaga ', 'sd')
