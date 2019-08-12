'''
    Reproduccion de video desde una ubicacion del disco fisico.
    Menor cantidad de lineas de codigo posible.
'''

import cv2
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
