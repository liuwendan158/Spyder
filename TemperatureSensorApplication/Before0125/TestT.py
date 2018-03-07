# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:20:39 2017

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:32:25 2017

@author: user
"""


import serial
import numpy as np
from time import time
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import Series,DataFrame
#from pylab import rcParams


M=np.zeros((50,50))
T0=np.zeros((50,50))
T1=np.zeros((50,50))
a=np.zeros((50,50))
b=np.zeros((50,50))

port = "COM29"
baud = 500000
temp = 0b101111
data = 0
header = 0
PressureArray=[]
X=[x for x in range(50)]
Y=[y for y in range(50)]
x,y=np.meshgrid(X, Y)
#fig=plt.figure()
#plt.axes().set_aspect('equal')
row=0



          #plt.contourf(x,y,df, 50, cmap=plt.cm.jet,vmin=0, vmax=700)                             
            #plt.show()
           
ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
     print(ser.name + ' is open...')

s='read data point 0'+'\n'
l=[ord(c) for c in s]
ser.write(l)
for i in range(50):
    header=0
    data1=0
    row=0
    while(header != b'\xff'):
        header = ser.read(1)
    header=0
    data1=ser.read(2)
    if(data1==b'\xff\xff'):
        row=int.from_bytes(ser.read(1),'little')
        if row>50:
            break;
        for j in range(50):
            data=int.from_bytes(ser.read(2),byteorder='big')
                    #data2=((330 / (0.244141 * data/ 1000 + 2) * 10 - 100 - 800) / 8.7298)
            if data==0:
                data2=0;
            else:
                data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
            T0[row,j]=data2
print(T0)          
    
s='read data point 1'+'\n'
l=[ord(c) for c in s]
ser.write(l)
for i in range(50):
    header=0
    data1=0
    row=0
    while(header != b'\xff'):
        header = ser.read(1)
    header=0
    data1=ser.read(2)
    if(data1==b'\xff\xff'):
        row=int.from_bytes(ser.read(1),'little')
        if row>50:
            break;
        for j in range(50):
            data=int.from_bytes(ser.read(2),byteorder='big')
                    #data2=((330 / (0.244141 * data/ 1000 + 2) * 10 - 100 - 800) / 8.7298)
            if data==0:
                data2=0;
            else:
                data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
            T1[row,j]=data2
print(T1)

y=np.array([25.,55.])
for i in range(50):
    for j in range(50):
        x=np.array([T0[i,j],T1[i,j]])
        if(T0[i,j]>0 and T1[i,j]>0):
            f = np.polyfit(x,y,1)
            p= np.poly1d(f)
            a[i,j]=p[1]
            b[i,j]=p[0]
        
print(a)
print(b)



