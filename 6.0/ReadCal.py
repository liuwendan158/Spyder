# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:33:27 2018

@author: NAMI
"""
import numpy as np
from settings import ser,caltimes,tcal,a,b,c
import time
from Command import sendcommand,stop


names=locals()
for i in range(caltimes):
    names['T%s' % i] = np.zeros((200,50))

def ReadCal():
    connected_board=[0,0,0,0]
    while(connected_board==[0,0,0,0]):
        connected_board=sendcommand('idle\n')
            
    for times in range(caltimes):
        sendcommand('read data point '+str(times)+'\n')
        names['T%s' % times]=caldata(times,connected_board)
        print(names['T%s' % times])


    #y=np.array([tcal[0],tcal[1],tcal[2],tcal[3]])
    '''
    y=[]
    for connect in range(4):
        for times in range(caltimes):
            y.append(tcal[connect,times])
        print('tcal:',y)'''
    for i in range(200):
        for j in range(50):
            x=[]
            for times in range(caltimes):
                x.append(names['T%s' % times][i,j])
            correction=0
            for times in range(caltimes):
                if(names['T%s' % times][i,j]==0):
                    correction=1
            if(correction==0):
                f = np.polyfit(x,tcal[i//50,:],2)
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

def caldata(times,connection):
    row=225
    while(row!=0):
        row=begin()
    for connect in range(4):
        if (connection[connect]==1):
            for i in range(51):
                if row==201:
                    tcal[connect,times]=readtemp()
                    if(connection[connect+1]==0):
                        break
                else:
                    for j in range(50):
                        data=int.from_bytes(ser.read(2),byteorder='big')
                        if data==0:
                            data2=0;
                        else:
                            data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                        names['T%s' % times][row,j]=data2
                ser.read(1)
                row=begin()
    return names['T%s' % times]

def begin():
    header=0
    data1=0
    ro=0
    while(header != b'\xff'):
        header = ser.read(1)
    data1=ser.read(2)
    if(data1==b'\xff\xff'):
        ro=int.from_bytes(ser.read(1),'little')
    return ro

def readtemp():
    ss=ser.read(6)
    temp=float(ss)
    ser.read(2)
    
    return temp

    
    
    

