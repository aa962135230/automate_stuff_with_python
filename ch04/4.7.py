spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)


spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello'
print(spam)
print(cheese)

print("4.7.2")
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)


