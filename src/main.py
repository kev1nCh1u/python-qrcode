##########################
# qrcode position        #
# 20201128 by kevin chiu #
##########################

from pyzbar.pyzbar import decode
import cv2


cap = cv2.VideoCapture(2)
while(True):
    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    qrDecode = decode(frame)
    for i in qrDecode:
        print(i.rect)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()