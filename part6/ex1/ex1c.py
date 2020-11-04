#!/usr/bin/env python

import cv2
import numpy as np

#variaveis glovais :
raio =5
color =(0,0,0) # cor em bgr
pressed =False                      # para simumar o presionar o rato
tela=np.ones([500,500,3], 'uint8')*255


def click(event, x, y, flags, param):
    global pressed, color, tela
    # para o primeiro clique no ecra
    if event==cv2.EVENT_LBUTTONDOWN:
        pressed=True
        cv2.circle(tela, (x,y), raio, color,-1)
    # para execotar o desenhar enquanto presiona
    elif event==cv2.EVENT_MOUSEMOVE and pressed == True:
        cv2.circle(tela, (x, y), raio, color, -1)
    elif event== cv2.EVENT_LBUTTONUP:
        pressed=False



def main():
    global color
    window_name="pait"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, click)

    while True:
        cv2.imshow(window_name, tela)
        ch=cv2.waitKey(1)
        if ch & 0xFF==ord('q'):
            break

            # ????????????????????? nao sei porqie nao funciona
        elif ch & 0xFF ==ord('r'):
            color ==(0,0,255)
        elif ch & 0xFF == ord('b'):
            color == (255, 0, 0)
        elif ch & 0xFF == ord('g'):
            color == (0, 255, 0)
        elif ch & 0xFF == ord('w'):
            color == (255, 255, 255)










if __name__ == '__main__':
    main()