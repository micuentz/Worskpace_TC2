# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:29:53 2023

@author: tobias_guerrero
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from pytc2.sistemas_lineales import analyze_sys, plot_plantilla

ripple = 0
atenuacion = 40

fs = 1000
nyq = 500
ws1 = 1.0
wp1 = 3.0
wp2 = 25.0
ws2 = 35.0

ws = np.array([ws1 , ws2])
wp = np.array([wp1 , wp2])

frecs = np.array([0.0 , ws1 , wp1 , wp2 , ws2 , nyq]) / nyq
gains = np.array([-atenuacion , -atenuacion , -ripple , -ripple , -atenuacion , -atenuacion])
gains = 10**(gains/20)

plt.axis([0,100,-50,5])
plot_plantilla(filter_type = 'bandpass' , fpass = np.array([wp1,wp2]) , ripple = ripple , fstop = np.array([ws1,ws2]) , attenuation = atenuacion)#, fs = fs)