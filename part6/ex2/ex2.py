#!/usr/bin/env python

import cv2



def main():

    cap =cv2.VideoCapture(0)
    cv2.namedWindow('Frame', cv2.WINDOW_AUTOSIZE)

    while True:
        _,frame=cap.read()
        cv2.imshow('Frame',frame)

        key=cv2.waitKey(1)
        if key==27:
            break



if __name__ == '__main__':
    main()