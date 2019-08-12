
import cv2
import imutils

c = 0
cap = cv2.VideoCapture('C:\\PrivateApps\\1-Gol1.mp4')

while True:

    ret, frame = cap.read()
    # frame = imutils.resize(frame, width=600)
    key = cv2.waitKey(10) & 0xff

    if not ret:
        break

    if key == ord('p'):
        print(c)
        while True:

            key2 = cv2.waitKey(1) or 0xff
            cv2.imshow('frame', frame)

            if key2 == ord('p'):
                break

    cv2.imshow('frame', frame)
    c += 1

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
