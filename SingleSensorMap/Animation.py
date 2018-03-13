# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:42:46 2018

@author: NAMI
"""
import numpy as np
from settings import ser
import time

def inital():
    ss='idle'+'\n' 
    ll=[ord(d) for d in ss]
    ser.write(ll)
    time.sleep(0.5)
    ser.flushInput()
    ser.flushOutput()
    ss='run'+'\n'
    ll=[ord(d) for d in ss]
    ser.write(ll)
    
def animate():
    inital()
    TemData = np.zeros((50,50))
    
    while 1:
        TemData=realtime(TemData)
        yield TemData
        
def realtime(TemData):
    #data3=0
    data2=0
    for i in range(51):
            header=0
            data1=0
            while(header != b'\xff'):
                header = ser.read(1)
            data1=ser.read(2)
            if(data1==b'\xff\xff'):
                row=int.from_bytes(ser.read(1),'little')
                if row>49:
                    #print('wrong row', row)
                    break;
                for j in range(50):
                    data=int.from_bytes(ser.read(2),byteorder='big')
                    if data==0:
                        data2=0;
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                        #data3=ReadCal.DoCal(row,j,data2)
                    TemData[row,49-j]=data2
                ser.read(1)
    return TemData
        
