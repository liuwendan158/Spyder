# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:18:04 2017

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
T2=np.zeros((50,50))
T3=np.zeros((50,50))
T4=np.zeros((50,50))
T5=np.zeros((50,50))
T6=np.zeros((50,50))
T7=np.zeros((50,50))
a=np.zeros((50,50))
b=np.zeros((50,50))
c=np.zeros((50,50))

port = "COM5"
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

def ReadCal():
    global T0,T1,T2,T3,T4,T5,T6,T7,a,b,c
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
                if data==0:
                    data2=0;
                else:
                    data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                T1[row,j]=data2
    print(T1)
    
    s='read data point 3'+'\n'
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
                if data==0:
                    data2=0;
                else:
                    data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                T3[row,j]=data2
    print(T3)
  
    s='read data point 4'+'\n'
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
                if data==0:
                    data2=0;
                else:
                    data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                T4[row,j]=data2
    print(T4)
      
    y=np.array([25.,35.,40.])
    for i in range(50):
        for j in range(50):
            x=np.array([T1[i,j],T3[i,j],T4[i,j]])
            if(T1[i,j]>0 and T3[i,j]>0 and T4[i,j]>0):
                f = np.polyfit(x,y,2)
                p= np.poly1d(f)
                a[i,j]=p[2]
                b[i,j]=p[1]
                c[i,j]=p[0]
  
def DoCal(row,j,data2):
    data=a[row,j]*data2*data2+b[row,j]*data2+c[row,j]
    return data
    
    
def animate():
    TemData = np.zeros((50,50))
    while 1:
        for i in range(50):
            header=0
            data1=0
            row=0
            before=0.
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
                    '''if data==0:
                        if j<16:
                            data3=before
                        else:
                            data3=0
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                        data3=DoCal(row,j,data2)
                    TemData[row,49-j] = data3
                    before=data3
                row=0
                ser.read(1)
                data1=0'''
                    if data==0:
                        data2=0
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                    TemData[row,49-j] = data2
                row=0
                ser.read(1)
                data1=0
                
                #ListData=TemData.tolist()
        yield TemData

            #plt.contourf(x,y,df, 50, cmap=plt.cm.jet,vmin=0, vmax=700)                             
            #plt.show()
           
ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
     print(ser.name + ' is open...')
     
#ReadCal()
ss='run'+'\n'
ll=[ord(c) for c in ss]
ser.write(ll)

rw=animate()
M=next(rw)
past=time()
#Figure =plt.figure()
#CS=Figure.add_subplot(111)

for i in range(6000):
    past=time()
    plt.clf()
    M=next(rw)
    CS=plt.contourf(X, Y, M, 100,origin='upper', cmap=plt.cm.jet,vmin=20, vmax=50)
    #sns.heatmap(M, vmax=50,cmap="plasma",cbar=True,square=True,annot=True)
	# use plt.contour to add contour lines
    #C = plt.contour(X, Y, M, 100, colors='black', linewidth=.01)
    #plt.clabel(C, inline=True, fontsize=1)
    '''plt.imshow(M,origin='lower',vmin=25,vmax=35,cmap=plt.cm.jet)
    for (j,h),label in np.ndenumerate(M):
        plt.text(h,j,float("%.1f" % label),ha='center',va='center',fontsize=8,color='white')'''
    rightnow=time()
    gap=int(rightnow-past)
    #plt.xlim(41, 50)
    #plt.ylim(-0.5,7.5)
    plt.title('NAMI T Sensor')
    plt.xticks(())
    plt.yticks(())
    plt.figure("Nano and Advanced Materials Institue")
    plt.axes().set_aspect('equal')
    plt.colorbar(CS)
    #plt.figure(figsize=(10,10))
    #rcParams['figure.figsize'] = 10, 10
    plt.pause(0.03)




