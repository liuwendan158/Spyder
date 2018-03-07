# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:42:46 2018

@author: NAMI
"""
import numpy as np
import ReadCal
from settings import ser
import time
from Command import initial,run,sendcommand
import matplotlib.pyplot as plt


def animate():
    connected_board=sendcommand('run\n')
    TemData = np.zeros((100,100))
    
    while 1:
        TemData=realtime(TemData,connected_board)
        yield TemData
        
def realtime(TemData,connection):
    data3=0
    data2=0
    row=255
    while(row!=0):
        row=ReadCal.begin()
    for connect in range(4):
        if (connection[connect]==1):
            for i in range(51):
                for j in range(50):
                    if row>200:
                        break
                    data=int.from_bytes(ser.read(2),byteorder='big')
                    if data==0:
                        data2=0;
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                        data3=ReadCal.DoCal(row,j,data2)
                    TemData[row,j]=data3
                ser.read(1)
                row=ReadCal.begin()
                
    '''for i in range(200):
            header=0
            data1=0
            while(header != b'\xff'):
                header = ser.read(1)
            data1=ser.read(2)
            if(data1==b'\xff\xff'):
                row=int.from_bytes(ser.read(1),'little')
                if row>200:
                    print('wrong row', row)
                    break;
                for j in range(200):
                    data=int.from_bytes(ser.read(2),byteorder='big')
                    if data==0:
                        data2=0;
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                        data3=ReadCal.DoCal(row,j,data2)
                    TemData[row,49-j]=data3
                ser.read(1)'''
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
        
