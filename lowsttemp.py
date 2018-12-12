import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Temprature = pd.DataFrame([])
stnnumber = '466920'
var = 'TX04'
month ='01'
for i in range(1961,2018):
    m = pd.read_table('%s%s_cwb_dy.txt'%(str(i),month),skiprows=106,delim_whitespace=True,names=colname)
    taipeiStn = m.query("stno=='%s'"%stnnumber)
    lowstTemp = taipeiStn['%s'%var].reset_index(drop=True)
    yymmdd = taipeiStn['yyyymmdd'].reset_index(drop=True)
    new = pd.concat([yymmdd,lowstTemp],axis=1)
    Temprature = pd.concat([Temprature,new])

Temprature = Temprature.reset_index(drop= True)
collect = pd.DataFrame([])
for ii in range(len(Temprature['yyyymmdd'])):
    if Temprature['%s'%var][ii] < 10 and Temprature['%s'%var][ii] > 0:
        collect = pd.concat([collect,Temprature[ii:ii+1]])
collect = collect.reset_index(drop = True)
collnp = np.asarray(collect['yyyymmdd'],dtype=str)
size = 80
plt.figure(figsize=(16,8))
for j in range(len(collnp)):
    if collect['%s'%var][j] > 9:
        plt.scatter(int(collnp[j][:4]),int(collnp[j][6:]),color = 'navy',s=size)
    elif collect['%s'%var][j] > 8 and collect['TX04'][j] <= 9:
        plt.scatter(int(collnp[j][:4]),int(collnp[j][6:]),color = 'blue',s=size)
    elif collect['%s'%var][j] > 7 and collect['TX04'][j] <= 8:
        plt.scatter(int(collnp[j][:4]),int(collnp[j][6:]),color = 'blue',alpha=0.5,s=size)
    elif collect['%s'%var][j] > 6 and collect['TX04'][j] <= 7:
        plt.scatter(int(collnp[j][:4]),int(collnp[j][6:]),color = 'lightblue',s=size)
    elif collect['%s'%var][j] > 5 and collect['TX04'][j] <= 6:
        plt.scatter(int(collnp[j][:4]),int(collnp[j][6:]),color = 'lightblue',marker='*',s=size)
    else:
        plt.scatter(int(collnp[j][:4]),int(collnp[j][6:]),color = 'red',s=size)
#19761128print(Temprature)
plt.show()
