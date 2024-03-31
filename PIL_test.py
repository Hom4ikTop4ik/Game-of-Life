from PIL import Image

with Image.open("map.png") as img:
    # if img not GRAYSCALE   we make it so
    if( img.getbands() != ("L") ):
        gray_img = img.convert("L")
        gray_img = gray_img.resize([100, 100])
        gray_img.save('map.png')
with Image.open("map.png") as img:
    pix = img.load()
    x, y = img.size[0], img.size[1]
print(2*x, 3*y)