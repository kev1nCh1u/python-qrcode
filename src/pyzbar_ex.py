# https://pypi.org/project/pyzbar/

from pyzbar.pyzbar import decode
from PIL import Image
print(decode(Image.open('img/c0FVK.jpg')))

from pyzbar.pyzbar import decode
import cv2
qq = decode(cv2.imread('img/34455166.png'))
print(qq[0])
print(qq[0].rect)
print("polygon",qq[0].polygon[0].x)

frame =  cv2.imread('img/34455166.png')
qrDecode = decode(frame)
for i in qrDecode:
    print(i.rect)