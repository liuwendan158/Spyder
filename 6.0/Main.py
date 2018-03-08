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
#import Calibration
#import AutoVel
import ReadCal
import SaveFile
import Animation
import DynamicAutomation
#import Calibration
#import AutoVel
#from pylab import rcParams
from settings import ser,X,Y,excelrow,worksheet,workbook,level
#from settings import ser1,ser2
from settings import caltimes


M=np.zeros((100,100))
'''
print("Do you need calibration?Please input y/n")
answer=input()
if (answer=='y'):    
    Calibration.AutoCal()
    ReadCal.ReadCal()
    AutoVel.AutoVel()'''

ReadCal.ReadCal()

print("Do you need Dynamic Automation?Please enter y/n")
answer=input()
if (answer=='n'):
    rw=Animation.animate()
elif (answer=='y'):
    print("Please input the times for dynamiautomation")
    answer=input()
    h=int(answer)
    rw=DynamicAutomation.dynamic(h)

for i in range(6000):
    M=next(rw)
    Animation.plot(X,Y,M,level)
    #CS=plt.contour(X, Y, M,levels=level)
    #plt.clabel(CS, inline=1, fontsize=10)
    #ListData=np.reshape(M,40000)
    #excelrow=SaveFile.SaveFile(excelrow,worksheet,ListData)
    #plt.show()


print('Finished')   
workbook.close()
ser.close()
#ser1.close()
#ser2.close()




