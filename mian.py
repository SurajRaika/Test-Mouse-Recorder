from PIL import ImageGrab
import pyautogui
import numpy as np
import cv2
import ctypes
import time
user32 = ctypes.windll.user32   
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
prevTime = 0
print(user32.GetSystemMetrics(2))
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Recording1.avi',fourcc, 8.0, (1600,900))
print(screensize)
height = int(input("enter width"))
width = int(input("enter height"))
Xs = [0,8,6,14,12,4,2,0]
Ys = [0,2,4,12,14,6,8,0]
while(True):
    
    MouseX , MouseY = pyautogui.position()    
    img = ImageGrab.grab(bbox=(1,1,int(screensize[0]),int(screensize[1]))) #bbox specifies specific region (bbox= x,y,width,height)
    img_np = np.array(img)
    img_np=img_np[:, :, ::-1].copy()

    currTime = time.time()
    fps = 1 / (currTime - prevTime)
    prevTime = currTime
    # cv2.putText(img_np , "👆",(MouseX - 10 ,MouseY - 10 ),cv2.FONT_HERSHEY_DUPLEX , 2 , (255,0,0),1)
    
    Xthis = [1*x+MouseX for x in Xs]
    Ythis = [1*y+MouseY for y in Ys]
    points = list(zip(Xthis,Ythis))
    points = np.array(points, 'int32')
    cv2.fillPoly(img_np,[points],color=[255,255,255])
    if MouseX < width :
        MouseX = width
    elif MouseX > ((screensize[0]) - width):
        MouseX = ((screensize[0]) - width)
    if MouseY < height :
        MouseY = height
    elif MouseY > ((screensize[1]) - height):
        MouseY = ((screensize[1]) - height)
    
    img_np=img_np[ MouseY - height : MouseY + height   , MouseX - width : MouseX + width].copy()
    cv2.putText(img_np, f'FPS: {int(fps)}', (1,13), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 1)
    cv2.imshow("test", img_np)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        cv2.destroyAllWindows()
        break

