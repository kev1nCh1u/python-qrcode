##########################
# qrcode position        #
# 20201128 by kevin chiu #
##########################

from pyzbar.pyzbar import decode
import cv2


cap = cv2.VideoCapture(2)
while(True):
    ret, frame = cap.read()
    img = frame

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    qrDecode = decode(img)
    for qrLoop in qrDecode:
        print(qrLoop.rect)

        qrRectX, qrRectY, qrRectW, qrRectH = qrLoop.rect.left, qrLoop.rect.top, qrLoop.rect.width, qrLoop.rect.height
        cv2.circle(img, (int(qrRectX + qrRectW / 2),
                         int(qrRectY + qrRectH / 2)), 5, (0, 255, 0), -1)
        cv2.rectangle(img, (qrRectX, qrRectY),
                      (qrRectX+qrRectW, qrRectY+qrRectH), (255, 0, 0), 8)

        for qrPolygonLoop in qrLoop.polygon:
            cv2.circle(img, (qrPolygonLoop.x, qrPolygonLoop.y), 5, (0, 0, 255), -1)

    cv2.imshow('img', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
