import cv2
from cards_information import *
import numpy as np
import matplotlib.pyplot as plt

def get_card():
    img = cv2.imread('screen.jpg', cv2.IMREAD_UNCHANGED)

    first_card = img[228:276,30:90]
    first_card = image_resize(first_card, 40, 32)
    cv2.imwrite('test_cards/cards/first_card.jpg', first_card)

    return first_card

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

get_card()
