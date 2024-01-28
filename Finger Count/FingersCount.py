import cv2
import time
import HandTrackingModule2 as htm
import os

wcam,hcam = 640,480
cap = cv2.VideoCapture(0)  
cap.set(3,wcam)
cap.set(4,hcam)

folderPath = "Finger Count\Fingers"
myList = os.listdir(folderPath)  #List the file name in the folder
print(myList)                      #
overlayList = [] #create a image object for each file
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)
pTime = 0

detector = htm.handDetector(detectionCon=0.7) #Create a hand track module
tipIds=[4,8,12,16,20] #ıds of the fingers tips
while True:
    ret,frame = cap.read()
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame,draw=False)
    if len(lmList) != 0: #if a hand detect
        fingers = [] # list to hold the number of finger
        
        #Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]: #If the tip is higher than the base, the thumb is considered raised (append 1 to fingers list)
            fingers.append(1)
        else:
            fingers.append(0)
        
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]: #Check whether the finger is open or not
                fingers.append(1)
            else:
                fingers.append(0)
        
        totalFingers=fingers.count(1) #The total value of the open fingers
        print(totalFingers)

        h,w,c = overlayList[totalFingers].shape
        frame[0:h,0:w]=overlayList[totalFingers] #Insert the image at specific coordinates

        cv2.rectangle(frame,(20,225),(170,425),(0,255,0),cv2.FILLED)
        cv2.putText(frame,str(totalFingers),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
    cTime = time.time()
    fps = 1/(cTime-pTime) #FPS
    pTime = cTime
    cv2.putText(frame,f'fps:{int(fps)}',(10,40),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()