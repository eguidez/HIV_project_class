#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:45:41 2023

@author: emilieguidez
"""
import numpy as np
import matplotlib.pyplot as plt

# The equation is:
# V(t)=Aexp(-alpha *t)+Bexp(-beta*t)
# t is the time in days
# V is the viral load
time = np.linspace(0,1,101)
A = 10000
B =90000
alpha =100
beta =0.1

#Calculate the viral load
viral_load = A * np.exp(-alpha*time) + B * np.exp(-beta*time)

# Plot viral load
Astring = 'A= '+str(A)+'\n'
Bstring = 'B= '+str(B)+'\n'
alphastring = 'alpha= '+str(alpha)+'\n'
betastring = 'beta='+str(beta)+'\n'
sample=Astring + Bstring + alphastring + betastring
plt.plot(time,viral_load,label=sample)
plt.xlabel('Time (days)')
plt.ylabel('viral load')
plt.legend()

