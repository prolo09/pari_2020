#!/usr/bin/env python

import cv2

import readchar


def main():

    # -------------
    #    initial
    #______________

    cap =cv2.VideoCapture(0)
    cv2.namedWindow('Frame', cv2.WINDOW_AUTOSIZE)

    #--------------
    #    body
    #--------------
    while True:
        ins_letter = readchar.readchar()  # pede para inserir uma letra
        asrletter = ord(ins_letter)
        _,frame=cap.read()

        if asrletter==32:
            break
    cv2.imshow('Frame', frame)
    cv2.waitKey(0)

    #----------------
    #      end
    #----------------





if __name__ == '__main__':
    main()