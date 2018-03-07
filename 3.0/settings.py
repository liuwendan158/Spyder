# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:46:35 2018

@author: NAMI
"""
import serial
import numpy as np
import time
import matplotlib.pyplot as plt
#import seaborn as sns
#import pandas as pd
#from pandas import Series,DataFrame
import xlsxwriter
from datetime import datetime
global M,T0,T1,T2,T3,T4,T5,T6,T7,a,b,c,empty,tcal,tvel,port,port1
global port2,baud2,baud1,baud,X,Y,excelrow,excelrow1,excelrow2
global workbook,workbook2,workbook3,worksheet,worksheet2,worksheet3
global ser,caltimes


######################################################################
#setting for the program
caltimes=10
startcal_temp=25

vertimes=10
startver_temp=27
####calgap has to be float!!!!
vergap=2.50
calgap=3.00

##port for MSP430
port="COM10"
##port for temperature control and reading
port1="COM7"
##port for milliK
port2="COM8"

level=np.linspace(20.0,35.0,20)

#######################################################################

a=np.zeros((50,50))
b=np.zeros((50,50))
c=np.zeros((50,50))
empty=[None]*2500

tcal=[None]*10
tvel=[None]*2500


baud2= 9800
baud1= 57600
baud = 1000000
temp = 0b101111
data = 0
header = 0
PressureArray=[]
X=[x for x in range(50)]
Y=[y for y in range(50)]
x,y=np.meshgrid(X, Y)
#fig=plt.figure()
#plt.axes().set_aspect('equal')

row=0
excelrow=-1

workbook  = xlsxwriter.Workbook(r"C:\Users\user\Desktop\SensorData"+datetime.now().strftime('%Y%m%d%H%M')+".csv")
worksheet = workbook.add_worksheet()

workbook1 = xlsxwriter.Workbook(r"C:\Users\user\Desktop\TvelDynamicData"+datetime.now().strftime('%Y%m%d%H%M')+".csv")
worksheet1 = workbook1.add_worksheet()

workbook2 = xlsxwriter.Workbook(r"C:\Users\user\Desktop\TvelData"+datetime.now().strftime('%Y%m%d%H%M')+".csv")
worksheet2 = workbook2.add_worksheet()


ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
     print(ser.name + ' is open...')
'''
ser1 = serial.Serial(port1, baud1, timeout=1)
if ser1.isOpen():
    print(ser1.name + ' is open...')
     
     
ser2 = serial.Serial(port2, baud2, timeout=1)
if ser1.isOpen():
    print(ser2.name + ' is open...')'''
