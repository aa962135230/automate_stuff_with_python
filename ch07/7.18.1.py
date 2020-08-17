import re

def pwd_check(password):
    regex1 = re.compile(r'[a-z]+')
    regex2 = re.compile(r'[A-Z]+')
    regex3 = re.compile(r'\d+')
    if regex1.search(password) == None:
        return False
    if regex2.search(password) == None:
        return False
    if regex3.search(password) == None:
        return False
    if len(password) < 8:
        return False
    return True


print(pwd_check('1234'))
print(pwd_check('1234AA'))
print(pwd_check('1234AASs'))
print(pwd_check('1234sfdA@python'))


