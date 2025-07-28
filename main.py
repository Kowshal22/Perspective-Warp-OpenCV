import numpy as np
import cv2
import os

img=cv2.imread(os.path.join(os.getcwd(),'img.png'))
width,height=477,500
pts1=np.float32([[280,121],[444,134],[274,352],[447,366]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
final=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow('original',img)
cv2.imshow('final',final)
cv2.imshow("Stacked", np.hstack([img, final]))
cv2.waitKey(0)
cv2.destroyAllWindows()