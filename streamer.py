"""
Author: G.Sfikas
Date:   Nov 2017

Get input from camera, perform some image processing frame-by-frame, and show the result realtime
"""

import numpy as np
from scipy import signal
import cv2


def meanFilterGeneric(inputCaret, windowsize):
    convolution_kernel = np.ones([windowsize, windowsize]) / (windowsize ** 2.)
    return linearFilter(inputCaret, convolution_kernel)

def identityFilter(inputCaret):
    return inputCaret

def linearFilter(inputCaret, convolution_kernel):
    return signal.convolve2d(inputCaret, convolution_kernel, mode='full', boundary='fill', fillvalue=0)

def meanFilter(inputCaret):
    return meanFilterGeneric(inputCaret, 7)

def laplacianFilter(inputCaret):
    convolution_kernel = np.array([
        [0., 1., 0.],
        [1., -4.,1.],
        [0., 1., 0.]
    ])
    return linearFilter(inputCaret, convolution_kernel)

def horizontalSobelFilter(inputCaret):
    convolution_kernel = np.array([
        [1., 0.,-1.],
        [2., 0.,-2.],
        [1., 0.,-1.]
    ])
    return linearFilter(inputCaret, convolution_kernel)

def verticalSobelFilter(inputCaret):
    convolution_kernel = np.array([
        [1., 0.,-1.],
        [2., 0.,-2.],
        [1., 0.,-1.]
    ])
    convolution_kernel = convolution_kernel.T
    return linearFilter(inputCaret, convolution_kernel)


def normalizeProcessedImage(A):
    A = A - np.min(A)
    A = (A / np.max(A)) * 255.
    return np.uint8(np.round(A))

def isKeyPressed(key):
    return cv2.waitKey(1) & 0xFF == ord(key)

if __name__=='__main__':
    processCaret = verticalSobelFilter #identityFilter
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