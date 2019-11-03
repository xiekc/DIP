from PIL import Image
import sys
import math
import numpy as np


class FFT:
    def zeroPadding(self, inputArray):
        M, N = inputArray.shape
        newM = 1
        newN = 1
        while newM < M:
            newM <<= 1
        while newN < N:
            newN <<= 1

        outputArray = np.zeros([newM, newN], dtype=np.complex)
        for i in range(M):
            for j in range(N):
                outputArray[i, j] = inputArray[i, j]
        return outputArray

    def dft1d(self, array, sign):
        M = len(array)
        spectrum = np.zeros([M], dtype=np.complex)
        for u in range(M):
            for x in range(M):
                spectrum[u] += array[x]*np.exp(sign*2j*np.pi*x*u/M)
        return spectrum

    def fft1d(self, array, sign):
        M = len(array)
        if M % 2 != 0:
            raise RuntimeError('M must be a power of 2')
        if M <= 32:
            return self.dft1d(array, sign)
        else:
            even = self.fft1d(array[::2], sign)
            odd = self.fft1d(array[1::2], sign)
            coeff = np.exp(sign*2j*np.pi*np.arange(M)/M)
            return np.concatenate([even+coeff[:M//2]*odd, even+coeff[M//2:]*odd])

    def fft2d(self, array, sign):
        oldM, oldN = array.shape
        array = self.zeroPadding(array)
        M, N = array.shape
        spectrum1 = np.zeros([M, N], dtype=np.complex)
        spectrum2 = np.zeros([M, N], dtype=np.complex)

        for x in range(M):
            spectrum1[x] = self.fft1d(array[x], sign)

        for v in range(N):
            spectrum2[:, v] = self.fft1d(spectrum1[:, v], sign)
        return spectrum2  # [:oldM, :oldN]

    def fft2dImg(self, inputImg, flags):
        print(inputImg.size)
        M, N = inputImg.size
        pxInput = inputImg.load()

        spectrum0 = np.zeros([M, N], dtype=np.complex)
        spectrum0 = self.zeroPadding(spectrum0)
        for x in range(M):
            for y in range(N):
                spectrum0[x, y] = pxInput[x, y]*(-1)**(x+y)
        M, N = spectrum0.shape

        outputImg = Image.new('L', (M, N), 0)
        pxOutput = outputImg.load()
        spectrum1 = self.fft2d(spectrum0, -1)
        # check correctness
        ans = np.fft.fft2(spectrum0)
        print(np.allclose(spectrum1, ans))

        if flags == 0:
            # log tranform
            spectrum2 = np.log(np.abs(spectrum1))
            minimum = np.min(spectrum2)
            minmaxScale = 255/(np.max(spectrum2)-np.min(spectrum2))
            for x in range(M):
                for y in range(N):
                    pxOutput[x, y] = (math.floor(
                        (spectrum2[x, y]-minimum)*minmaxScale),)
            return outputImg

        elif flags == 1:
            ispectrum = self.fft2d(spectrum1, 1)
            for x in range(M):
                for y in range(N):
                    pxOutput[x, y] = (math.floor(
                        ispectrum[x, y].real*(-1)**(x+y)/(M*N)),)
            return outputImg


if __name__ == '__main__':
    img = Image.open(sys.argv[1])
    mode = int(sys.argv[3])
    f = FFT()
    outputImg = f.fft2dImg(img, mode)
    outputImg.save(sys.argv[2])
