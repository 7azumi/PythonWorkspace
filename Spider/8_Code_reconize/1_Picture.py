import tesserocr
from PIL import Image

'1--XCFP  2--RGFN  3--MYF7  4--82QS  5--5EPB'
# 直接识别
image = Image.open('code5.jpg')
result = tesserocr.image_to_text(image)
print(result)

# 进行灰度化或二值化处理
image = image.convert('L')  # L: 灰度图像  1：二值化图像

threshold = 136
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, mode='1')
image.show()
result = tesserocr.image_to_text(image)
print(result)