#! python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:11:42 2019
@author: Tech
Julian Daniel
"""

import numpy as np
import pylab as plt


xValues = np.array(list(range(11)))
dubValues = [5]
fiveValues = [21]

for i in range(10):
    dubValues.append(dubValues[-1] * 2)
    fiveValues.append(fiveValues[-1] + 5)
    
    
    
plt.plot(xValues, dubValues)
plt.plot(xValues, fiveValues)
plt.show()