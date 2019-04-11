# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 00:46:14 2019

@author: ASUS
"""
from math import sin,pi
import numpy as np
import matplotlib.pyplot as plt 
A=1
T=2*pi
sigma=0.04*A
x=np.linspace(0,200,201)
ita0=np.sin(x*2*pi/T)*A
h=1/300
E=np.random.normal(0,sigma,201)
ita=ita0+E
#d1=np.cos(x*2*pi/T)*A*2*pi/T
#d2=-np.sin(x*2*pi/T)*(A*2*pi/T)**2
detabar=np.zeros(199)
dE=np.zeros(199)
d2etabar=np.zeros(199)
d2E=np.zeros(199)
for i in range(1,200):
    detabar[i-1]=(ita0[i+1]-ita0[i-1])/2/h
for i in range(1,200):
    dE[i-1]=(E[i+1]-E[i-1])/2/h
mean=sum(dE)/len(dE)
ax1=plt.subplot(121)
ax1.plot(x[:-2],detabar,'b-')
ax1.plot(x[:-2],detabar+dE,'r-')
for i in range(1,200):
    d2etabar[i-1]=(ita0[i+1]-2*ita0[i]+ita0[i-1])/h/h
for i in range(1,200):
    d2E[i-1]=(E[i+1]-2*E[i]+E[i-1])/h/h
ax1=plt.subplot(122)
ax1.plot(x[:-2],d2etabar,'b-')
ax1.plot(x[:-2],d2etabar+d2E,'r-')
#噪音相较于普通值更容易影响峰值