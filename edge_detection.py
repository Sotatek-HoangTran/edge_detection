import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('./dxd/big_1.jpg')

retval, threshold = cv.threshold(img, 45, 255, cv.THRESH_BINARY_INV)
blur = cv.blur(threshold,(5,5))
median = cv.medianBlur(threshold,5)
gaussian = cv.GaussianBlur(threshold,(5,5),0)
retval_, threshold_ = cv.threshold(gaussian, 80, 255, cv.THRESH_BINARY)
edges2 = cv.Canny(gaussian,0,200)

#laplacian
laplacian = cv.Laplacian(threshold_, cv.CV_64F)

#sobel
img_sobelx = cv.Sobel(threshold_,cv.CV_8U,1,0,ksize=5)
img_sobely = cv.Sobel(threshold_,cv.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely

#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv.filter2D(threshold_, -1, kernelx)
img_prewitty = cv.filter2D(threshold_, -1, kernely)
img_prewitt = img_prewittx + img_prewitty

#robert
robertx = np.array([[0,0,0],[0,1,0],[0,0,-1]])
roberty = np.array([[0,0,0],[0,0,1],[0,-1,0]])
img_robertx = cv.filter2D(threshold_, -1, robertx)
img_roberty = cv.filter2D(threshold_, -1, roberty)
img_robert = img_robertx + img_roberty

plt.subplot(2,2,1),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(img_robert,cmap = 'gray')
plt.title('robert'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(img_prewitt,cmap = 'gray')
plt.title('prewitt'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(img_sobel,cmap = 'gray')
plt.title('sobel'), plt.xticks([]), plt.yticks([])


plt.show()
cv.waitKey(0)
cv.destroyAllWindows()