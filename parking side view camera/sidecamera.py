from itertools import count
import numpy as np
import cv2
from copy import copy
import pickle
import cvzone

#events=[i for i in dir(cv2) if'EVENT' in i]
#print(events)
cap = cv2.VideoCapture('carPark.mp4')

def empty(a):
    pass
 
 
#cv2.namedWindow("Vals")
#cv2.resizeWindow("Vals", 640, 240)
#cv2.createTrackbar("Val1", "Vals", 43, 50, empty)
#cv2.createTrackbar("Val2", "Vals", 20, 20, empty)
#cv2.createTrackbar("Val3", "Vals", 1, 1, empty)

counter = 0
myList = []
List = []

width, height = 598, 250

try:
    with open('parkingSlots', 'rb') as f:
        myList = pickle.load(f)
        print(myList)
except:
    myList = []

def checkSpaces():
    global width
    global height
    spaces = 0
    for pos in myList:
        x, y = pos[1]
        w, h = width, height
        pts1 = np.float32([list(pos[1]),list(pos[0]),list(pos[2]),list(pos[3])])
        pts2 = np.float32([[0,0],[w, 0],[0, h],[w, h]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgCrop = cv2.warpPerspective(imgThres, matrix, (w, h))
        #imgCrop = imgCrop[0:h, 0:w]
        #cv2.imshow(f"{list(pos[1])}", imgCrop)
        
        count = cv2.countNonZero(imgCrop)
 
        if count < 49000:
            color = (0, 200, 0)
            thic = 5
            spaces += 1
 
        else:
            color = (0, 0, 200)
            thic = 2
 
        #cv2.rectangle(img, (x, y), (x + w, y + h), color, thic)
 
        cv2.putText(img, str(cv2.countNonZero(imgCrop)), (x, y), cv2.FONT_HERSHEY_PLAIN, 1,
                    color, 1)
 
    cvzone.putTextRect(img, f'Free: {spaces}/{len(myList)}', (50, 60), thickness=3, offset=20,
                       colorR=(0, 200, 0))



    
    
    #cv2.waitKey(0)
while True:
    success, img = cap.read()
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    img=cv2.resize(img,(700, 500))
    for List in myList:
        for i, point in enumerate(List):
            start_point = point
            end_point = List[(i+1) % 4]
            img = cv2.line(img, start_point, end_point, (255,255,0), 1)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    #imgBlur = imgGray
    # ret, imgThres = cv2.threshold(imgBlur, 150, 255, cv2.THRESH_BINARY)

    #val1 = cv2.getTrackbarPos("Val1", "Vals")
    #val2 = cv2.getTrackbarPos("Val2", "Vals")
    #val3 = cv2.getTrackbarPos("Val3", "Vals")
    #if val1 % 2 == 0: val1 += 1
    #if val3 % 2 == 0: val3 += 1
    imgThres = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY_INV, 43, 20)
    imgThres = cv2.medianBlur(imgThres, 1)
    kernel = np.ones((3, 3), np.uint8)
    imgThres = cv2.dilate(imgThres, kernel, iterations=1)

    checkSpaces()
    # Display Output

    cv2.imshow("Image", img)
    #cv2.imshow("ImageGray", imgThres)
    #cv2.imshow("ImageBlur", imgBlur)
    cv2.waitKey(1)
