my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(my_cat['size'])
print('My cat has ' + my_cat['color'] + ' fur.')

spam = {12345: 'Luggage Combination', 42: 'The answer'}
print(spam)

print("****5.1.1****")
spam = ['cats', 'gogs', 'moose']
bacon = ['dogs', 'mosse', 'cats']
print(spam == bacon)

eggs = {'name':'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name':'Zophie'}
print(eggs == ham)


spam = {'name':'Zophie', 'age': '8'}
try:
      print(spam['color'])
except KeyError:
      print("KeyError")


print("****5.1.2****")
spam = {'color': 'red', 'age': 42}
for v in spam.values():
      print(v)

for k in spam.keys():
      print(k)

for i in spam.items():
      print(i)

print(spam.keys())
print(list(spam.keys()))

for k, v in spam.items():
      print('key: ' + k + ' Value: ' + str(v))

print("****5.1.3****")
spam = {'name': 'Zophine', 'age': 7}
print('name' in spam.keys())
print('Zophine' in spam.values())
print('color' in spam.keys())
print('color' not in spam.keys())
print('color' in spam)

print('****5.1.4****')
picnic_items = {'apple': 5, 'cups': 2}
print("I am bringing " + str(picnic_items.get('cups', 0)) + ' cups.')

print("I am bringing " + str(picnic_items.get('eggs', 0)) + ' eggs.')

try:
      print("I am bringing " + str(picnic_items['eggs']) + ' eggs.')
except KeyError:
      print("KeyError")

spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
      spam['color'] = 'black'
print(spam)

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(spam)
spam.setdefault('color', 'white')
print(spam)




