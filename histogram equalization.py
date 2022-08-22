import numpy as np
import cv2

img = cv2.imread("C:\\Users\Admin\Desktop\plaka\\1.jpg",0)

#To display image before equalization
cv2.imshow('image',img)
cv2.waitKey(0)


a = np.zeros((256,),dtype=np.float16)      # Create new matrix for RGB histogram
b = np.zeros((256,),dtype=np.float16)      # Create new matrix for histogram equalization

height,width=img.shape

#Applying RGB histgoram 
for i in range(width):
    for j in range(height):
        g = img[j,i]        
        a[g] = a[g]+1      



#Histogram equalization
for i in range(256):
    for j in range(i+1):
        b[i] += a[j]/(height*width)
    b[i] = round(b[i] * 255)       

b=b.astype(np.uint8)        #all elements should be integer

#Final matrix
for i in range(width):
    for j in range(height):
        g = img[j,i]
        img[j,i]= b[g]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
