# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:33:27 2018

@author: NAMI
"""
import numpy as np
from settings import ser,T0,T1,T2,T3,T4,T5,T6,T7,a,b,c
import time

def ReadCal():
    ss='idle'+'\n' 
    ll=[ord(d) for d in ss]
    ser.write(ll)
    time.sleep(0.5)
    ser.flushInput()
    ser.flushOutput()
    
    ss='read data point 0'+'\n'
    ll=[ord(c) for c in ss]
    ser.write(ll)
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
    
      
    y=np.array([24.707, 29.598, 34.504, 39.429, 44.365, 49.33, 54.277, 59.242])
    print('tcal:',[24.707, 29.598, 34.504, 39.429, 44.365, 49.33, 54.277, 59.242])
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

