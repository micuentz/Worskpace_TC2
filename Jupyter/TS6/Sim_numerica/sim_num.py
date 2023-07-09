# -*- coding: utf-8 -*-
"""
@author: Tobias Guerrero

Simulación numérica TS6

"""

import numpy as np
import scipy.signal as sig
from pytc2.sistemas_lineales import analyze_sys


wc = 1 # frecuencia de corte
w0 = 1/3 # frecuencia del cero de transmision

# El orden se determino mediante criterio
n = 3

z,p,k = sig.buttap(n)
num_LP , den_LP = sig.zpk2tf(z,p,k) # Transferencia pasabajos

num_LP = np.array([ 1 , 0 , w0**2 , 0 ]) # Modifico el numerador para incorporar los ceros de transmision

num_HP , den_HP = sig.lp2lp( num_LP , den_LP ) # Transformo a pasa-altos

tf_HP = sig.TransferFunction( num_HP , den_HP )

analyze_sys(tf_HP) # Grafico