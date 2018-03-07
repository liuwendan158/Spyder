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
global ser


T0=np.zeros((50,50))
T1=np.zeros((50,50))
T2=np.zeros((50,50))
T3=np.zeros((50,50))
T4=np.zeros((50,50))
T5=np.zeros((50,50))
T6=np.zeros((50,50))
T7=np.zeros((50,50))
a=np.zeros((50,50))
b=np.zeros((50,50))
c=np.zeros((50,50))
empty=[None]*2500

tcal=[None]*10
tvel=[None]*2500

port="COM5"
port1="COM7"
port2="COM8"
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
excelrow2=-1
excelrow3=-1

workbook  = xlsxwriter.Workbook(r"C:\Users\NAMI\Desktop\SensorData"+datetime.now().strftime('%Y%m%d%H%M')+".csv")
worksheet = workbook.add_worksheet()

workbook2 = xlsxwriter.Workbook(r"C:\Users\NAMI\Desktop\TvelData"+datetime.now().strftime('%Y%m%d%H%M')+".csv")
worksheet2 = workbook.add_worksheet()

workbook3 = xlsxwriter.Workbook(r"C:\Users\NAMI\Desktop\CalibrationData"+datetime.now().strftime('%Y%m%d%H%M')+".csv")
worksheet3 = workbook.add_worksheet()

ser = serial.Serial(port, baud, timeout=1)
if ser.isOpen():
     print(ser.name + ' is open...')

ser1 = serial.Serial(port1, baud1, timeout=1)
if ser1.isOpen():
    print(ser1.name + ' is open...')
     
     
ser2 = serial.Serial(port2, baud2, timeout=1)
if ser1.isOpen():
    print(ser2.name + ' is open...')
