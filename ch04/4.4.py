print("4.4.1")
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))
print(spam.index('heyas'))
try:
      print(spam.index('howdy howdy howdy'))
except ValueError:
      print("The value is not in list")

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka'))


print("4.4.2")
spam = ['cat', 'dog', 'cat']
spam.append('moose')
print(spam)

spam = ['cat', 'dog', 'cat']
spam.insert(1, 'chicken')
print(spam)

eggs = 'hello'

try:
      eggs.append('world')
except AttributeError:
      print("'str' object has no attribute 'append'")

bacon = 42
try:
      bacon.insert(1, 'world')
except AttributeError:
      print("'int' object has no attribute 'insert'")


print("4.4.3")
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)
try:
      spam.remove('chicken')
except ValueError:
      print("list.remove(x): chicken not in list")


spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
print(spam)


print("4.4.4")
spam = [2, 3, 3.14, 1, -7]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)

spam = [1, 2, 3, 4, 'Alice', 'Bob']
try:
      spam.sort()
except TypeError:
      print(" not supported between instances of 'str' and 'int'")


spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
print(spam)
