#!/usr/bin/env python

# part 3 exer1

# Pedro Rolo n-84803

import cv2

#ex1 a)

def main():

    image_filename='atlascar2.png'
    image=cv2.imread(image_filename, cv2.IMREAD_COLOR)        # load a image

    cv2.imshow('window', image)
    cv2.waitKey(0)

    exit



if __name__ == '__main__':
    main()


