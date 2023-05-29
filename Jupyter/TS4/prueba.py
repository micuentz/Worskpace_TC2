# -*- coding: utf-8 -*-
"""
Created on Sun May 28 20:14:59 2023

@author: Tobias
"""

from scipy.signal import TransferFunction
from pytc2.sistemas_lineales import analyze_sys
from numpy import polymul

num1 = [ 0 , 0.8 , 0 ]
den1 = [ 0 , 1 , 0.8]

num2 = [ 0.64 , 0 , 0 ]
den2 = [ 1 , 0.8 , 0.64 ]

num = polymul(num1,num2)
den = polymul(den1,den2)

H1 = TransferFunction( num, den )

print(den)

analyze_sys(H1,sys_name='TS4')