spam = "That is Alice's cat"
print(spam) 
spam = 'Say hi to Bob\'s mother.'
print(spam)
print("Hello there! \nHow are you? \nI\'m doing fine.")


"""This is a test python program.
written by Al Sweigart al@inventwithpython.com

This program was designed for Python 3, not Python 2.
"""
def spam1():
      """This is a multiline comment to help
      explain what the spam() function does."""
      print("Hello!")

spam1()

spam = 'Hello world!'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[6:])
fizz = spam[0:5]
print(spam)
print(fizz)

print('Hello' in 'Hello world!')
print('Hello' in 'Hello')
print('HELLO' in 'Hello world!')
print('' in spam)
print('cats' not in 'cats and dogs')
