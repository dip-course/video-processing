"""
Author: G.Sfikas
Date:   Nov 2017

Get input from camera, perform some image processing frame-by-frame, and show the result realtime
'Skeleton' version of the more complete 'streamer.py'.
"""

import numpy as np
from scipy import signal
import cv2


def identityFilter(inputCaret):
    return inputCaret

def normalizeProcessedImage(A):
    return np.uint8(np.round(A))

def isKeyPressed(key):
    return cv2.waitKey(1) & 0xFF == ord(key)

if __name__=='__main__':
    processCaret = identityFilter
    cap = cv2.VideoCapture(0)
    while(True):
        caret_ok, caret = cap.read() # caret: Numpy array containing current frame
        if not caret_ok:
            continue
        caret_gray = cv2.cvtColor(caret, cv2.COLOR_BGR2GRAY)
        caret_processed = processCaret(np.float32(caret_gray))
        cv2.imshow('frame', normalizeProcessedImage(caret_processed))
        if isKeyPressed(' '):
            break

    cap.release()
    cv2.destroyAllWindows()