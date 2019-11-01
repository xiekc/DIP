from PIL import Image
from math import *


def bilinear(distI, distJ, origin_size, final_size, px):
    w_o, h_o = origin_size
    w_f, h_f = final_size
    i = min(floor(distI*w_o/w_f), w_o-2) # to prevent out of the range
    j = min(floor(distJ*h_o/h_f), h_o-2)
    v = (distI*w_o/w_f)-i
    u = (distJ*h_o/h_f)-j
    return floor(v*u*px[i, j]+v*(1-u)*px[i, j+1]+(1-v)*u*px[i+1, j]+(1-v)*(1-u)*px[i+1, j+1])


def scale(img, final_size):
    w_f, h_f = final_size
    final_img = Image.new('L', final_size)
    px_o = img.load()
    px_f = final_img.load()
    for i in range(w_f):
        for j in range(h_f):
            px_f[i, j] = (bilinear(i, j, img.size, final_size, px_o),)
    return final_img


if __name__ == '__main__':
    img = Image.open('./09.png')

    scale(img, (192, 128)).save('./s1.png')
    scale(img, (96, 64)).save('./s2.png')
    scale(img, (48, 32)).save('./s3.png')
    scale(img, (24, 16)).save('./s4.png')
    scale(img, (12, 8)).save('./s5.png')

    scale(img, (300, 200)).save('./s6.png')
    scale(img, (450, 300)).save('./s7.png')
    scale(img, (500, 200)).save('./s8.png')
