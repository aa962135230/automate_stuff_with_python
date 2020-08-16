print("****6.2.1****")
spam = 'Hello world!'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

spam = 'Hello world!'
print(spam.islower())
print(spam.isupper())

print('HELLO'.isupper())
print('abc12345'.islower())
print('12345'.islower())
print('12345'.isupper())

print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper())
print('HELLO'.lower())
print('HELLO'.lower().islower())

print("****6.2.2****")
print('hello'.isalpha())
print('hello123'.isalpha())
print('hello123'.isalnum())
print('hello'.isalnum())
print('123'.isdecimal())
print(' '.isspace())
print('This Is Title Case'.istitle())
print('This Is Title Case 123'.istitle())
print('This Is not Title Case'.istitle())
print('This Is NOT Title Case Either'.istitle())

print("****6.2.3****")
print('Hello world!'.startswith('Hello'))
print('Hello world!'.endswith('world!'))
print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12'))
print('Hello world!'.startswith('Hello world!'))
print('Hello world!'.endswith('Hello world!'))

print("****6.2.4****")
print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('ABC'.join(['My', 'name', 'is', 'Simon']))

print('My name is Simon'.split())
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))

spam='''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".
please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))

print("****6.2.5****")
print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello World'.rjust(20))
print('Hello'.ljust(10))
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
print('Hello'.center(20))
print('Hello'.center(20, '='))


print("****6.2.6****")
spam = ' Hello World '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

print("****6.2.7****")

import pyperclip
pyperclip.copy('Hello world!')
print(pyperclip.paste())


