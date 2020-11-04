#!/usr/bin/env python

import cv2
import argparse
import numpy as np
from functools import partial

def escolhamodo():
    # funcao para escolher os modos
    esc_modo = argparse.ArgumentParser(description="escolhe modo de canis")
    esc_modo.add_argument('-hvs', help="moda para o modo hvs", action="store_true")
    arg_list=vars(esc_modo.parse_args())

    return arg_list['hvs']

#def onTrackbar(nada,image, windon_name):
 #   cv2.imshow(windon_name, image)
  #  print (nada)


def nothing(x):
    pass

def main():

    escolha=escolhamodo()

    windon_name='segmentacao'

    image_file='../imaguens/atlas2000_e_atlasmv.png'    #nome da imaguem
    image=cv2.imread(image_file, cv2.IMREAD_COLOR)      # importo a imaguem


    if escolha:
        image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


    #myOnTracbar = partial(onTrackbar, image=image, windon_name=windon_name)
    # criar as varias trackbar

    cv2.createTrackbar('min B/H', windon_name, 0, 255, nothing)
    cv2.createTrackbar('max B/H', windon_name, 0, 255, nothing)
    cv2.createTrackbar('min G/S', windon_name, 0, 255, nothing)
    cv2.createTrackbar('max G/S', windon_name, 0, 255, nothing)
    cv2.createTrackbar('min R/V', windon_name, 0, 255, nothing)
    cv2.createTrackbar('max R/V', windon_name, 0, 255, nothing)


    while True:

        # vou buscar o valor das variaveis
        minB_H=cv2.getTrackbarPos('min B/H', windon_name)
        maxB_H = cv2.getTrackbarPos('max B/H', windon_name)
        minG_S = cv2.getTrackbarPos('min G/S', windon_name)
        maxG_S = cv2.getTrackbarPos('max G/S', windon_name)
        minR_V = cv2.getTrackbarPos('min R/V', windon_name)
        maxR_V = cv2.getTrackbarPos('max R/V', windon_name)


        #separo a imaguem nos varios canais
        image_b, image_g, image_r = cv2.split(image)

        image_np_threshold_b= image_b>minB_H #and image_b<maxB_H
        image_np_threshold_r = (image_g > minG_S) #and (image_g < maxG_S)
        image_np_threshold_g = (image_r > minR_V) #and (image_r < maxR_V)

        new_image_b = image_np_threshold_b.astype(np.uint8)*255

        new_image_g = image_np_threshold_g.astype(np.uint8)*255

        new_image_r = image_np_threshold_r.astype(np.uint8)*255


        new_image = cv2.merge((new_image_b,new_image_r,new_image_g))

        cv2.imshow(windon_name, new_image)

# brincadeira para ver se dava com o treshold
    #image_b, image_g, image_r=cv2.split(image)
    #_, image_b_trs=cv2.threshold(image_b,50,255, cv2.THRESH_BINARY)
    #_, image_g_trs = cv2.threshold(image_g, 50, 255, cv2.THRESH_BINARY)
    #_, image_r_trs = cv2.threshold(image_r, 50, 255, cv2.THRESH_BINARY)


    #new_image=cv2.merge((image_b_trs,image_g_trs,image_r_trs))
    #cv2.imshow(windon_name,new_image)

        key=cv2.waitKey(1)
        if key==27:
            break

if __name__ == '__main__':
    main()