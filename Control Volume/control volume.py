import cv2
import time
import numpy as np
import handtrackingmodule2 as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wcam,hcam = 640,480
cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
pTime = 0
detector = htm.handDetector()

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
#volume.GetMute()
#volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-5.0, None)
minvol = volRange[0]
maxvol = volRange[1]
vol = 0
volBar = 400
while True:
    ret,frame = cap.read()
    frame = detector.findHands(frame)
    lmlist = detector.findPosition(frame,draw=False)
    #print(lmlist)
    if len(lmlist) != 0:

        x1, y1 = lmlist[4][1], lmlist[4][2] 
        x2, y2 = lmlist[8][1], lmlist[8][2]   #Detection the fingertips
        
        x3, y3 = (x1+x2)//2 , (y1+y2)//2
        cv2.circle(frame,(x1,y1),15,(255,0,255), cv2.FILLED)
        cv2.circle(frame,(x2,y2),15,(255,0,255), cv2.FILLED)
        cv2.line(frame,(x1,y1),(x2,y2),(255,0,255),3)
        cv2.circle(frame,(x3,y3),15,(0,255,255), cv2.FILLED)
        
        length = math.hypot(x1-x2 , y1-y2)
        #print(length)

        vol = np.interp(length,[50,300],[minvol, maxvol])
        volBar = np.interp(length,[50,300],[400, 150])
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)



    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.rectangle(frame,(50,150),(85,400),(0,255,0),3)
    cv2.rectangle(frame,(50,int(volBar)),(85,400),(0,255,0),cv2.FILLED)
    cv2.putText(frame,f'fps:{int(fps)}',(10,40),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()