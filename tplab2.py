# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 22:22:46 2023

@author: Tobias
"""
import pandas as pd
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt


pd.set_option('display.max_rows', None)

fs = 40000
nyq = 20000

cant_coef = 77

fpass = np.array([2000, 8000])
fstop = np.array([4000, 6000])
gpass = 1
gstop = 20 

frecs = [0.0,   fpass[0],     fstop[0],     fstop[1],     fpass[1],     nyq]
gains = [0,     0,     -gstop,     -gstop,      0,      0] 
gains = 10**(np.array(gains)/20)

fir_ls = sig.firls(cant_coef, frecs, gains, fs=fs)

np.set_printoptions(precision=20, suppress = True)
print("Coeficientes del filtro: \n")
print(fir_ls)

wrad, hh = sig.freqz(fir_ls, worN = 1000)
ww = wrad/np.pi * nyq

#------ Modulo ------
modulo = plt.figure()
plt.title('FIR LS: Modulo')
plt.plot(ww, 20 * np.log10(abs(hh)))
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Modulo [dB]')
plt.grid()
plt.show()

#------ Fase ------
fase = plt.figure()
plt.title('FIR LS: Fase')
angles = np.unwrap(np.angle(hh))
plt.plot(ww, angles)
plt.ylabel('Fase [rads]')
plt.xlabel('Frecuencia [Hz]')
plt.grid()
plt.show()