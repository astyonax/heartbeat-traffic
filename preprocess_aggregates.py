#! /usr/bin/env python
#! -.- codec?? -.-

import numpy as np
import pandas as pd

print '1/ loading data'
data = pd.read_hdf('aggregates.hdf','aggregates')

print '2/ removing dead traffic counters'
def myapp(group):
    # this function removes dead counting stations
    var = group['AVG(debit)'].var()
    if abs(var)>1e-1:return group
data = data.groupby('id_arc_trafic').apply(myapp)
print '3/ columns for plotting (time and modified debit)'
df = data[(data.lon!=0) & (data.lat!=0)].copy()
df.loc[:,'lndebit']=df['AVG(debit)']**.2
df.loc[:,'time']=df['month']*100+df['hour']
print '4/ coarse grained readings'
DLO = df.lon.max(),df.lon.min()
DLA = df.lat.max(),df.lat.min()
DLOb = np.linspace(DLO[0],DLO[1],25)
DLAb = np.linspace(DLA[0],DLA[1],25)
df.loc[:,'dlo25']=df.lon.apply(lambda x:np.digitize(x,DLOb))
df.loc[:,'dla25']=df.lat.apply(lambda x:np.digitize(x,DLAb))
DLOb = np.linspace(DLO[0],DLO[1],50)
DLAb = np.linspace(DLA[0],DLA[1],50)
df.loc[:,'dlo50']=df.lon.apply(lambda x:np.digitize(x,DLOb))
df.loc[:,'dla50']=df.lat.apply(lambda x:np.digitize(x,DLAb))
DLOb = np.linspace(DLO[0],DLO[1],75)
DLAb = np.linspace(DLA[0],DLA[1],75)
df.loc[:,'dlo75']=df.lon.apply(lambda x:np.digitize(x,DLOb))
df.loc[:,'dla75']=df.lat.apply(lambda x:np.digitize(x,DLAb))
print '5/ saving to traffic_preprocessed.pkl'
df.to_pickle('traffic_preprocessed.pkl')
exit(0)
