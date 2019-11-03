from PIL import Image
import sys
from fft import FFT
import numpy as np
import math


def filter2d_freq(inputImg, filter):
    print(inputImg.size)
    pxInput = inputImg.load()
    M, N = inputImg.size
    size = len(filter)
    fft = FFT()

    position = [i-i/2 for i in range(size)]
    imgArray = np.zeros([M, N], dtype=np.complex)
    imgArray = fft.zeroPadding(imgArray)
    for x in range(M):
        for y in range(N):
            imgArray[x, y] = pxInput[x, y]

    M, N = imgArray.shape
    outputImg = Image.new('L', (M, N), 0)
    pxOutput = outputImg.load()
    filterArray = np.zeros([M, N], dtype=np.complex)
    for x in range(size):
        for y in range(size):
            filterArray[x, y] = filter[x][y]

    filterSpectrum = fft.fft2d(filterArray, -1)
    ans = np.fft.fft2(filterArray)
    print(np.allclose(filterSpectrum, ans))
    
    imgSpectrum = fft.fft2d(imgArray, -1)
    ans = np.fft.fft2(imgArray)
    print(np.allclose(imgSpectrum, ans))

    spectrum = np.zeros([M, N], dtype=np.complex)
    for x in range(M):
        for y in range(N):
            spectrum[x, y] = filterSpectrum[x, y]*imgSpectrum[x, y]
    spectrum = fft.fft2d(spectrum, 1)

    for x in range(M):
        for y in range(N):
            pxOutput[x, y] = (math.floor(
                spectrum[x, y].real/(M*N)),)
    return outputImg


if __name__ == '__main__':
    inputImg = Image.open(sys.argv[1])
    mode = int(sys.argv[3])
    filter = []
    if mode == 0:
        size = 5
        filter = [[1/(size*size)] * size for i in range(size)]
        print(filter)
        filter2d_freq(inputImg, filter).save(sys.argv[2])
    elif mode == 1:
        filter = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
        print(filter)
        filter2d_freq(inputImg, filter).save(sys.argv[2])
