import os
from PIL import Image

fileList = []
for dirpath, dirname, files in os.walk('./hw3/'):
    for filename in files:
        fileList.append(os.path.join(dirpath, filename))

print(fileList)

for f in fileList:
    if os.path.splitext(f)[1].lower() == '.jpg' or os.path.splitext(f)[1].lower() == '.png':
        img = Image.open(f)
        # thumbnail: resize to scale
        img.thumbnail((100, 100))
        img.save(os.path.splitext(f)[0]+'_scaled'+os.path.splitext(f)[1])

        # img.save(os.path.splitext(f)[0]+'.bmp')
