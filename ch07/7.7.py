import re
vowel_regex = re.compile(r'[aeiouAEIOU]')
print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))

consonant_regex = re.compile(r'[^aeiouAEIOU]')
print(consonant_regex.findall('RoboCop eats baby food. BABY FOOD.'))
