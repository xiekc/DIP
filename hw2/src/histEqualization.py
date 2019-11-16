from PIL import Image
import matplotlib.pyplot as plt


def histgram(img):
    width, height = img.size
    pdf = [0 for i in range(256)]
    px = img.load()
    width, height = img.size
    for i in range(width):
        for j in range(height):
            pdf[px[i, j]] += 1
    return pdf


def equalize_hist(img):
    img_f = img.copy()
    accumulation = [0 for i in range(256)]
    px = img_f.load()
    width, height = img.size

    pdf = histgram(img_f)
    for i in range(len(pdf)):
        accumulation[i] = pdf[i]
        if i > 0:
            accumulation[i] += accumulation[i-1]

    for i in range(width):
        for j in range(height):
            px[i, j] = int((255)/(width*height)*accumulation[px[i, j]])

    return img_f


if __name__ == '__main__':
    # (1)Compute and display its histogram
    img = Image.open('../pic/09.png')
    pdf = histgram(img)
    plt.bar([i for i in range(256)], pdf, width=1)
    plt.savefig('../pic/hist1.png')
    plt.close()

    # (2)Equalize the histogram
    img = equalize_hist(img)
    img.save('../pic/img1.png')
    pdf = histgram(img)
    plt.bar([i for i in range(256)], pdf, width=1)
    plt.savefig('../pic/hist2.png')
    plt.close()

    # (3)Equalize the histogram again
    img = equalize_hist(img)
    img.save('../pic/img2.png')
    pdf = histgram(img)
    plt.bar([i for i in range(256)], pdf, width=1)
    plt.savefig('../pic/hist3.png')
    plt.close()
