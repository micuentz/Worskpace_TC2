#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:30:31 2020

@author: mariano
"""

import scipy.signal as sig
from pytc2.sistemas_lineales import analyze_sys, pretty_print_lti
import numpy as np
from math import log, sqrt, ceil

# Cargamos la funcion transferencia como vectores de sus coeficientes.
amax = 1
amin = 30
fp = 1
fs = 4

ee = 10**(amax/10) - 1
n = ceil(log(sqrt(((10**(amin/10))-1)/((10**(amax/10)-1))))/log(fs/fp))
omega_Butter = ee**(-1/(2*n))

butter = np.zeros(2*n + 1)
butter[-1] = 1
butter[0] = -1

aa = np.roots(butter)
raices = aa[ np.real(aa) < 0 ]

#print( raices )

poli1_0 = np.array([ 1, -raices[0] ])
poli1_1 = np.array([ 1, -raices[1] ])
poli1_2 = np.array([ 1, -raices[2] ])

poli_aux = np.polymul(poli1_0,poli1_1)

den = np.polymul( poli_aux , poli1_2 )

for i in range(n+1):
    den[i] = den[i]/(omega_Butter**(i))
    print(i,den[i])

print(den)

#num = np.array([ 1.96 ])
#den = np.array([ 1, 2.51, 3.14, 1.96 ])

#H1 = sig.TransferFunction( num, den )

#display(H1)

#plt.sca(bodePlot(H1))

#analyze_sys(H1,sys_name='TS3')