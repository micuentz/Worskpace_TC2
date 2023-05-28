
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
from pytc2.sistemas_lineales import analyze_sys, tf2sos_analog
from pytc2.general import Chebyshev_polynomials

ee = 0.31

cw = Chebyshev_polynomials(5)

cw2 = np.polymul(cw,cw)

cw10 = cw2 * ee
cw10[-1] = cw10[-1] + 1

display(cw10)

num = np.array([ 1 ])
den = np.array([ 24.6, 0, -61.5, 0, 44.2, 0, -9.6, 0, 2.4, 0, 1 ])



display(np.roots(cw2))

#H1 = sig.TransferFunction( num, den )

# mostramos la transferencia construida
#display(H1)

#plt.sca(bodePlot(H1))

#analyze_sys(H1,sys_name='TS3')