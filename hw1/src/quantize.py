from PIL import Image
from math import *


def quantize(img, level):
    img_f = img.copy()
    px = img_f.load()
    w, h = img.size
    for i in range(w):
        for j in range(h):
            px[i, j] = floor(px[i, j]*level/256)*floor(256/(level-1))

    return img_f


if __name__ == '__main__':
    img = Image.open('./09.png')

    quantize(img, 128).save('./q1.png')
    quantize(img, 64).save('./q2.png')
    quantize(img, 32).save('./q3.png')
    quantize(img, 8).save('./q4.png')
    quantize(img, 2).save('./q5.png')
