# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:29:53 2023

@author: tobias_guerrero
"""

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from pytc2.sistemas_lineales import plot_plantilla

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

num , den = signal.iirdesign(wp , ws , ripple , atenuacion, ftype = "butter", output = 'ba', fs = fs)

sos = signal.iirdesign(wp , ws , ripple , atenuacion, ftype = "butter", output = 'sos', fs = fs)

w, h = signal.sosfreqz(sos, worN=1000)

ww = w / np.pi * nyq

phase = np.unwrap(np.angle(h))

wd , gd = signal.group_delay([num,den], fs = fs)
fd = wd / 2*np.pi

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
plt.axis([0,100,-50,5])
plt.show()

retardo = plt.figure()
plt.title("Retardo")
plt.plot(fd, gd)
plt.show()

resp_impulso = plt.figure()
plt.title("Respuesta al impulso")
plt.plot(t,imp)
plt.show()