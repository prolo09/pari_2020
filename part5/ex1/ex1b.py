#!/usr/bin/env python

# part 3 exer1

# Pedro Rolo n-84803

import cv2
import argparse

#ex1 b)

def main():

    parser=argparse.ArgumentParser(description="ler imaguem")

    parser.add_argument('-imag1','--imaguem1', help='ver imaguem lida')
    parser.add_argument('-imag2', '--imaguem2', help='ver imaguem lida')

    args=parser.parse_args()
    args=vars(args)
    print(args)

    img1=cv2.imread(args['imaguem1'],1)
    img2 = cv2.imread(args['imaguem2'], 1)

    window_name='window'
    flip_flop=False

    while True:
        if flip_flop:
            cv2.imshow(window_name, img1)
            flip_flop=False

        else:
            cv2.imshow(window_name, img2)
            flip_flop=True

    cv2.waitKey(30)




if __name__ == '__main__':
    main()


