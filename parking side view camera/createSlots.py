from itertools import count
import numpy as np
import cv2
from copy import copy
import pickle
import os

#events=[i for i in dir(cv2) if'EVENT' in i]
#print(events)

counter = 0
myList = []
List = []
cwd=os.path.dirname(os.path.realpath(__file__))
try:
    with open(cwd+'\parkingSlots', 'rb') as f:
        myList = pickle.load(f)
        #print(myList)
except:
    myList = []

def click_event(event,x,y,flags,param):
    global original
    global counter
    global img
    global List
    global myList
    if event==cv2.EVENT_LBUTTONDOWN:
        if(counter == 0):
            List = []
            img = copy(original)
        counter += 1
        List.append((x, y))
        #print(myList)
        #font=cv2.FONT_HERSHEY_SIMPLEX
        #strXY=str(x)+', '+str(y)
        #cv2.putText(img,strXY,(x,y),font,.5,(255,255,0),2)
        cv2.circle(img, (x,y), 2, (255,255,0), 2)
        cv2.imshow('image',img)
        if(counter % 4 == 0):
            myList.append(List)
            counter = 0
        
    if event==cv2.EVENT_RBUTTONDOWN:
        with open(cwd+'\parkingSlots', 'wb') as f:
            pickle.dump(myList, f)


def click_event_second(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        mycolorImage=np.zeros((512,512,3),np.uint8)
        mycolorImage[:]=[blue,green,red]
        cv2.imshow('color',mycolorImage)



#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread(cwd+'\carPark.jpg')
img=cv2.resize(img, (700, 500))
original = copy(img)


cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
