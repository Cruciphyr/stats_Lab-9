# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:48:28 2019

@author: Kerri-Ann Norton
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 13:38:31 2019

@author: Kerri Norton
Hypothesis Testing (t-tests)
"""
import pylab, random, scipy
from scipy import stats

tStat = -2.13165598142 #t-statistic for PED-X example
tDist = []
numBins = 1000
for i in range(10000000):
  tDist.append(scipy.random.standard_t(190))

pylab.hist(tDist, bins = numBins,
           weights = pylab.array(len(tDist)*[1.0])/len(tDist))
pylab.axvline(tStat, color = 'w') 
pylab.axvline(-tStat, color = 'w')
pylab.title('T-distribution with 190 Degrees of Freedom')
pylab.xlabel('T-statistic')
pylab.ylabel('Probability')

from scipy.stats import ttest_1samp
trueMean = 1.76
samples = [1.752, 1.818, 1.597, 1.697, 1.644,  1.593, 1.878, 1.648, 1.819, 1.794, 1.745,  1.827]
tStat, twoTailProb = ttest_1samp(samples, trueMean)
print('t-statistic: ',tStat)
print('p-value: ', twoTailProb)
# Result is: t-statistic: -0.918, p-value:0.378