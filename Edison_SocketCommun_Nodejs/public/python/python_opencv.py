# -*- coding:UTF-8 -*-
#! /usr/bin/env python

import cv2
import sys
import thread
import time import localtime

if __name__ == "__main__":
    while True:
        capture = cv2.videoCapture(0)
        if capture.isOpen() is False:
            continue
        ret, image = capture.read()
        if ret == False:
            continue
        
