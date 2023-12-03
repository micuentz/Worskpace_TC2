# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 16:29:24 2023

@author: tobias_guerrero
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from pytc2.sistemas_lineales import plot_plantilla

coef = 3001
den_fir = 1.0

ripple = 0.01
atenuacion = 40

fs = 1000
nyq = 500
ws1 = 1.0
wp1 = 3.0
wp2 = 25.0
ws2 = 35.0

ws = np.array([ws1 , ws2])
wp = np.array([wp1 , wp2])

frecs = [0.0 , ws1 , wp1 , wp2 , ws2 , nyq]
gains = [-atenuacion,-atenuacion,-ripple,-ripple,-atenuacion,-atenuacion]
gains = 10**(np.array(gains)/20)

taps = signal.firwin2(coef , frecs , gains , window = 'blackmanharris' , fs = fs)

w, h = signal.freqz(taps, den_fir, worN=1000)

ww = w / np.pi * nyq

phase = np.unwrap(np.angle(h))

gd = -np.diff(np.unwrap(np.angle(h)))/np.diff(ww)

t = np.arange(0 , 10 , 0.01)
imp = np.fft.ifft(h)

modulo = plt.figure()
plt.title("")
plt.plot(ww , 20*np.log10(abs(h)))
plt.axis([0,100,-50,5])
plot_plantilla(filter_type = 'bandpass' , fpass = wp , ripple = ripple , fstop = ws , attenuation = atenuacion, fs = fs)

fase = plt.figure()
plt.title("Fase")
plt.plot(ww, phase)
plt.show()

retardo = plt.figure()
plt.title("Retardo")
plt.plot(ww[1:], gd)
plt.axis([0,500,-4,0])
plt.show()

resp_impulso = plt.figure()
plt.title("Respuesta al impulso")
plt.plot(t,imp)
plt.show()