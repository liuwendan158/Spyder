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
from settings import ser
import time
from Animation import realtime
from Command import initial

def dynamic(DynamicTimes):
    names=locals()
    Temtotal= np.zeros((200,200))
    ADC=np.zeros((200,200))
    for i in range(DynamicTimes):
        names['TemData%s' % i] = np.zeros((200,200))
        
    initial()
    
    for DynamicTime in range(DynamicTimes):
       names['TemData%s' % DynamicTime]=realtime(names['TemData%s' % DynamicTime])
    
    while 1:
        Temtotal=np.zeros((200,200))
        for i in range(1,DynamicTimes):
            names['TemData%s' % (i-1)]=names['TemData%s' % (i)]
            Temtotal=Temtotal+names['TemData%s' % (i-1)]
        
        names['TemData%s' % (DynamicTimes-1)]=realtime(names['TemData%s' % (DynamicTimes-1)])
        Temtotal=(Temtotal+names['TemData%s' % (DynamicTimes-1)])/DynamicTimes
        yield Temtotal