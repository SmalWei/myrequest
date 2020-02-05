import pytesseract
from PIL import Image

image = Image.open('RandCode.gif')
#转换图片的模式
# 图片的二值化处理识别：
image = image.convert('L')
threshold = 140
table = []
for  i in range(256):
    if i <threshold:
        table.append(0)
    else:
        table.append(1)
out = image.point(table,'1')
text=pytesseract.image_to_string(Image.open('b'+'1.jpg'),lang='chi_sim')
print(text)
# # print(pytesseract.image_to_string())
# print(text)






