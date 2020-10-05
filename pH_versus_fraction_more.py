# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:29:58 2020

@author: marine
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set(font_scale=3)
sns.set_style("ticks")


data = pd.read_excel ('C54-OH.xlsx')


x = data.loc[:, ['pH']]
y1 = data.loc[:, ['F-1']]
y0 = data.loc[:, ['F0']]


#plt.figure(1,figsize=(8,8),dpi=60)


plt.plot(x,y1,'r',label='F-1')
plt.plot(x,y0,'black',label='F0')

plt.xlabel('pH')
plt.ylabel('Fraction')

plt.legend(loc='upper left')

plt.xlim(0,14.01)
plt.ylim(-0.01,1.01)

plt.title("GQD-OH(pKa=8.95)",size=15)

