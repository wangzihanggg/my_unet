from email.mime import image
from PIL import Image

def  keep_image_size_open(path, size(256, 256)):
    img = Image.open(path)
    temp = max(image.path)
    mask = Image.new('RGB', ((temp, temp), (0,0,0)))
    mask.paste(img,(0,0))
    mask = mask.resize(size)
    return mask