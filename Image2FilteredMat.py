import cv2
import numpy as np
import os
imgMatDict=dict()
image_files=os.listdir("mapjpg")#Get the list of image filenames
#print image_files
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
colorup=np.array([124,235,255])
colordown=np.array([0,193,211])
def jpginRange(jpgName,upper_Bond,lower_Bond,kernel):
    img = cv2.imread("mapjpg\\"+jpgName)
    res = cv2.inRange(img, lower_Bond,upper_Bond)  # from stackoverflow: http://stackoverflow.com/questions/7722519/fast-rgb-thresholding-in-python-possibly-some-smart-opencv-code
    res = cv2.dilate(res, kernel)
    #cv2.imshow("ghj",res)
    #cv2.waitKey(0)
    return res
for i in image_files:
    imgMat=jpginRange(i,colorup,colordown,kernel)
    i=i.strip().split(".")[0]
    imgMatDict.get(i,imgMat)
