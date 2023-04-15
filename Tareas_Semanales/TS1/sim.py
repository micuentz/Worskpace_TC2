#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:30:31 2020

@author: mariano
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np


# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

R1 = 1
R2 = 1
R3 = 1000 
C = 0.000001

my_tf = TransferFunction( [1,-R2/(R1*R3*C)], [1,1/(R3*C)] )


plt.close('all')

bodePlot(my_tf, fig_id=1, filter_description = '' )

pzmap(my_tf, fig_id=2, filter_description = '') #S plane pole/zero plot

GroupDelay(my_tf, fig_id=3, filter_description = '')
