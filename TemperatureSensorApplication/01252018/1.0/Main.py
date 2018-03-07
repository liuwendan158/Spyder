# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 10:27:07 2018

@author: NAMI
"""
# -*- coding: utf-8 -*-

import serial
import numpy as np
import time
import matplotlib.pyplot as plt
#import seaborn as sns
#import pandas as pd
#from pandas import Series,DataFrame

from datetime import datetime
import Calibration
import AutoVel
import ReadCal
import SaveFile
import Animation
import DynamicAutomation
#from pylab import rcParams
from settings import ser,X,Y,excelrow,worksheet,workbook
from settings import workbook2,workbook3,ser1,ser2


M=np.zeros((50,50))
print("Do you need calibration?Please input y/n")
answer=input()
if (answer=='y'):    
    Calibration.AutoCal(8)
    
ReadCal.ReadCal()
    
print("Do you need Accuracy Test? Please input y/n")
answer=input()
if (answer=='y'):   
    AutoVel.AutoVel()
 

print("Do you need Dynamic Automation?Please enter y/n")
answer=input()
if (answer=='n'):
    rw=Animation.animate()
elif (answer=='y'):
    print("Please input the times for dynamiautomation")
    answer=input()
    h=int(answer)
    rw=DynamicAutomation.dynamic(h)

plt.title('NAMI Temprature Sensor')
plt.xticks(())
plt.yticks(())
plt.figure("Nano and Advanced Materials Institue")
plt.axes().set_aspect('equal')

for i in range(100):
    plt.clf()
    M=next(rw)
    CS=plt.contourf(X, Y, M, 100,origin='upper', cmap=plt.cm.jet)
    ListData=np.reshape(M,2500)
    excelrow=SaveFile.SaveFile(excelrow,worksheet,ListData)
    plt.colorbar(CS)
    plt.pause(0.03)


print('Finished')   
workbook.close()
workbook2.close()
workbook3.close()
ser.close()
ser1.close()
ser2.close()




