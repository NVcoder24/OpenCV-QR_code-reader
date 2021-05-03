from cv2 import VideoCapture, QRCodeDetector, imshow, waitKey
from os import system
import numpy


camera = VideoCapture(0)

debug = True

while(True):
    ret, image = camera.read()

    try:
        qrCodeDetector = QRCodeDetector()
        decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
    except Exception as e:
        decodedText = ""
        if debug:
            print(f"something goes wrong: {e}")

    if decodedText != "":
        system("cls")
        print(decodedText)
        print(points)

    imshow('image', image)

    if waitKey(1) & 0xFF == ord('q'):
        break


camera.release()