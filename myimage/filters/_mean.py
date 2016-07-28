# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 21:04:10 2016

@author: scloudyy
"""

import numpy as np
from myimage import common

def mean(input, size = 3):
    height, width, channel = np.shape(input)
    output = np.zeros([height, width, channel])
    kernal = np.zeros([size, size])
    kernal[0:size, 0:size] = 1
    kernal = kernal / np.sum(kernal)

    output = common.convolution(input, kernal)

    return output
