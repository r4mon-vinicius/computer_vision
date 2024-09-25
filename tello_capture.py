from tello_zune import TelloZune
import cv2

tello = TelloZune()
tello.start_tello()

numImages = 0

while True:
    frame = tello.get_frame()

    key = cv2.waitKey(5)
    
    if key == ord('s'):
        cv2.imwrite("Image" + str(numImages) + ".png", frame)
        numImages += 1

    elif key == ord('q'):
        break

    cv2.imshow("Image", frame)

tello.end_tello()