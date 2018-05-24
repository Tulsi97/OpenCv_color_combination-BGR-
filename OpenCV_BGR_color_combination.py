# -*- coding: utf-8 -*-
"""
Created on Thu May 24 19:36:09 2018

@author: hp-u
"""
import cv2
import numpy as np

def emptyFunction():
    pass

def main():
    
    img = np.zeros((720,720,3),np.uint8)
    windowName = 'OpenCV BGR color combination'

    cv2.namedWindow(windowName)

    cv2.createTrackbar('B' ,windowName, 0, 255,emptyFunction)
    cv2.createTrackbar('G' ,windowName, 0, 255,emptyFunction)
    cv2.createTrackbar('R' ,windowName, 0, 255,emptyFunction)

    while(True):                
        cv2.imshow(windowName,img)
    
        if cv2.waitKey(1) == 27:            
            break
    
        blue = cv2.getTrackbarPos('B' , windowName)
        green = cv2.getTrackbarPos('G' , windowName)
        red = cv2.getTrackbarPos('R' , windowName)
    
        img[:] = [blue,green,red]
        print(blue,green,red)
    cv2.destroyAllWindows()   

if __name__ == "__main__":
    main()
   
    
