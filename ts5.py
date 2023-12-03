# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:39:56 2023

@author: Tobias
"""

import numpy as np
import scipy.signal as sig
import math

amax = 0.5
amin = 24
omega_stop = 2.64

num = np.array([1])
den = np.array([ 1 , 0.2506 , 3.0614 , 0.507 , 3.0614 , 0.2506 , 1 ])

tf = sig.TransferFunction( num , den )

z,p,k = sig.tf2zpk(num,den)

print(p)

