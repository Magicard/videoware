import cv2
import os
import ctypes
import sys


cwd= os.getcwd()
path= "C:/Users/Teo/Desktop/Video Malware/frames/62.jpg"
ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)