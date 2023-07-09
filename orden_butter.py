# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 15:32:38 2023

@author: Tobias
"""

import math
import numpy as np
import scipy.signal as sig
import pytc2

amax = 3
amin = 17
omega_stop = 2

n_calc = math.log(math.sqrt(((10**(amin/10))-1)/((10**(amax/10)-1))))/math.log(omega_stop)

n = math.ceil(n_calc)

ee = 10**(0.1*amax) - 1

#num = np.array([ 0 , 0 , 1/ee ])
#den = np.array([ 1 , 0 , 1/ee ])

#tf = sig.TransferFunction( num , den )

#print(tf)

#sig.pretty_print_SOS( tf , mode='omegayq' )