import sys
import os
import cv2
print(cv2.__version__)

#FINDS THE VIDEO YOU WANT TO PLAY
selectedVideo= "video.mp4"
vid= cv2.VideoCapture(selectedVideo)

#CREATES FOLDER TO STORE FRAMES IN
if not os.path.exists('frames'):
    os.makedirs('frames')

whi