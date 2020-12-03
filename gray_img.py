import cv2

img_log = "input/baboon.png"

img_bgr = cv2.imread(img_log)

img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
cv2.imwrite("output_grayscale/gray.png", img_gray)
