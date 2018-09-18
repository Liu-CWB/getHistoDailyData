#This script is written for the person who want to get CWB historical daily data. 
#However, this script is not for web crawler so that you should have the data before you excute this script.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

colname = ['stno', 'yyyymmdd', 'PS01', 'PS02', 'PS03', 'PS04', 'PS05', 'PS06', 'PS07', 'PS08', 'PS09', 'PS10', 'TX01', 'TX02', 'TX03',
           'TX04', 'TX05', 'TX06', 'TD01', 'TD02', 'TD03', 'TD04', 'TX07', 'TX08', 'TX09', 'VP01', 'VP02', 'VP03', 'VP04', 'VP05', 'RH01',
           'RH02', 'RH03', 'RH04',   'RH05', 'WD01', 'WD02', 'WD03', 'WD04', 'WD05', 'WD06', 'WD07', 'WD08', 'WD09', 'PP01', 'PP02', 'PP03',
           'PP04', 'PP05','PP06', 'SS01', 'SS02', 'GR01', 'GR02', 'GR03', 'VS01', 'CD01', 'SD01', 'ST01', 'ST02', 'ST03', 'ST04', 'ST05', 
           'ST06', 'ST07', 'ST08', 'ST09', 'ST10', 'ST11', 'ST12', 'EP01', 'EP02', 'EP03', 'TG01', 'TS01', 'TS02', 'TS03', 'TS04', 'TS05',
           'TS06', 'TS07', 'TS08', 'TS09', 'TS10']
Temprature = pd.DataFrame([])
stnnumber = '466920'
var = 'TX02'
month = '09'
for i in range(2008,2018):
    m = pd.read_table('%s%s_cwb_dy.txt'%(str(i),month),skiprows=106,delim_whitespace=True,names=colname)
    taipeiStn = m.query("stno=='%s'"%stnnumber)
    highTemp = taipeiStn['%s'%var].reset_index(drop=True)
    yymmdd = taipeiStn['yyyymmdd'].reset_index(drop=True)
    new = pd.concat([yymmdd,highTemp],axis=1)
    Temprature = pd.concat([Temprature,new])

Temprature = Temprature.reset_index(drop=True)
Temprature_sort = Temprature.sort_values(by='%s'%var,ascending=False).reset_index(drop=True)
Temprature_final =Temprature_sort[Temprature_sort['%s'%var]>0]
print(Temprature_final)
Tempday = Temprature_final['yyyymmdd']
Tempday = np.asarray(Tempday,dtype=str)

yy = []
for rank in range(78):
    yy.append(Tempday[rank][:4])
yy = np.asarray(yy,dtype=int)
plt.scatter(range(78),yy,color='m',alpha=0.65)
plt.show()
