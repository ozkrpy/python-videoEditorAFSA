import cv2
import numpy as np
import imutils
# INICIALIZACION DE VARIABLES
# C = contador de frames
# video = archivo de video a ser procesado
c = 0
video = cv2.VideoCapture("C:\\PrivateApps\\1-Gol1.mp4")

if (video.isOpened() == False):
    print("Error opening video  file")

while (video.isOpened()):
    ret, frame = video.read()
    if ret:
        frame = imutils.resize(frame, width=600)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(15) & 0xFF == ord('q'):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()

# while(cap.isOpened()):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#     # espera la presion de una tecla
#     frame = imutils.resize(frame, width=800)
#     key = cv2.waitKey(25) & 0xff

#     # if ret == True:
#     #     frame = imutils.resize(frame, width=1000)
#     #     # Display the resulting frame
#     #     cv2.imshow('Frame', frame)
#     #     # waitKey define la velocidad de reproduccion
#     #     if cv2.waitKey(15) & 0xFF == ord('q'):
#     #         break
#     # else:
#     #     break
#     if key == ord('a'):
#         while True:

#             key2 = cv2.waitKey(1) or 0xff
#             cv2.imshow('frame', frame)

#             if key2 == ord('a'):
#                 break
#     cv2.imshow('frame', frame)

#     if key == 27:
#         break
#     # current frame
#     c += 1
#     print(c)
# cap.release()
# cv2.destroyAllWindows()
