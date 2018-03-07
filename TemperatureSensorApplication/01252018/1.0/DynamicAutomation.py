# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:34:59 2018

@author: NAMI
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:42:46 2018

@author: NAMI
"""
import numpy as np
import ReadCal
from settings import ser
import time

def dynamic(DynamicTimes):
    names=locals()
    Temtotal= np.zeros((50,50))
    ADC=np.zeros((50,50))
    for i in range(DynamicTimes):
        names['TemData%s' % i] = np.zeros((50,50))
        
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
        for DynamicTime in range(DynamicTimes):
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
                        names['TemData%s' % DynamicTime][row,49-j] = data3
                        ADC[row,49-j]= data2
                    #ListData=np.reshape(ADC,2500)
                    row=0
                    data1=0
            print(DynamicTime)
        for i in range(DynamicTimes):
            Temtotal=Temtotal+names['TemData%s' % i]
        Temtotal=Temtotal/DynamicTimes
        yield Temtotal