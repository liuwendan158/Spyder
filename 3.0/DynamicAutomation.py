# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:34:59 2018

@author: NAMI
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:42:46 2018

@author: NAMI
"""
import numpy as np
import ReadCal
from settings import ser
import time

def dynamic(DynamicTimes):
    names=locals()
    Temtotal= np.zeros((50,50))
    ADC=np.zeros((50,50))
    for i in range(DynamicTimes):
        names['TemData%s' % i] = np.zeros((50,50))
        
    ss='idle'+'\n' 
    ll=[ord(d) for d in ss]
    ser.write(ll)
    time.sleep(0.5)
    ser.flushInput()
    ser.flushOutput()
    ss='run'+'\n'
    ll=[ord(d) for d in ss]
    ser.write(ll)
    
    for DynamicTime in range(DynamicTimes):
       row=225
       header=0
       data1=0
       while(row!=0):
            while(header != b'\xff'):
                header = ser.read(1)
            data1=ser.read(2)
            if(data1==b'\xff\xff'):
                row=int.from_bytes(ser.read(1),'little')
       for i in range(51):
            if row>49 and row!= 202:
                break;
            for j in range(50):
                data=int.from_bytes(ser.read(2),byteorder='big')
                if data==0:
                    data2=0;
                else:
                    data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                    data3=ReadCal.DoCal(row,j,data2)
                names['TemData%s' % DynamicTime][row,j] = data3
            ser.read(4)
            row=int.from_bytes(ser.read(1),'little')
    
    while 1:
        Temtotal=np.zeros((50,50))
        for i in range(1,DynamicTimes):
            names['TemData%s' % (i-1)]=names['TemData%s' % (i)]
            Temtotal=Temtotal+names['TemData%s' % (i-1)]
            
        row=225
        header=0
        data1=0
        while(row!=0):
            while(header != b'\xff'):
                header = ser.read(1)
            data1=ser.read(2)
            if(data1==b'\xff\xff'):
                row=int.from_bytes(ser.read(1),'little')
        for i in range(51):
            if row>49 and row!= 202:
                break;
            for j in range(50):
                data=int.from_bytes(ser.read(2),byteorder='big')
                if data==0:
                    data2=0;
                else:
                    data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                    data3=ReadCal.DoCal(row,j,data2)
                names['TemData%s' % (DynamicTimes-1)][row,j]=data3
            ser.read(4)
            row=int.from_bytes(ser.read(1),'little')
        Temtotal=(Temtotal+names['TemData%s' % (DynamicTimes-1)])/DynamicTimes
        yield Temtotal