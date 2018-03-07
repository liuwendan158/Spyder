# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:05:08 2017

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:09:38 2017

@author: user
"""

import serial
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pandas import Series,DataFrame
import os
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

tcal=[None]*10

port = "COM4"
port1="COM7"
port2="COM8"
baud2=9800
baud1=57600
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
maxi=0
mini=0

def AutoCal():
    global tcal
    Temp=np.zeros((50,50))
    re1="0"
    re2='0'
    for h in range(1):
        while(re1 != b'!\r'):
            T= 30
            ss="SS0"+str(T)+".00"+"\n\r"
            print(ss)
            ll=[ord(c) for c in ss]
            ser1.write(ll)
            re1=ser1.read(2)
            print(re1)
        
        for number in range(3):
            time.sleep(3600)
            print("waitint for temperature to stable")

        re1='0' 
        ss="save data point "+str(1)+"\n"
        print(ss)
        ll=[ord(c) for c in ss]
        ser.write(ll)
        
        ss='idle'+'\n'
        ll=[ord(c) for c in ss]
        ser.write(ll)
        time.sleep(0.5)
        ser.flushInput()
        ser.flushOutput()
        ser2.flushInput()
        ser2.flushOutput()
        ser1.flushInput()
        ser1.flushOutput()
        print('successful')
        
        ss='read data point '+str(1)+'\n'
        print(ss)
        ll=[ord(c) for c in ss]
        ser.write(ll)
        
        ss='MON2? 1\n\r'
        print(ss)
        ll=[ord(c) for c in ss]
        ser2.write(ll)
        time.sleep(0.5)
        re2=ser2.read(6)
        #re2.substring(0, re2.length() - 2)
        print(re2)
        tcal[h]=float(re2)
        print(tcal[h])
            
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
                        data2=0.0;
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                    Temp[row,j]=data2
        print('Calibation for point '+str(h)+' is:')
        print(Temp)
    print(tcal)
        
    

def ReadCal():
    global T0,T1,T2,T3,T4,T5,T6,T7,a,b,c,maxi,mini,tcal
    
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
                if data==0:
                    data2=0;
                else:
                    data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                T1[row,j]=data2
    print(T1)
    
    
    s='read data point 2'+'\n'
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
                T2[row,j]=data2
    print(T2)
    
    
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
    
    s='read data point 5'+'\n'
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
                T5[row,j]=data2
    print(T5)
    
    s='read data point 6'+'\n'
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
                T6[row,j]=data2
    print(T6)
    
    s='read data point 7'+'\n'
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
                T7[row,j]=data2
    print(T7)
    
      
    y=np.array([tcal[0],tcal[1],tcal[2],tcal[3],tcal[4],tcal[5],tcal[6],tcal[7]])
    print('tcal:',tcal)
    for i in range(50):
        for j in range(50):
            x=np.array([T0[i,j],T1[i,j],T2[i,j],T3[i,j],T4[i,j],T5[i,j],T6[i,j],T7[i,j]])
            if(T0[i,j]>0 and T1[i,j]>0 and T2[i,j]>0 and T3[i,j]>0 and T4[i,j]>0
               and T5[i,j]>0 and T6[i,j]>0 and T7[i,j]>0 and 
               T0[i,j]!=T1[i,j]!=T2[i,j]!=T3[i,j]!=T4[i,j]!=T5[i,j]!=T6[i,j]!=T7[i,j]):
                f = np.polyfit(x,y,2)
                p= np.poly1d(f)
                a[i,j]=p[2]
                b[i,j]=p[1]
                c[i,j]=p[0]
            else:
                a[i,j]=0
                b[i,j]=0
                c[i,j]=0
  
def DoCal(row,j,data2):
    data=a[row,j]*data2*data2+b[row,j]*data2+c[row,j]
    #data=b[row,j]*data2+c[row,j]
    return data
    
    
def animate():
    global maxi,mini
    TemData = np.zeros((50,50))
    while 1:
        for i in range(50):
            header=0
            data1=0
            row=0
            maxi=0
            mini=45
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
                        data3=0
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                        data3=DoCal(row,j,data2)
                        '''if data3>maxi:
                            maxi=data3
                        elif data3<maxi and data3<mini and data3>0:
                            mini=data3'''
                    TemData[row,49-j] = data3
                row=0
                ser.read(1)
                data1=0
                '''
                    if data==0:
                        data2=0
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                    TemData[row,49-j] = data2
                    before=data2
                row=0
                ser.read(1)
                data1=0'''
                #print("Max:", maxi, "Min:",mini)
                #ListData=TemData.tolist()
        yield TemData

            #plt.contourf(x,y,df, 50, cmap=plt.cm.jet,vmin=0, vmax=700)                             
            #plt.show()
           
ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
     print(ser.name + ' is open...')
     
ser1 = serial.Serial(port1, baud1, timeout=1)
if ser1.isOpen():
     print(ser1.name + ' is open...')
     
     
ser2 = serial.Serial(port2, baud2, timeout=1)
if ser1.isOpen():
     print(ser2.name + ' is open...')
     
ss='idle'+'\n'
ll=[ord(c) for c in ss]
ser.write(ll)

time.sleep(0.5)

ser.flushInput()

AutoCal()

ss='idle'+'\n'
ll=[ord(c) for c in ss]
ser.write(ll)

time.sleep(0.5)

ser.flushInput()
     
#ReadCal()
ss='run'+'\n'
ll=[ord(c) for c in ss]
ser.write(ll)

rw=animate()
M=next(rw)
#past=time()
#Figure =plt.figure()
#CS=Figure.add_subplot(111)

for i in range(6):
    #past=time()
    plt.clf()
    M=next(rw)
    CS=plt.contourf(X, Y, M, 100,origin='upper', cmap=plt.cm.jet,vmin=25, vmax=50)
    #sns.heatmap(M, vmax=50,cmap="plasma",cbar=True,square=True,annot=True)
	# use plt.contour to add contour lines
    #C = plt.contour(X, Y, M, 100, colors='black', linewidth=.01)
    #plt.clabel(C, inline=True, fontsize=1)
    '''plt.imshow(M,origin='lower',vmin=25,vmax=35,cmap=plt.cm.jet)
    for (j,h),label in np.ndenumerate(M):
        plt.text(h,j,float("%.1f" % label),ha='center',va='center',fontsize=8,color='white')'''
    #rightnow=time()
    #gap=int(rightnow-past)
    #plt.xlim(41, 50)
    #plt.ylim(-0.5,7.5)
    plt.title('Max: '+str(maxi)+'\n Min:'+str(mini))
    plt.xticks(())
    plt.yticks(())
    plt.figure("Nano and Advanced Materials Institue")
    plt.axes().set_aspect('equal')
    plt.colorbar(CS)
    #plt.figure(figsize=(10,10))
    #rcParams['figure.figsize'] = 10, 10
    plt.pause(0.03)
  
ser.close()
ser1.close()
ser2.close()
exec(open(r"C:\Users\user\Desktop\TemperatureSensorApplication\VerifyProgram.py").read())





