import sys
import os
from PIL import Image
image_folder = sys.argv[1]
op_folder = sys.argv[2]
if not os.path.exists(op_folder):
    os.mkdir(op_folder)
for filename in os.listdir(image_folder):
    image = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)
    image.save(f'{op_folder}{clean_name[0]}.png', 'png')
