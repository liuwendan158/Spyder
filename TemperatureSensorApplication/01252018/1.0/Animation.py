# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:42:46 2018

@author: NAMI
"""
import numpy as np
import ReadCal
from settings import ser
import time

def animate():
    TemData = np.zeros((50,50))
    ss='idle'+'\n' 
    ll=[ord(d) for d in ss]
    ser.write(ll)
    time.sleep(0.5)
    ser.flushInput()
    ser.flushOutput()
    ss='run'+'\n'
    ll=[ord(d) for d in ss]
    ser.write(ll)
    
    while 1:
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
                        data2=0
                        data3=0
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                        data3=ReadCal.DoCal(row,j,data2)
                    TemData[row,49-j] = data3
                row=0
                data1=0
        yield TemData
        
