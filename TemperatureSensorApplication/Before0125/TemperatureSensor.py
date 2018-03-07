# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:04:08 2017

@author: user
"""

import serial
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import animation

zero = np.zeros((50,50))
df=pd.DataFrame(zero)
port = "COM25"
baud = 500000
temp = 0b101111
data = 0
header = 0

x=[0,1,2,3,4,5,6]
y=[0,1,2,3,4,5,6,7,8,9]
cmd="COM6"
fig=plt.figure()
row=0


def init():
    sns.heatmap(df, vmax=1000,cmap="plasma",cbar=False,square=True)
      
def animate(i):
    if cmd == 'exit':
        ser.close()
        exit()
    else:
        #ser.flushInput()
        #print("Please Enter CMD")
        #cmd=input()
        for i in range(50):
            header=0
            data1=0
            row=0
            while(header != b'\xff'):
                header = ser.read(1)
            data1=ser.read(2)
            if(data1==b'\xff\xff'):
                temp = ser.read(1)
                row=int.from_bytes(temp,byteorder='big')
                if(row>50):
                    break;
                for j in range(50):
                    temp =ser.read(2)
                    data=int.from_bytes(temp,byteorder='big')
                    if data==0:
                        data2=0;
                    else:
                        data2=((330 / (0.244141 * data/ 1000 + 2) * 10 - 100 - 800) / 8.7298)
                    df.set_value(row, j, data2)
        print('Data is : %i %i',row, df)
        sns.heatmap(df, vmin=25,vmax=35,cmap="plasma",cbar=False,square=True)


ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
     print(ser.name + ' is open...')
  
anim = animation.FuncAnimation(fig, animate, init_func=init,frames=112000, repeat = False)
plt.show()

