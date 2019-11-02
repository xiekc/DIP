from PIL import Image
import matplotlib.pyplot as plt
import sys
import numpy as np


def dft2d(inputImg, flags):
    print(inputImg.size)
    M, N = inputImg.size
    outputImg = Image.new('L', inputImg.size, 0)
    spectrum1 = np.zeros([M, N], dtype=np.complex)
    spectrum2 = np.zeros([M, N], dtype=np.complex)
    pxInput = inputImg.load()
    pxOutput = outputImg.load()
    if flags == 0:
        sign = -1j
    elif flags == 1:
        sign = 1j

    spectrum0 = np.zeros([M, N], dtype=np.complex)
    for x in range(M):
        for y in range(N):
            spectrum0[x, y] = pxInput[x, y]*(-1)**(x+y)

    for x in range(M):
        for v in range(N):
            for y in range(N):
                spectrum1[x, v] += spectrum0[x, y]*np.exp(sign*2*np.pi*y*v/N)

    for v in range(N):
        for u in range(M):
            for x in range(M):
                spectrum2[u, v] += spectrum1[x, v]*np.exp(sign*2*np.pi*x*u/M)
    # check correctness
    ans = np.fft.fft2(spectrum0)
    print(np.allclose(spectrum2, ans))

    spectrum3 = np.log(np.abs(spectrum2))
    minimum = np.min(spectrum3)
    minmaxScale = 255/(np.max(spectrum3)-np.min(spectrum3))
    for x in range(M):
        for y in range(N):
            pxOutput[x, y] = (floor((spectrum3[x, y]-minimum)*minmaxScale),)
            # print(pxOutput[x,y],end=' ')
    return outputImg


if __name__ == '__main__':
    filename = '../img/09.png'
    img = Image.open(filename)
    mode = int(sys.argv[1])
    outputImg = dft2d(img, mode)
    outputImg.save('../img/dft.png')
