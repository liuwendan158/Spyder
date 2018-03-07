# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:40:16 2018

@author: NAMI
"""
import time
import SaveFile
import Animation
import DynamicAutomation
import numpy as np
import matplotlib.pyplot as plt
from settings import tvel,ser,X,Y,empty,worksheet2
from settings import ser1,worksheet1,workbook1,workbook2
from settings import vertimes
from settings import startver_temp,vergap
from Command import sendcommand,initial,stop,run


def AutoVel():
    M=np.zeros((50,50))
    N=np.zeros((50,50))
    excelrow1=-1
    excelrow2=-1
    stop()
    
    for i in range(vertimes):
        re1="0"
        re2='0'
        while(re1 != b'!\r'):
            ser1.flushInput()
            ser1.flushOutput()
            T= startver_temp+vergap*i
            ss="SS0"+str(T)+"\n\r"
            print(ss)
            ll=[ord(c) for c in ss]
            ser1.write(ll)
            re1=ser1.read(2)
            print(re1)
        
        '''for number in range(3):
            time.sleep(3600)
            print("waiting for temperature to stable")'''
        
        initial()
        print('successful')
        
        ss='RR\n\r'
        print(ss)
        ll=[ord(c) for c in ss]
        ser1.write(ll)
        time.sleep(0.5)
        re2=ser1.read(6)
        #re2.substring(0, re2.length() - 2)
        print(re2)
        tvel[i]=float(re2)
        print(tvel[i])
    
        run()
        
        plt.title('NAMI Temprature Sensor')
        plt.xticks(())
        plt.yticks(())
        plt.figure("Nano and Advanced Materials Institue")
        plt.axes().set_aspect('equal')
        
        rw=Animation.animate()
        rh=DynamicAutomation.dynamic(4)
        
        excelrow2=SaveFile.SaveFile(excelrow2,worksheet2,tvel)
        
        for i in range(20):
            M=np.zeros((50,50))
        #plt.clf()
            plt.clf()
            M=next(rw)
            CS=plt.contourf(X, Y, M, 100,origin='upper', cmap=plt.cm.jet)
            ListData=np.reshape(M,2500)
            '''excelrow2=SaveFile.SaveFile(excelrow2,worksheet2,ListData)
            M[0:5,:]=0
            M[45:50,:]=0
            M[:,0:5]=0
            M[:,45:50]=0
            ListData=np.reshape(M,2500)'''
            excelrow2=SaveFile.SaveFile(excelrow2,worksheet2,ListData)
            #excelrow2=SaveFile.SaveFile(excelrow2,worksheet2,empty)
            plt.colorbar(CS)
            plt.pause(0.3)
            
        ser.flushInput()
        ser.flushOutput()
        ser1.flushInput()
        ser1.flushOutput()
        print('successful')
        
        ss='RR\n\r'
        print(ss)
        ll=[ord(c) for c in ss]
        ser1.write(ll)
        time.sleep(0.5)
        re2=ser1.read(6)
        #re2.substring(0, re2.length() - 2)
        print(re2)
        tvel[i]=float(re2)
        print(tvel[i])
    
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
        excelrow1=SaveFile.SaveFile(excelrow1,worksheet1,tvel)
        for i in range(20):
            plt.clf()
            N=np.zeros((50,50))
            N=next(rh)
            #CS=plt.contourf(X, Y, N, 100,origin='upper', cmap=plt.cm.jet)
            ListData=np.reshape(N,2500)
            excelrow1=SaveFile.SaveFile(excelrow1,worksheet1,ListData)
            N[0:5,:]=0
            N[45:50,:]=0
            N[:,0:5]=0
            N[:,45:50]=0
            ListData=np.reshape(N,2500)
            CS=plt.contourf(X, Y, N, 100,origin='upper', cmap=plt.cm.jet)
            excelrow1=SaveFile.SaveFile(excelrow1,worksheet1,ListData)
            #excelrow1=SaveFile.SaveFile(excelrow1,worksheet1,empty)
            plt.colorbar(CS)
            plt.pause(0.3)
            
    workbook1.close()
    workbook2.close()
    re1=0
    while(re1 != b'!\r'):
        ser1.flushInput()
        ser1.flushOutput()
        T= 25.00
        ss="SS0"+str(T)+"\n\r"
        print(ss)
        ll=[ord(c) for c in ss]
        ser1.write(ll)
        re1=ser1.read(2)            
        print(re1)
    