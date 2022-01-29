from PIL import Image

im = Image.open(r"D:\pyrus\NewGame\images\bos\face4.png")
im = im.crop((5, 5, 65, 65))
im.save(r"D:\pyrus\NewGame\images\bos\face4.png", quality = 5)