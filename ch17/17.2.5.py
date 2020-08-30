from PIL import Image

cat_im = Image.open('zophie.png') # type: Image.Image
cat_im.rotate(90).save('rotated90.png')
cat_im.rotate(180).save('rotated180.png')
cat_im.rotate(270).save('rotated270.png')
cat_im.rotate(6).save('rotated6.png')
cat_im.rotate(6, expand=True).save('rotated6_expand.png')

cat_im.transpose(Image.FLIP_LEFT_RIGHT).save("horizontal_flip.png")
cat_im.transpose(Image.FLIP_TOP_BOTTOM).save("vertical_flip.png")