def list_to_str(list):
      str = ''
      for i in range(0,len(list)):
            if i == len(list)-1:                 
                  str = str + 'and ' + list[i]
            else:
                  str = str + list[i] + ','
      return str

spam = ['apples', 'bananas', 'tofu', 'cats']
spamtest2 = spam * 3

print(list_to_str(spam))
print(list_to_str(spamtest2))
