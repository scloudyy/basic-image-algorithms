# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 18:20:08 2016

@author: scloudyy
"""

import numpy as np

def convolution(input, kernel):
    height, width = np.shape(input)
    kHeight, kWidth = np.shape(kernel)
    output = np.zeros([height, width])
    rH = int((kHeight - 1) / 2)
    rW = int((kWidth - 1) / 2)

    inputFill = np.zeros([height + 2 * rH, width + 2 * rW])
    iBegin = rH
    iEnd = height + rH
    jBegin = rW
    jEnd = width + rW
    inputFill[iBegin:iEnd, jBegin:jEnd] = input[:, :]

    for i in range(iBegin, iEnd):
        for j in range(jBegin, jEnd):
            k = np.sum(inputFill[i-rH:i+rH+1, j-rW:j+rW+1] * kernel[:, :])
            output[i - rH, j - rW] = k

    return output

