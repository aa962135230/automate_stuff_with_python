import pyautogui

pyautogui.scroll(200)

import pyperclip
numbers = ''
for i in range(200):
    numbers = numbers + str(i) + '\n'

print(numbers)
pyperclip.copy(numbers)