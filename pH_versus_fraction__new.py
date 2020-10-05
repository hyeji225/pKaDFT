# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:55:25 2020

@author: USER
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set(font_scale=2.2)
sns.set_style("ticks")


n = 2                                   # 고려하는 분자의 수
a = []                                  # 모든 분자의 (F_1,F0)을 담을 list
for j in range(1,n+1):                  
    #title0 = input("molecule: GQD-")   # 분자
    k=str(j)
    Gp = float(input(k+'. Gp='))        # 입력
    Gdp = float(input(k+'. Gdp='))      # 입력
    GH = -270.29
    Ga = ((Gdp-Gp)*627.5095)
    pKa = (Ga+GH)*0.733362659135118
    pH = np.arange(0,14.1,0.1)
    F = []                              # 각 분자의 F_1,F0을 담을 list
    F_1 = 1/(1+10**(pKa-pH))
    F0 = 1-F_1
    F.append(F_1)
    F.append(F0)
    a.append(F)                         # (F_1,F0) #반복

b=a[0]                                  # 첫번째 분자의 (F_1,F0)
if n>1:
    for i in range(1,n):
        c=a[i]                          # i번째 분자의 (F_1,F0)
        b1=np.dot(b,c[0])               # 첫번째 분자의 (F_1,F0) * i번째 분자의 F_1
        b2=np.dot(b,c[1])               # 첫번째 분자의 (F_1,F0) * i번째 분자의 F_1
        b3=np.concatenate((b1,b2),axis=0) # 2^i 개의 fraction
        
        
        
"""
pKa0 = round(pKa,2)
pKa1 = str(pKa0)
GQD = "GQD-"
title1 = " , pKa= "
title = GQD + title0 + title1 + pKa1
    
plt.figure(1,figsize=(30,20),dpi=50)
plt.subplot(3,4,i)
plt.plot(pH,Fdp,'r',label='deprotonated')
plt.plot(pH,Fp,'black',label='protonated')
plt.xlabel('pH')
plt.ylabel('Fraction')
plt.xlim(0,14.01)
plt.ylim(-0.01,1.01)
plt.title(title,size=15)
plt.legend(loc='upper left')
    
plt.tight_layout()
plt.show()
"""