print([1, 2, 3])

print(['cat', 'bat', 'rat', 'elephat'])

spam = ['cat', 'bat', 'rat', 'elephat']
print(spam)
print(spam[0])
print(spam[1])
print(spam[2])
print(spam[3])

print(['cat', 'bat', 'rat', 'elephat'][3])

print('Hello ' + spam[0])

print('The ' + spam[1] + ' ate the ' + spam[0] + '.')

try:
      print(spam[1000])
except IndexError:
      print("list index out of range")

print(spam[1])

try:
      print(spam[1.0])
except TypeError:
      print('list indices must be integers, not float')

print(spam[int(1.0)])


spam = [['cat', 'bat'], ['10', '20', '30', '40', '50']]
print(spam[0])
print(spam[0][1])
print(spam[1][4])


spam = ['cat', 'bat', 'rat', 'elephat']
print(spam[-1])
print(spam[-3])

print('The '+ spam[-1] + ' is afarid of the ' + spam[-3] + '.')
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])

print(spam[:2])
print(spam[1:])
print(spam[:])

spam = ['cat', 'dog', 'moose']
print(len(spam))


spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
print(spam)
spam[2] = spam[1]
print(spam)
spam[-1] = 12345
print(spam)


print([1, 2, 3] + ['A', 'B', 'C'])
print(['X', 'Y', 'Z'] * 3)
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)


spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)
