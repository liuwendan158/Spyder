# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:42:46 2018

@author: NAMI
"""
import numpy as np
import ReadCal
from settings import ser,connected_board
import time
from Command import initial,run
import matplotlib.pyplot as plt


def animate():
    connected_board=run()
    TemData = np.zeros((50,50))
    
    while 1:
        TemData=realtime(TemData)
        yield TemData
        
def realtime(TemData):
    data3=0
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
                    print('wrong row', row)
                    break;
                for j in range(50):
                    data=int.from_bytes(ser.read(2),byteorder='big')
                    if data==0:
                        data2=0;
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                        data3=ReadCal.DoCal(row,j,data2)
                    TemData[row,49-j]=data3
                ser.read(1)
    return TemData

def plot(X, Y, M,level):
    plt.clf()
    plt.axes().set_aspect('equal')
    plt.title('NAMI Temprature Sensor')
    plt.xticks(())
    plt.yticks(())
    plt.figure("Nano and Advanced Materials Institue")
    CX=plt.contourf(X, Y, M,origin='upper', cmap=plt.cm.jet,levels=level)
    plt.colorbar(CX)
    plt.pause(0.03)
        
