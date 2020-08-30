import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

os.makedirs('withLogo', exist_ok=True)

logo_im = Image.open(LOGO_FILENAME) # type: Image.Image
logo_width, logo_height = logo_im.size

for file_name in os.listdir('.'):
    if not (file_name.endswith('.png')) or file_name.endswith('.jpg') or file_name == LOGO_FILENAME:
        continue
    im = Image.open(file_name) # type: Image.Image
    width, height = im.size

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        print('Resizing %s...' % (file_name))
        im = im.resize((width, height)) # type: Image.Image 

    print('Adding logo to %s...' % (file_name))
    im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)
    im.save(os.path.join('withLogo', file_name))


