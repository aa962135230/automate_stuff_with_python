name = 'Zophie'
print(name[0])
print(name[-2])
print(name[0:4])
print('Zo' in name)
print('z' in name)
print('p' not in name)

for i in name:
      print('***' + i + '***')


print("4.6.1")
name = 'Zophie a cat'
try:
      name[7] = 'the'
except TypeError:
      print("'str' object does not support item assignment")


name = 'Zophie a cat'
new_name = name[0:7] + 'the'+ name[8:12]
print(name)
print(new_name)

eggs = [1, 2, 3]
eggs = [4, 5, 6]
print(eggs)

eggs = [1, 2, 3]
del eggs[2]
del eggs[1]
del eggs[0]

eggs.append(4)
eggs.append(5)
eggs.append(6)
print(eggs)


print("4.6.2")
eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

try:
      eggs[1] = 99
except TypeError:
      print("'tuple' object does not support item assignment")


print(type(('hello',)))


print("4.6.3")


print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
print(list('hello'))
