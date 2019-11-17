from PIL import Image
import matplotlib.pyplot as plt
from HSI import *

def histgram3d(img):
    width, height = img.size
    px = img.load()
    pdf = [[0 for i in range(256)]for j in range(3)]
    width, height = img.size
    for k in range(3):
        for i in range(width):
            for j in range(height):
                pdf[k][px[i, j][k]] += 1
    return pdf

def histgram1d(arr):
    width, height = len(arr),len(arr[0])
    pdf = [0 for i in range(256)]
    for i in range(width):
        for j in range(height):
            pdf[arr[i][j]] += 1
    return pdf


def equalize_hist(img):
    imgCopy = img.copy()
    px = imgCopy.load()
    pdf = histgram3d(imgCopy)
    width, height = img.size
    accumulation = [[0 for i in range(256)]for j in range(3)]
    for k in range(3):
        for i in range(len(pdf[k])):
            accumulation[k][i] = pdf[k][i]
            if i > 0:
                accumulation[k][i] += accumulation[k][i-1]

    for i in range(width):
        for j in range(height):
            px[i, j] = (int((255)/(width*height)*accumulation[0][px[i, j][0]]),
                        int((255)/(width*height)*accumulation[1][px[i, j][1]]),
                        int((255)/(width*height)*accumulation[2][px[i, j][2]]))

    return imgCopy


def equalize_hist_average(img):
    imgCopy = img.copy()
    px = imgCopy.load()
    pdf = histgram3d(imgCopy)
    width, height = img.size
    accumulation = [0 for i in range(256)]
    for i in range(len(pdf[0])):
        for k in range(3):
            accumulation[i] += pdf[k][i]
        accumulation[i] /= 3
        if i > 0:
            accumulation[i] += accumulation[i-1]

    for i in range(width):
        for j in range(height):
            px[i, j] = (int((255)/(width*height)*accumulation[px[i, j][0]]),
                        int((255)/(width*height)*accumulation[px[i, j][1]]),
                        int((255)/(width*height)*accumulation[px[i, j][2]]))

    return imgCopy

def equalize_hist_HSI(img):
    imgCopy = img.copy()
    px = imgCopy.load()
    width, height = img.size

    HSI=img2hsi(imgCopy)
    pdf = [0 for i in range(256)]
    for i in range(width):
        for j in range(height):
            pdf[int(HSI[2][i][j]*255)] += 1

    accumulation = [0 for i in range(256)]
    for i in range(len(pdf)):
        accumulation[i] = pdf[i]
        if i > 0:
            accumulation[i] += accumulation[i-1]

    for i in range(width):
        for j in range(height):
            HSI[2][i][j] = (255)/(width*height)*accumulation[int(HSI[2][i][j]*255)]/255
            # print(HSI[0][i][j],HSI[1][i][j],HSI[2][i][j])

    return hsi2img(HSI)


if __name__ == '__main__':
    # (1)Compute and display its histogram
    img = Image.open('../img/09.png')
    pdf = histgram3d(img)
    for j in range(3):
        plt.bar([i for i in range(256)], pdf[j], width=1)
        plt.savefig('../img/hist1'+'_'+str(j)+'.png')
        plt.close()

    # (2)Equalize the histogram
    imgCopy = equalize_hist(img)
    imgCopy.save('../img/img1.png')
    pdf = histgram3d(imgCopy)
    for j in range(3):
        plt.bar([i for i in range(256)], pdf[j], width=1)
        plt.savefig('../img/hist2'+'_'+str(j)+'.png')
        plt.close()

    # (3)average histogram
    imgCopy = equalize_hist_average(img)
    imgCopy.save('../img/img2.png')
    pdf = histgram3d(imgCopy)
    for j in range(3):
        plt.bar([i for i in range(256)], pdf[j], width=1)
        plt.savefig('../img/hist3'+'_'+str(j)+'.png')
        plt.close()

    # (4)perform histogram equalization on the intensity channel
    # img.thumbnail((10,10))
    imgCopy = equalize_hist_HSI(img)
    imgCopy.save('../img/img3.png')
    pdf = histgram3d(imgCopy)
    for j in range(3):
        plt.bar([i for i in range(256)], pdf[j], width=1)
        plt.savefig('../img/hist4'+'_'+str(j)+'.png')
        plt.close()