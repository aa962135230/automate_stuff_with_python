import pyperclip

text = '''List of animals
List of aquarium life
List of biologists by author abbreviation
List of cultivars'''

pyperclip.copy(text)  #模拟系统复制操作
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
      lines[i] = '*' + lines[i]
      print(lines[i])
text = '\n'.join(lines)
pyperclip.copy(text)
