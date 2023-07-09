# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 15:32:38 2023

@author: Tobias
"""

import math
import numpy as np
import scipy.signal as sig
import pytc2

amax = 2.5
amin = 15
omega_stop = 29.7

n_calc = (math.log(math.sqrt(4*((10**(0.1*amin) - 1)/(10**(0.1*amax) - 1)))))/(math.log(omega_stop+(math.sqrt((omega_stop**2)-1))))



ee = 10**(0.1*amax) - 1

num = np.array([ 0 , 0 , 1/ee ])
den = np.array([ 1 , 0 , 1/ee ])

tf = sig.TransferFunction( num , den )

print(tf)

sig.pretty_print_SOS( tf , mode='omegayq' )