from PIL import Image

cat_im = Image.open('zophie.png') # type: Image.Image

width, height = cat_im.size
quartersized_im = cat_im.resize((int(width/2), int(height/2))) # type: Image.Image

quartersized_im.save('svelte.png')

svelte_im = cat_im.resize((width, height + 300)) # type: Image.Image

svelte_im.save('svelte.png')