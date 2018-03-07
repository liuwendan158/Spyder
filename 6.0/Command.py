# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 11:09:53 2018

@author: user
"""

from settings import ser
import time

connected_board=[0,0,0,0]

def run():
    ss='idle'+'\n' 
    ll=[ord(d) for d in ss]
    ser.write(ll)
    time.sleep(0.5)
    ser.flushInput()
    ser.flushOutput()
    sendcommand('run\n')

def stop():
    sendcommand('stop\n')
    ser.flushInput()
    ser.flushOutput()
    
    
def initial():
    ser.flushInput()
    ser.flushOutput()
    

def sendcommand(ss):
    initial() 
    ll=[ord(d) for d in ss]
    ser.write(ll)
    time.sleep(0.5)
    re=ser.read(5)
    if(re==b'\xff\xff\xff\xca\x00'):
        re1=int.from_bytes(ser.read(1),'little')
        i=0
        while(re1//2 !=0 ):
            connected_board[i]=re1%2
            re1=re1//2
            i=i+1
        connected_board[i]=re1
    print(connected_board)
    ser.read(1)
    return connected_board
 
    
    