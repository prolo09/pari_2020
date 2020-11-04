#!/usr/bin/env python

import cv2
from functools import partial

window_name = 'exer1- circulo'
raio=40


def drawcirculo(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(window_name,(x,y),raio,(0,255,0), -1 )



def main():

    imag_file='../imaguens/atlascar.png'
    image=cv2.imread(imag_file,cv2.IMREAD_COLOR)
    cv2.namedWindow(window_name)





    cv2.setMouseCallback(window_name, drawcirculo)   # envoca as foncionalidade de poder usar o rato
    #cv2.setMouseCallback(window_name, partial(drawcirculo, window_name=window_name))

    cv2.imshow(window_name, image)
    cv2.waitKey(0)








if __name__ == '__main__':
    main()