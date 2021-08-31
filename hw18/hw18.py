# Написать скрипт, который будет создавать миниатюры фотографий.
# Объем полученого файла должен передаваться как параметр.
#!/usr/bin/env python3
import sys
from PIL import Image

errorstring = '''
Incorrect arguments.
First argument should be path to original image.
Second argument should be scale as percent."
'''

def resizeimage(sourceimage, scale):
    ''' Saves resized version.
    Args:
        sourceimage: source image
        scale: size of scfaled version as percentage of source image
    '''
    sourceimagename = sourceimage.split(".")[0]
    sourceimageformat = sourceimage.split(".")[1]
    src = Image.open(sourceimage)
    width, height = src.size
    newsize = (int(width * int(scale) / 100), int(height * int(scale) / 100))
    resizedimage = src.resize(newsize)
    resizedimage.save(f"{sourceimagename}_scale_{scale}_percents.{sourceimageformat}")

if __name__ == '__main__':
    try:
        sourceimage = sys.argv[1]
        scale = sys.argv[2]
        resizeimage(sourceimage, scale)
    except IndexError:
        print(errorstring)
    
