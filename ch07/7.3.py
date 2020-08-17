import re

print('****7.3.1****')
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is 415-555-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())

area_code, main_number = mo.groups()
print(area_code)
print(main_number)


phone_num_regex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is (415)-555-4242')
print(mo.group(1))
print(mo.group(2))

print('****7.3.2****')

hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = hero_regex.search('Tina Fey and Batman')
print(mo2.group())

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))


print('****7.3.3****')
bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('The Adventures of Batman')
print(mo1.group())

mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())

phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phone_regex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phone_regex.search('My number is 555-4242')
print(mo2.group())


print('****7.3.4****')
bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('The Adventures of Batman')
print(mo1.group())

mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())

mo3 = bat_regex.search('The Adventures of Batwowowowoman')
print(mo3.group())


print('****7.3.5****')
bat_regex = re.compile(r'Bat(wo)+man')
mo1 = bat_regex.search('The Adventures of Batwoman')
print(mo1.group())

mo2 = bat_regex.search('The Adventures of Batwowowowoman')
print(mo2.group())

mo3 = bat_regex.search('The Adventures of Batman')
print(mo3 == None)

print('****7.3.6****')
ha_ragex = re.compile(r'(Ha){3}')
mo1 = ha_ragex.search('HaHaHa')
print(mo1.group())

mo2 = ha_ragex.search('Ha')
print(mo2 == None)