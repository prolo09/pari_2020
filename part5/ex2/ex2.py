#!/usr/bin/env python

import cv2

def main():
    # load image
    image_rgb=cv2.imread('../imaguens/atlas2000_e_atlasmv.png',1)
    window_name='my_windows'

    # converte rgb to gray
    image_gray= cv2.cvtColor(image_rgb, cv2.COLOR_BGR2BGRA)


    window_name='my_window'
    cv2.imshow(window_name,image_gray )


    # C)

    image_b, image_g, image_r =cv2.split(image_rgb)

    _,image_b_theshold










if __name__ == '__main__':
    main()





