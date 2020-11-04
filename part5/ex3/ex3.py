import argparse
import cv2

# Global variables
window_name = 'window - Ex3a'
image_gray = None


def onTrackbar(threshold):
    _, I_bin= cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, I_bin)




def main():

    image_file_name="../imaguens/atlascar.png"

    I=cv2.imread(image_file_name, cv2.IMREAD_COLOR)

    global image_gray # use global var

    image_gray = cv2.cvtColor(I, cv2.COLOR_BGR2GRAY)  # convert bgr to gray image (single channel)
    cv2.namedWindow(window_name)

    Trackbar_nome='thersold'

    cv2.createTrackbar(Trackbar_nome, window_name, 0, 255, onTrackbar)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()





















