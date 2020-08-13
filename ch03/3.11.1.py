import sys

def collatz(number):
      if (number%2) == 0:
            print(number//2)
            return number//2
      elif (number%2) == 1:
            print( (number*3) + 1)
            return ((number*3) + 1)
            
print("请输入一个整数")

try:
      number = int(input())
except ValueError:
      print("你必须输入一个整数")
      sys.exit()


while True:
      number = collatz(number)
      if number == 1:
            break

