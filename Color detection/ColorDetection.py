import cv2
import pandas as pd
import numpy as np

#Upload the color picture.
imgPath = "Color detection\color palette.jpg"
img = cv2.imread(imgPath)
img = cv2.resize(img,(700,500))


clicked = False
r = g = b = xpos = ypos = 0

#Upload the color data set
index=["color","color_name","hex","R","G","B"]
dataframe = pd.read_csv('Color detection\colors.csv',names=index,header=None)

df = dataframe.copy()
#print(df.head(5))

#Getting the color from data set when our mouse move the picture.
def getColorName(r,g,b):
    minimum  =1000
    for i in range(len(df)):
        d = abs(r - int(df.loc[i,"R"])) + abs(g - int(df.loc[i,"G"])) + abs(b - int(df.loc[i,"B"]))
        if (d<=minimum):
            minimum = d
            cname = df.loc[i,"color_name"]
    return cname


def draw_function(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global r,g,b,xpos,ypos,clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
        cv2.circle(img,(x,y),100,(255,0,0),-1)

cv2.namedWindow('color detection by programming_fever')
cv2.setMouseCallback('color detection by programming_fever',draw_function)

while True:
    cv2.imshow("Color detection by programming_fever",img)
    #
    if(clicked):
        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)

        text = getColorName(r,g,b) + 'R='+str(r) + 'G='+str(g) + 'B='+str(b)

        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        if(r+g+b >= 600):
            cv2.putText(img,text,(50,50),2,0.7,(0,0,0),2,cv2.LINE_AA)
        
        clicked = False
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
