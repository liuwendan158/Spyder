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
        checkrow=0
        row=1240
        while(row!=0):
            header=0
            data1=0
            while(header != 255):
                header = int.from_bytes(ser.read(1),'little')
            data1=int.from_bytes(ser.read(2),'little')
            if(data1==65535):
                row=int.from_bytes(ser.read(1),'little')
                checkrow=checkrow+1
                if(row==255):
                    print(ser.read(1000));
                    break;
                #print(row,checkrow)
        #print('Done!')
        for i in range(51):
            if row>49 and row!=202:
                break;
            for j in range(50):
                data=int.from_bytes(ser.read(2),byteorder='big')
                if data==0:
                    data2=0;
                else:
                    data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                    data3=ReadCal.DoCal(row,j,data2)
                TemData[row,49-j]=data3
            ser.read(4)
            row=int.from_bytes(ser.read(1),'little')
        #print('Inloop')
        yield TemData
        
