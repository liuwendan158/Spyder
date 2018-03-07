# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:41:50 2018

@author: NAMI
"""

def SaveFile(excelrow,worksheet,list):
    col=0
    excelrow= excelrow+1
    for col in range(2500):
        worksheet.write(excelrow, col, list[col]) 
    return excelrow