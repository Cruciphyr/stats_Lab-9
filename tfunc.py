# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 11:33:46 2026

@author: Tarin Katasema
"""
import stats
import csv 
import pylab as py
from scipy.stats import ttest_ind as ttest

def load_csv(filename):
    """Read data from a CSV file and return the data list."""
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
            else:
                data.append(int(row[1]))
                line_count += 1
        print(f'Processed {line_count} lines.')
    return data

def plot_hist(data,title,xlabel,ylabel,bins):
    py.figure()
    py.title(title)
    py.xlabel(xlabel)
    py.ylabel(ylabel)
    py.hist(data,bins)
    


prozac = [64,68,84,65,50,60,81,76]
truzac = [53,44,61,50,40,39,58,42]

def sumStats(name,data):
    print()
    print(f"Mean of {name}:",stats.mean(data))
    print(f"N of {name}:",len(data))
    print(f"Std Dev of {name:}",stats.sampleDev(data))

def tTest(name,data_a,data_b):
    results = ttest(data_a,data_b)
    print()
    print(f"T test {name}:",results)
    
sumStats("Prozac Data",prozac)
sumStats("Truzac Data",truzac)

#def tTest()

crabData = load_csv('HorseshoeCrabDataMod.csv')
sumStats("Horse Shoe Crab",crabData)

tTest("t test",prozac,truzac)

