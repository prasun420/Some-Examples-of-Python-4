s="aaba"
length_s=len(s)
#print(s[-1])
if length_s%2==0:
    mid=int(length_s/2)
    s1=s[0:mid]
    s2=s[mid:]
    #print(s1)
    #print(s2)
    if (s1[::-1]==s1) or (s2[::-1]==s2) or (s[::-1]==s):
        print("This is a Halindrome")
    else:
        print("NO")

elif length_s%2!=0:
    if s[::-1]==s:
        print("this is halindrome")
        
        
        
        
        
  #open cv code      
         import cv2
import numpy as np 
import time
video=cv2.VideoCapture(0,cv2.CAP_DSHOW)
time.sleep(3)
for i in range(60):
    check,background = video.read()
background = np.flip(background, axis=1)

while(video.isOpened()):
    check,img=video.read()
    if check==False:
        break
    img=np.flip(img,axis=1)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,120,50])
    upeer_red=np.array([10,255,255])
    mask1=cv2.inRange(hsv,lower_red, upeer_red)
    
