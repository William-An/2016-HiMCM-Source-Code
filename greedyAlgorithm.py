#This python file uses Greedy Algorithm to find the partial best-fit solution hoping to get the best-fit solution for entire problem
from Image2FilteredMat import *
import cv2
import numpy as np
import os
def cover(Kbest,Pbest): #Find partial best-fit solution based on the overlapping area and the covered area
    zero=np.zeros((imgMatDict[Kbest[1]].shape[0],imgMatDict[Kbest[1]].shape[1]),dtype=imgMatDict[Kbest[1]].dtype) #Create zero matrix
    for i in Kbest:
        if i ==0:continue
        zero+=imgMatDict[i]
    A=3.0
    bestmat=0
    temp=np.copy(zero)
    cover=-10
    #consider cover
    for i in Pbest:
        try:
            new=np.add(temp,imgMatDict[i])
        except KeyError:
            continue
        test=np.copy(new)
        valid_range = np.logical_not(zero[:,:] < 1)
        new[valid_range]=1
        if (np.sum(test)/np.sum(new)) < A and np.sum(new)>cover:
            A=np.sum(test)/np.sum(new)
            cover=np.sum(new)
            bestmat=i

    else:   return bestmat# ,np.sum(zero)

for i in image_files:
    imgMat=jpginRange(i,colorup,colordown,kernel)
    i=i.strip().split(".")[0]
    imgMatDict.setdefault(i, imgMat)
#temp=imgMatDict["AL35006"]
#ia=np.zeros((temp.shape[0],temp.shape[1]),dtype=temp.dtype)
r=[]
r.append(0)
best=[0,]
best.append("NH03607")

temp=[0,]
#temp.append(sorted([[np.sum(imgMatDict[x]),x] for x in imgMatDict]))
temp.append(sorted([[np.sum(imgMatDict[x]),x] for x in imgMatDict]))
for i in temp[1]:
    r.append(i[1])
r.reverse()
#greedy
for j in range(1,485):

    mat=cover(best,r)
        #q=max(q,r[i]+r[j-i])
    if mat!=0:
        best.append(mat)
        r.pop(r.index(mat))
print best
zero=np.zeros((imgMatDict.get(best[1]).shape[0],imgMatDict.get(best[1]).shape[1]),dtype=imgMatDict.get(best[1]).dtype)
for i in best:
    if i==0:continue
    im=imgMatDict.get(i)
    #cv2.imshow("sad",im)
    #print np.sum(im)
    valid_range = np.logical_not(im[:, :] == 1)
    im[valid_range]=0
    im[np.logical_not(valid_range)]=255
    zero+=im
cv2.imshow("sd",zero)
cv2.waitKey(0)
print len(best)
