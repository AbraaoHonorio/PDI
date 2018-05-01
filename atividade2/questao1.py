# -*- coding: utf-8 -*-
import cv2
import numpy as np


def convolve(image, kernel):
    
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    
    pad = (kW - 1) / 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
                               cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype="float32")

   
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            
            roi = image[y - pad:y + pad + 1, x - pad:x + pad + 1]

            
            k = (roi * kernel).sum()

            
            output[y - pad, x - pad] = k

    
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
