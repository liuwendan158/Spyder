# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:41:50 2018

@author: NAMI
"""

def SaveFile(excel,worksheet,list):
    col=0
    excel= excel+1
    for col in range(2500):
        worksheet.write(excel, col, list[col]) 
    return excel