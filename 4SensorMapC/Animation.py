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
import math


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
                        print('wrong row',row)
                        break
                    data=int.from_bytes(ser.read(2),byteorder='big')
                    if data==0:
                        data2=0;
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                        data3=ReadCal.DoCal(row,j,data2)
                    row1,j1=remap(row,j)
                    #TemData[row,j]=data3
                    TemData[row1,j1]=data3
                ser.read(1)
                row=ReadCal.begin()
    return TemData

def plot(X, Y, M,level):
    plt.figure("Nano and Advanced Materials Institue")
    plt.axes().set_aspect('equal')
    plt.title('NAMI Temprature Sensor')
    plt.xticks(())
    plt.yticks(())
    CX=plt.contourf(X, Y, M,origin='upper', cmap=plt.cm.jet,levels=level)
    plt.colorbar(CX)
    plt.pause(0.1)
    plt.clf()
    
def remap(row,j):
    if(row<50):
        row,j=change(180,row,j)
        row=row+49
        j=-j
    elif(row<100):
        row,j=change(90,row,j)
        row=row+99
        j=-j-1
    '''
    if(row>99 and row<150):
        break
    if(row>149 and row<200):
    '''
    return row,j

def change(deg,row,j):
    m=int(math.sin(math.radians(deg)))
    n=int(math.cos(math.radians(deg)))
    #matrix=np.zeros((2,2))
    matrix=np.array([[n,-m],[m,n]])
    #print(matrix)
    a=np.array([[row],[j]])
    [[row],[j]]=matrix.dot(a)
    #print(row,j)
    return row,j
        
