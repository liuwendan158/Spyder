# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:40:16 2018

@author: NAMI
"""
import time
import SaveFile
import Animation
import numpy as np
import matplotlib.pyplot as plt
from settings import tvel,ser,X,Y,empty,excelrow2,worksheet2
from settings import ser1,ser2

def AutoVel():
    ss='idle'+'\n' 
    ll=[ord(d) for d in ss]
    ser.write(ll)
    time.sleep(0.5)
    ser.flushInput()
    
    for i in range(8):
        re1="0"
        re2='0'
        while(re1 != b'!\r'):
            T= 23+i*5
            ss="SS0"+str(T)+".00"+"\n\r"
            print(ss)
            ll=[ord(c) for c in ss]
            ser1.write(ll)
            re1=ser1.read(2)
            print(re1)
        
        '''for number in range(3):
            time.sleep(3600)
            print("waiting for temperature to stable")'''
        
        ser.flushInput()
        ser.flushOutput()
        ser2.flushInput()
        ser2.flushOutput()
        ser1.flushInput()
        ser1.flushOutput()
        print('successful')
        
        ss='MON2? 1\n\r'
        print(ss)
        ll=[ord(c) for c in ss]
        ser2.write(ll)
        time.sleep(0.5)
        re2=ser2.read(5)
        #re2.substring(0, re2.length() - 2)
        print(re2)
        tvel[i]=float(re2)
        print(tvel[i])
        SaveFile.SaveFile(tvel)
    
        ss='idle'+'\n'
        ll=[ord(c) for c in ss]
        ser.write(ll)
        time.sleep(0.5)
        ser.flushInput()
        ss='run'+'\n'
        ll=[ord(c) for c in ss]
        ser.write(ll)
        
        plt.title('NAMI Temprature Sensor')
        plt.xticks(())
        plt.yticks(())
        plt.figure("Nano and Advanced Materials Institue")
        plt.axes().set_aspect('equal')
        
        rw=Animation.animate()
        for i in range(20):
        #plt.clf()
            M=next(rw)
            CS=plt.contourf(X, Y, M, 100,origin='upper', cmap=plt.cm.jet,vmin=36, vmax=39)
            ListData=np.reshape(M,2500)
            excelrow2=SaveFile.SaveFile(excelrow2,worksheet2,ListData)
            excelrow2=SaveFile.SaveFile(excelrow2,worksheet2,empty)
            excelrow2=SaveFile.SaveFile(excelrow2,worksheet2,tvel)
            plt.colorbar(CS)
            plt.pause(0.03)
    