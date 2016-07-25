# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 14:53:56 2016

@author: scloudyy
"""

import os
from skimage import io, img_as_float
from myimage import filters

inputDir = 'inputs/'
outputDir = 'outputs/'

inputNames = os.listdir(inputDir)
filter(lambda x: ('.bmp' in x) or ('.jpg' in x) or ('.png' in x),
                inputNames)

for inputIndex in range(len(inputNames)):
    inputName = inputNames[inputIndex]
    input = img_as_float(io.imread(inputDir + inputName))

    outputGaussian = filters.gaussian(input)
    io.imsave(outputDir + inputName + '_gaussian.bmp', outputGaussian)
