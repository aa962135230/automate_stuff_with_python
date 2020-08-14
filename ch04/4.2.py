print("4.2.1")

for i in range(4):
      print(i)

for i in [0, 1, 2, 3]:
      print(i)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
      print("Index " + str(i) + ' in supplies is: ' + supplies[i])


print("4.2.2")
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])

spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam) 
print('howdy' not in spam)
print('cat' not in spam)


print("4.2.3")
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(cat)
cat = ['fat', 'black', 'loud']
print(cat)

size, color, disposition = cat
print(size + " " + color + " " + disposition)



