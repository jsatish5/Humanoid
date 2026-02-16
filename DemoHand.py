import cv2
import numpy as np

cv2.namedWindow("Test", cv2.WINDOW_NORMAL)
img = np.zeros((400, 400, 3), dtype=np.uint8)
cv2.imshow("Test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()