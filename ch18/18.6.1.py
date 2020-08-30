import pyautogui

im = pyautogui.screenshot()
print(im.getpixel((0, 0)))
print(im.getpixel((50, 200)))

