from PIL import ImageFont, Image, ImageDraw
import os

im = Image.new('RGBA', (200, 200), 'white') #tyep: Image.Image
draw = ImageDraw.Draw(im) # type: ImageDraw
draw.text((20, 150), 'Hello', fill='purple')
fonts_folder = 'FONT_FOLDER'

arial_font = ImageFont.truetype(os.path.join(fonts_folder, 'KhmerOS.ttf'), 32)
draw.text((100, 150), 'Howdy', fill='gray', font=arial_font)
im.save('text.png')