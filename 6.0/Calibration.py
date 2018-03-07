# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:29:43 2018

@author: NAMI
"""
import numpy as np
import time
from datetime import datetime
#file = open(r"C:\Users\user\Desktop\CalibrationTemp"+datetime.now().strftime('%Y%m%d%H')+".txt","w") 
from settings import ser,tcal,ser1
from settings import caltimes,startcal_temp,calgap
from Command import sendcommand,initial,stop,run

def AutoCal():
    stop()
    Temp=np.zeros((50,50))
    re1="0"
    re2='0'
    for h in range(caltimes):
        while(re1 != b'!\r'):
            ser1.flushInput()
            ser1.flushOutput()
            T= startcal_temp+h*calgap
            ss="SS0"+str(T)+"\n\r"
            print(ss)
            ll=[ord(c) for c in ss]
            ser1.write(ll)
            re1=ser1.read(2)
            print(re1)
        re1='0'
        
        '''for number in range(3):
            time.sleep(3600)
            print("waiting for temperature to stable")'''

        ss='RR\n\r'
        print(ss)
        ll=[ord(c) for c in ss]
        ser1.write(ll)
        time.sleep(0.5)
        re2=ser1.read(6)
        #re2.substring(0, re2.length() - 2)
        print(re2)
        if(re2!=''):
            tcal[h]=float(re2)
        print(tcal[h])
        #file.write(str(tcal[h])+"5\n")
        re2=0
        
        re3=0
        while (re3!=b'\xff\xff\xff\xc8\x00\x007'):
            re3=0
            ser.flushInput()
            ser.flushOutput()
            sendcommand("save data point "+str(h)+" "+str(tcal[h])+"5\n")
            time.sleep(30)
            re3=ser.read(7)
            print(re3)
        
        initial()
        sendcommand('read data point '+str(h)+'\n')

        for i in range(51):
            header=0
            data1=0
            row=0
            while(header != b'\xff'):
                header = ser.read(1)
            header=0
            data1=ser.read(2)
            if(data1==b'\xff\xff'):
                row=int.from_bytes(ser.read(1),'little')
                if row>49:
                    ss=ser.read(6)
                    print(ss)
                    print(float(ss))
                    ser.read(3)
                    break;
                for j in range(50):
                    data=int.from_bytes(ser.read(2),byteorder='big')
                    if data==0:
                        data2=0.0;
                    else:
                        data2=((3003 / ((0.292969 * data) / 1000 + 1.8)) - 834.66) / 8.7295
                    Temp[row,j]=data2
                ser.read(1)
        print('Calibation for point '+str(h)+' is:')
        print(Temp)
    #file.close
    
    while(re1 != b'!\r'):
            ser1.flushInput()
            ser1.flushOutput()
            T= 25
            ss="SS0"+str(T)+".00"+"\n\r"
            print(ss)
            ll=[ord(c) for c in ss]
            ser1.write(ll)
            re1=ser1.read(2)
            print(re1)
    print(tcal)


