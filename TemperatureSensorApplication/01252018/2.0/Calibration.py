# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:29:43 2018

@author: NAMI
"""
import numpy as np
import time
from datetime import datetime
file = open(r"C:\Users\NAMI\Desktop\CalibrationTemp"+datetime.now().strftime('%Y%m%d%H')+".txt","w") 
from settings import ser,tcal

def AutoCal(h):
    ss='idle'+'\n' 
    ll=[ord(d) for d in ss]
    ser.write(ll)
    time.sleep(0.5)
    ser.flushInput()
    ser.flushOutput()
    
    Temp=np.zeros((50,50))
    re1="0"
    re2='0'
    for h in range(h):
        while(re1 != b'!\r'):
            T= 25+h*5
            ss="SS0"+str(T)+".00"+"\n\r"
            print(ss)
            ll=[ord(c) for c in ss]
            ser1.write(ll)
            re1=ser1.read(2)
            print(re1)
        
        for number in range(3):
            time.sleep(3600)
            print("waiting for temperature to stable")

        re1='0' 
        ss="save data point "+str(h)+"\n"
        print(ss)
        ll=[ord(c) for c in ss]
        ser.write(ll)
        time.sleep(30)
        
        ss='idle'+'\n'
        ll=[ord(c) for c in ss]
        ser.write(ll)
        time.sleep(0.5)
        ser.flushInput()
        ser.flushOutput()
        ser2.flushInput()
        ser2.flushOutput()
        ser1.flushInput()
        ser1.flushOutput()
        print('successful')
        
        ss='read data point '+str(h)+'\n'
        print(ss)
        ll=[ord(c) for c in ss]
        ser.write(ll)
        
        ss='MON2? 1\n\r'
        print(ss)
        ll=[ord(c) for c in ss]
        ser2.write(ll)
        time.sleep(0.5)
        re2=ser2.read(6)
        file.write(re2+"\n")
        #re2.substring(0, re2.length() - 2)
        print(re2)
        if(re2!=''):
            tcal[h]=float(re2)
        print(tcal[h])
            
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
                    if data==0:
                        data2=0.0;
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                    Temp[row,j]=data2
        print('Calibation for point '+str(h)+' is:')
        print(Temp)
    file.close
    print(tcal)


