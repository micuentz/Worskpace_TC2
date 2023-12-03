# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:39:56 2023

@author: Tobias
"""

import scipy.signal as sig
import math
from pytc2.sistemas_lineales import pretty_print_lti,tf2sos_analog,pretty_print_SOS,analyze_sys
from IPython.display import display, Math, Latex

amax = 2.5
amin = 15
omega_stop = 10
Q = 3

n_calc = (math.log(math.sqrt(4*((10**(0.1*amin) - 1)/(10**(0.1*amax) - 1)))))/(math.log(omega_stop+(math.sqrt((omega_stop**2)-1))))

n = math.ceil(n_calc)

z,p,k = sig.cheb1ap(n,amax)

num , den = sig.zpk2tf(z,p,k)

num_bp , den_bp = sig.lp2bp(num,den,1,1/Q)

tf_bp = tf2sos_analog(num_bp , den_bp)

pretty_print_SOS(tf_bp)

analyze_sys(tf_bp)