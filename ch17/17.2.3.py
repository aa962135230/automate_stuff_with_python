from PIL import Image

cat_im = Image.open('zophie.jpg')
cat_copy_im = cat_im.copy()

face_im = cat_im.crop((335, 345, 565,560))
print(face_im.size)
cat_copy_im.paste(face_im, (0, 0))
cat_copy_im.paste(face_im, (400, 500))
cat_copy_im.save('pasted.png')


cat_im_width, cat_im_height = cat_im.size
face_im_width, face_im_height = face_im.size

cat_copy_two = cat_im.copy()
for left in range(0, cat_im_width, face_im_width):
    for top in range(0, cat_im_height, face_im_height):
        print(left, top)
        cat_copy_two.paste(face_im, (left, top))

cat_copy_two.save('title.png')



