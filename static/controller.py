import numpy as np
import cv2
img=cv2.imread("/content/pic.png")

#reflection across y axis
sh=img.shape
nimg=np.zeros((sh[0],sh[1],sh[2]))
for i in range(sh[0]):
  for j in range(sh[1]):
    nimg[i][sh[1]-j-1][0]=img[i][j][0]
    nimg[i][sh[1]-j-1][1]=img[i][j][1]
    nimg[i][sh[1]-j-1][2]=img[i][j][2]
if cv2.imwrite("/content/mirrory.png",nimg):
  print("Successful")
else:
  print("Failed")
 
#reflection across x-axis
img=cv2.imread("/content/pic.png")

sh=img.shape
nimg=np.zeros((sh[0],sh[1],sh[2]))
for i in range(sh[0]):
  for j in range(sh[1]):
    nimg[sh[0]-1-i][j][0]=img[i][j][0]
    nimg[sh[0]-1-i][j][1]=img[i][j][1]
    nimg[sh[0]-1-i][j][2]=img[i][j][2]
if cv2.imwrite("/content/mirrorx.png",nimg):
  print("Successful")
else:
  print("Failed")

 #rotate left by 90 degree
img=cv2.imread("/content/pic.png")
sh=img.shape
nimg=np.zeros((sh[1],sh[0],sh[2]))
for i in range(sh[0]):
  for j in range(sh[1]):
    nimg[sh[1]-1-j][i][0]=img[i][j][0]
    nimg[sh[1]-1-j][i][1]=img[i][j][1]
    nimg[sh[1]-1-j][i][2]=img[i][j][2]
if cv2.imwrite("/content/left90.png",nimg):
  print("Successful")
else:
  print("Failed")

 #rotate right by 90degree
img=cv2.imread("/content/pic.png")
sh=img.shape
nimg=np.zeros((sh[1],sh[0],sh[2]))
for i in range(sh[0]):
  for j in range(sh[1]):
    nimg[j][sh[0]-1-i][0]=img[i][j][0]
    nimg[j][sh[0]-1-i][1]=img[i][j][1]
    nimg[j][sh[0]-i-1][2]=img[i][j][2]
if cv2.imwrite("/content/right90.png",nimg):
  print("Successful")
else:
  print("Failed")

