from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import sys

def get_output_path():
    import shutil
    if sys.argv and len(sys.argv) > 1:
        output_path = sys.argv[1]
    else:
        output_path = "output-images"
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.mkdir(output_path)
    return output_path


output_path = get_output_path()
input_path = "source-images"
images_list = os.listdir(input_path)
height_margin = 90
width_margin = 30

for image in images_list:
    if image.endswith('.jpg'):
        output_image_path = output_path + '/' + image
        img = Image.open(input_path + '/' + image)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("AftaSansThin-Regular.otf", 64)
        width, height = img.size
        image_text = "(c) " + image.replace('.jpg', '').replace('-', ' ').title()
        text_lenght = len(image_text)
        draw.text((width - width_margin * (text_lenght + 1), height - height_margin),
                  image_text, (255, 255, 255), font=font)
        img.save(output_image_path)

