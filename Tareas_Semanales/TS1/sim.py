#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:30:31 2020

@author: mariano
"""

import scipy.signal as sig
from pytc2.sistemas_lineales import analyze_sys
import numpy as np
import math
from math import log, e, sqrt, ceil

# Cargamos la funcion transferencia como vectores de sus coeficientes.
amax = 1
amin = 12
fp = 1
fs = 2

ee = 10**(amax/10) - 1
n = ceil(log(sqrt(((10**(amin/10))-1)/((10**(amax/10)-1))))/log(fs/fp))



num = np.array([ 1.96 ])
den = np.array([ 1, 2.51, 3.14, 1.96 ])

H1 = sig.TransferFunction( num, den )

# mostramos la transferencia construida
#display(H1)

#plt.sca(bodePlot(H1))

analyze_sys(H1,sys_name='TS3')