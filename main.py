import sys
import os
import ctypes
import cv2
print(cv2.__version__)

# FINDS THE VIDEO YOU WANT TO PLAY
selectedVideo= "video.mp4"
vid= cv2.VideoCapture(selectedVideo)

# CREATES FOLDER TO STORE FRAMES IN
if not os.path.exists('frames'):
    os.makedirs('frames')

# CURRENT FRAME THAT ITS ON
frameNumber= 0
while(True):
    # GET THE FRAME
    ret, frame= vid.read()
    # END OF FRAME
    if not ret:
        break
    # STORING THE CURRENT FRAME
    name= './frames/'+ str(frameNumber) + '.jpg'
    print('beep boop making frame number ')
    print(frameNumber)
    cv2.imwrite(name, frame)
    # NEXT FRAME
    frameNumber += 1
    ctypes.windll.user32.SystemParametersInfoW(20, 0, name, 0)
