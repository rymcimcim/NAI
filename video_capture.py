import numpy as np
import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 10.0, (640, 480))
while True:
    ret_val, img1 = capture.read()
    img2 = cv2.flip(img1, 1)
    img3 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    cv2.imshow('my webcam', img1)
    out.write(img1)
    cv2.imshow('filpped', img2)
    cv2.imshow('gray', img3)
    if cv2.waitKey(1) == 27:
        break  # esc to quit

capture.release()
out.release()
cv2.destroyAllWindows()
