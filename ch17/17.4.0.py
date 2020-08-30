from PIL import Image, ImageDraw

im = Image.new("RGBA", (200, 200), 'white')
draw = ImageDraw.Draw(im) # type: ImageDraw


