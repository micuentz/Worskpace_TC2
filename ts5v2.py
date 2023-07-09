# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:39:56 2023

@author: Tobias
"""

import scipy.signal as sig
import math
from pytc2.sistemas_lineales import pretty_print_lti,tf2sos_analog,pretty_print_SOS
from IPython.display import display, Math, Latex

amax = 0.5
amin = 24
omega_stop = 2.64
Q = 5

n_calc = (math.log(math.sqrt(4*((10**(0.1*amin) - 1)/(10**(0.1*amax) - 1)))))/(math.log(omega_stop+(math.sqrt((omega_stop**2)-1))))

n = math.ceil(n_calc)

ee = 10**(0.1*amax) - 1

z,p,k = sig.cheb1ap(n,amax)
num, den = sig.zpk2tf(z,p,k)

tf = sig.TransferFunction(num, den)

tf_bp = sig.lp2bp(num,den,bw=1/Q)

sos_bp = tf2sos_analog(tf_bp[0], tf_bp[1])

pretty_print_SOS(sos_bp,mode='omegayq')
#cheb = np.polynomial.chebyshev.Chebyshev((0,0,0,1))
#coef = np.polynomial.chebyshev.cheb2poly(cheb.coef)

#print(coef)



#num = np.array([1])
#den = np.array(coef)

#print(num)
#print(den)

#tf = sig.TransferFunction( num , den )

#pretty_print_SOS(tf, mode='omegayq')

