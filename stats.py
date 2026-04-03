# -*- coding: utf-8 -*-
import math
import pylab
"""
Created on Fri Feb 13 11:42:28 2026
tk8431@bard.edu
@author: Tarin Katasema
"""



def mode(x):
    freq = {}
    
    for num in x:   
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1 
    
    frequency = max(freq, key=freq.get)  
    return frequency

def mean(x):
    n = len(x)
    sumNum = 0
    for num in x:
        sumNum += num
    mean = sumNum/n 
    return round(mean,3)


def median(x):  
   n = len(x)
   
   x.sort()
   
   if n % 2 == 0:
       med1 = x[n//2]
       med2 = x[n//2 - 1]
       median = (med1 + med2)/2
   else:
       median = x[n//2]
       
   return median,2

def variance(x):
   mu = mean(x)
   total = 0
   for i in x:
       total += (i - mu) ** 2 
       
   return total/len(x)
        

    

def stdDev(x):
   s = (SS_Comp(x)/len(x)) ** 0.5
   return round(s, 3)
    
def sampleDev(x):
    n = len(x)-1
    s = (SS_Comp(x)/n) ** 0.5
    return round(s, 3)


def SS_Comp(x):
    n = len(x)

    sum_x = 0
    sum_x_squared = 0

    for value in x:
        sum_x += value
        sum_x_squared += value * value

    SS = sum_x_squared - (sum_x * sum_x) / n

    return SS

def SS_def(x):
    m = mean(x)
    
    sum_squared = 0
    for value in x:
        dev = value - m
        squared_dev = dev * dev
        sum_squared += squared_dev
    return sum_squared


#def pearsonC(x):
    

    
    




