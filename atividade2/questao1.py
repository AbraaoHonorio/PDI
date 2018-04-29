# -*- coding: utf-8 -*-
import cv2
import numpy as np


def convolve(image, kernel):
    # grab the spatial dimensions of the image, along with
    # the spatial dimensions of the kernel
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    # allocate memory for the output image, taking care to
    # "pad" the borders of the input image so the spatial
    # size (i.e., width and height) are not reduced
    pad = (kW - 1) / 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
                               cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")

    # loop over the input image, "sliding" the kernel across
    # each (x, y)-coordinate from left-to-right and top to
    # bottom
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            # extract the ROI of the image by extracting the
            # *center* region of the current (x, y)-coordinates
            # dimensions
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

            # perform the actual convolution by taking the
            # element-wise multiplicate between the ROI and
            # the kernel, then summing the matrix
            k = (roi * kernel).sum()

            # store the convolved value in the output (x,y)-
            # coordinate of the output image
            output[y - pad, x - pad] = k

    # # rescale the output image to be in the range [0, 255]
    # output = rescale_intensity(output, in_range=(0, 255))
    # output = (output * 255).astype("uint8")

    # return the output image
    return output


def readFile(filename, image, filter):
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    input = np.loadtxt(filename, dtype='i', delimiter=',')

    if(filter == 'blur'):
        height = len(input)
        width = len(input[0])
        input = np.array(input, dtype="float") * (float(input[0][0]) / (height * width))
        print(input)

    else:
        input = np.array(input, dtype="int")


    convoleOutput = convolve(imageGray, input)

    return convoleOutput
