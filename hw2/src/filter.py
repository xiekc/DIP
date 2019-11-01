from PIL import Image
import matplotlib.pyplot as plt
import sys


def filter2d(img, filter):
    img_f = img.copy()
    width, height = img.size
    px = img_f.load()
    size = len(filter)

    position = [i-i/2 for i in range(size)]
    for i in range(width):
        for j in range(height):
            sum = 0
            for m in range(size):
                for n in range(size):
                    if i+position[m] < 0 or j+position[n] < 0 or i+position[m] >= width or j+position[n] >= height:
                        sum += 0
                    else:
                        sum += px[i+position[m], j+position[n]]*filter[m][n]
            px[i, j] = int(sum)
    return img_f


if __name__ == '__main__':
    img = Image.open('../pic/09.png')
    mode = int(sys.argv[1])
    filter = []
    if mode == 0:
        size = int(sys.argv[2])
        filter = [[1/(size*size)] * size for i in range(size)]
        print(filter)
        filter2d(img, filter).save('../pic/img'+str(mode)+'_'+str(size)+'.png')
    elif mode == 1:
        filter = [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
        print(filter)
        filter2d(img, filter).save('../pic/img'+str(mode)+'_'+str(size)+'.png')

    elif mode == 2:
        size = 3
        filter = [[1/(size*size)] * size for i in range(size)]
        img_smooth = filter2d(img, filter)
        width, height = img.size
        px = img.load()
        px_smooth = img_smooth.load()
        k = int(sys.argv[2])
        for i in range(width):
            for j in range(height):
                px[i, j] += int(k*px[i, j]-k*px_smooth[i, j])
        img.save('../pic/img'+str(mode)+'_'+str(k)+'.png')
