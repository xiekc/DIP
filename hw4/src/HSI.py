from PIL import Image
import math


def rgb2hsi(rgb):
    r, g, b = rgb
    theta = math.acos(1/2*(r-g+r-b)/(math.sqrt((r-g)**2+(r-b)*(g-b))+1e-10))
    theta = 180*theta/math.pi
    if b <= g:
        H = theta
    else:
        H = 360-theta
    S = 1-(3/(r+b+g)*(min(r, g, b)))
    I = 1/3*(r+b+g)
    return H, S, I


def hsi2rgb(hsi):
    H, S, I = hsi

    if 0 <= H and H < 120:
        H = H*math.pi/180
        b = I*(1-S)
        r = I*(1+(S*math.cos(H)/(math.cos(math.pi/3-H))))
        g = 3*I-(r+b)
    elif 120 <= H and H < 240:
        H = H-120
        H = H*math.pi/180
        r = I*(1-S)
        g = I*(1+(S*math.cos(H))/(math.cos(math.pi/3-H)))
        b = 3*I-(r+g)
    elif 240 <= H and H <= 360:
        H = H-240
        H = H*math.pi/180
        g = I*(1-S)
        b = I*(1+(S*math.cos(H))/(math.cos(math.pi/3-H)))
        r = 3*I-(g+b)
    else:
        raise Exception('error HSI')

    return r, g, b


def img2hsi(img):
    imgCopy = img.copy()
    px = imgCopy.load()
    width, height = img.size
    HSI = [[[0 for i in range(height)]for j in range(width)]for k in range(3)]

    for i in range(width):
        for j in range(height):
            # print(px[i, j][0], px[i, j][1], px[i, j][2])
            H, S, I = rgb2hsi((px[i, j][0]/255, px[i, j][1]/255, px[i, j][2]/255))
            HSI[0][i][j] = (H)
            HSI[1][i][j] = (S)
            HSI[2][i][j] = (I)
    return HSI


def hsi2img(HSI):
    width, height = len(HSI[0]), len(HSI[0][0])
    img = Image.new('RGB', (width, height))
    px = img.load()
    for i in range(width):
        for j in range(height):
            # print(px[i,j])
            r, g, b = hsi2rgb((HSI[0][i][j], HSI[1][i][j], HSI[2][i][j]))
            px[i, j] = (int(r*255), int(g*255), int(b*255))
    return img


if __name__ == '__main__':
    print(rgb2hsi((1, 0, 1)))
    print(rgb2hsi((0, 0, 1)))
    print(hsi2rgb((300, 1, 1)))
    print(hsi2rgb((240, 1, 1)))
    pass
