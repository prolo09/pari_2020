#!/usr/bin/env python
import argparse
import cv2
from functools import partial
# Global variables
#window_name = 'window - Ex3a'
#image_gray = None


def onTrackbar(threshold, image_gray , window_name):
    _, I_bin= cv2.threshold(image_gray , threshold, 255, cv2.THRESH_BINARY)


    # para retirar coordenadas
    cv2.setMouseCallback(window_name, mouseCord)   # envoca as foncionalidade de poder usar o rato
    cv2.imshow(window_name, I_bin)


def mouseCord(event,x,y, flags,params):
    # funcao que me premite tirar cordenadas 

    if event==cv2.EVENT_LBUTTONDOWN:    # se o envent que e o que tem valore da matriz for igual a quando clico no rato ele printe os resultados
        print("clicou no esquerdo tem a cordenada:")
        print (x,y)


def main():

    window_name='window 3c'

    image_file_name="../imaguens/atlascar.png"

    I=cv2.imread(image_file_name, cv2.IMREAD_COLOR)



    image_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    Trackbar_nome='thersold'



    myOnTracbar=partial(onTrackbar, image_gray =image_gray , window_name=window_name)

    cv2.createTrackbar(Trackbar_nome, window_name, 0, 255, myOnTracbar)

    cv2.waitKey(0)




if __name__ == '__main__':
    main()


