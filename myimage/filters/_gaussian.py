# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 23:03:09 2016

@author: scloudyy
"""

import numpy as np
from myimage import common

def gaussian(input, size = 5, theta = 1):
    height, width, channel = np.shape(input)
    output = np.zeros([height, width, channel])
    kernal = np.zeros([size, size])
    center = (size - 1) / 2

    for i in range(size):
        for j in range(size):
            k = np.exp(- ((i - center)**2 + (j - center)**2) /
                       (2 * theta**2))
            kernal[i, j] = k
    kernal = kernal / np.sum(kernal)

    for c in range(channel):
        output[:,:,c] = common.convolution(input[:,:,c], kernal)

    return output