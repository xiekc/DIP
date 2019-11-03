from PIL import Image
import matplotlib.pyplot as plt
import sys
import math
import numpy as np


class DFT:
    def dft1d(self, array, sign):
        M = len(array)
        spectrum = np.zeros([M], dtype=np.complex)
        for u in range(M):
            for x in range(M):
                spectrum[u] += array[x]*np.exp(sign*2j*np.pi*x*u/M)
        return spectrum

    def dft2d(self, inputImg, flags):
        print(inputImg.size)
        self.M, self.N = inputImg.size
        outputImg = Image.new('L', inputImg.size, 0)
        pxInput = inputImg.load()
        pxOutput = outputImg.load()

        spectrum0 = np.zeros([self.M, self.N], dtype=np.complex)
        spectrum1 = np.zeros([self.M, self.N], dtype=np.complex)
        spectrum2 = np.zeros([self.M, self.N], dtype=np.complex)
        for x in range(self.M):
            for y in range(self.N):
                spectrum0[x, y] = pxInput[x, y]*(-1)**(x+y)

        for x in range(self.M):
            spectrum1[x]=self.dft1d(spectrum0[x],-1)

        for v in range(self.N):
            spectrum2[:,v]=self.dft1d(spectrum1[:,v],-1)
        # check correctness
        ans = np.fft.fft2(spectrum0)
        print(np.allclose(spectrum2, ans))

        if flags == 0:
            # log tranform
            spectrum3 = np.log(np.abs(spectrum2))
            minimum = np.min(spectrum3)
            minmaxScale = 255/(np.max(spectrum3)-np.min(spectrum3))
            for x in range(self.M):
                for y in range(self.N):
                    pxOutput[x, y] = (math.floor(
                        (spectrum3[x, y]-minimum)*minmaxScale),)
                    # print(pxOutput[x,y],end=' ')
            return outputImg

        elif flags == 1:
            ispectrum1 = np.zeros([self.M, self.N], dtype=np.complex)
            ispectrum2 = np.zeros([self.M, self.N], dtype=np.complex)
            for x in range(self.M):
                ispectrum1[x]=self.dft1d(spectrum2[x],1)

            for v in range(self.N):
                ispectrum2[:,v]=self.dft1d(ispectrum1[:,v],1)

            for x in range(self.M):
                for y in range(self.N):
                    pxOutput[x, y] = (math.floor(ispectrum2[x, y].real*(-1)**(x+y)/(self.M*self.N)),)
            return outputImg



if __name__ == '__main__':
    filename = '../pic/09.png'
    img = Image.open(filename)
    mode = int(sys.argv[1])
    f = DFT()
    outputImg = f.dft2d(img, mode)
    outputImg.save('../pic/testidft.png')
