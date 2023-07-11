# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 15:32:38 2023

@author: Tobias
"""

import math
import numpy as np
import scipy.signal as sig
from pytc2 import sistemas_lineales
from IPython.display import display, Math, Latex

amax = 0.5
amin = 20
omega_stop = 2

n_calc = math.log(math.sqrt(((10**(amin/10))-1)/((10**(amax/10)-1))))/math.log(omega_stop)

n = math.ceil(n_calc)

z,p,k = sig.buttap(n)
num, den = sig.zpk2tf(z, p, k)

tf = sig.TransferFunction(num, den)

sos = sig.tf2sos(num, den)

sistemas_lineales.pretty_print_SOS(sos)