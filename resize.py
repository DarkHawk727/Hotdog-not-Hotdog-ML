import PIL
import os
from PIL import Image

f = r'dataset/train/hotdog'

for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((128,128))
    img.save(f_img)