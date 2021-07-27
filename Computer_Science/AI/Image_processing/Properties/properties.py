import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./image.png', 1)

title_o = str(img.shape)

gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Gray", gimg)

img_copy = np.copy(gimg)

img_copy = img_copy/255
cv2.imshow("Scaled", img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
