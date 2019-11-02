from PIL import Image
import matplotlib.pyplot as plt
import sys
from math import *


def dft2d(inputImg, flags):
    print(inputImg.size)
    width, height = inputImg.size
    outputImg = Image.new('L', inputImg.size, 0)
    px = outputImg.load()
    for u in range(width):
        for v in range(height):
            result = 0+0j
            for x in range(width):
                for y in range(height):
                    coeff = u*x/width+v*y/height
                    if flags == 0:
                        result += complex(cos(coeff), -sin(coeff))
                    elif flags == 1:
                        result += complex(cos(coeff), sin(coeff))
            px[u, v] = floor(
                sqrt(result.real*result.real+result.imag*result.imag))

    return outputImg


if __name__ == '__main__':
    img = Image.open('../img/09.png')
    # mode = int(sys.argv[1])
    outputImg = dft2d(img, 0)
    outputImg.save('../img/dft.png')
