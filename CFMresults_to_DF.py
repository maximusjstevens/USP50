import numpy as np
import pandas as pd
import scipy as sp
from datetime import datetime,timedelta

def decyeartodatetime(din):
    start = din
    year = int(start)
    rem = start - year
    base = datetime(year, 1, 1)
    result = base + timedelta(seconds=(base.replace(year=base.year + 1) - base).total_seconds() * rem)
    if result.hour<12:
        result2 = result.replace(hour=0, minute=0, second=0, microsecond=0)
    else:
        result = result + timedelta(days=1)
        result2 = result.replace(hour=0, minute=0, second=0, microsecond=0)
    return result2

# firnmass = np.diff(d[site][datasource][name][fil]['depth_trun'][-1,:])*d[site][datasource][name][fil]['density'][-1,:-1]
d2h={}
d2 = {}
dps = [5,10,15,20,25,30,40,80,106]
cra_df = pd.DataFrame(index=dps)
str_df = pd.DataFrame(index=dps)
cra_df_alt = pd.DataFrame(index=dps)
for kk, fil in enumerate(fils):
    print(fil)
    d2h[fil]={}
    d2[fil]={}
    i_t = np.where(d[site][datasource][thenames[0]][fil]['time']>=2017.0328)[0]
#     i_t = np.where(d[site][datasource][thenames[0]][fil]['time_trun']>=2017.0328)[0]
#     i_t = i_t[1:]
    tsteps = d[site][datasource][thenames[0]][fil]['time'][i_t]
    tsteps_datetime = [decyeartodatetime(rr) for rr in tsteps]
#     tsteps = d[site][datasource][thenames[0]][fil]['time_trun'][i_t]
    i_tstart = i_t[0]
    for ii,name in enumerate(thenames):
        print(name)
#         firnmass = np.diff(d[site][datasource][name][fil]['depth_trun'][i_tstart,:])*d[site][datasource][name][fil]['density'][i_tstart,:-1]
        
        i0 = np.where(d[site][datasource][name][fil]['depth'][i_tstart,:]>0.2)[0][0]
        dc0 = d[site][datasource][name][fil]['dcon'][i_tstart,i0]

        i5 = np.where(d[site][datasource][name][fil]['depth'][i_tstart,:]>4.4)[0][0]
        dc5 = d[site][datasource][name][fil]['dcon'][i_tstart,i5]

        i10 = np.where(d[site][datasource][name][fil]['depth'][i_tstart,:]>9.7)[0][0]
        dc10 = d[site][datasource][name][fil]['dcon'][i_tstart,i10]

        i15 = np.where(d[site][datasource][name][fil]['depth'][i_tstart,:]>14.9)[0][0]
        dc15 = d[site][datasource][name][fil]['dcon'][i_tstart,i15]

        i20 = np.where(d[site][datasource][name][fil]['depth'][i_tstart,:]>19.5)[0][0]
        dc20 = d[site][datasource][name][fil]['dcon'][i_tstart,i20]

        i25 = np.where(d[site][datasource][name][fil]['depth'][i_tstart,:]>24.8)[0][0]
        dc25 = d[site][datasource][name][fil]['dcon'][i_tstart,i25]

        i30 = np.where(d[site][datasource][name][fil]['depth'][i_tstart,:]>29.8)[0][0]
        dc30 = d[site][datasource][name][fil]['dcon'][i_tstart,i30]

        i40 = np.where(d[site][datasource][name][fil]['depth'][i_tstart,:]>40.16)[0][0]
        dc40 = d[site][datasource][name][fil]['dcon'][i_tstart,i40]

        i80 = np.where(d[site][datasource][name][fil]['depth'][i_tstart,:]>80.0)[0][0]
        dc80 = d[site][datasource][name][fil]['dcon'][i_tstart,i80]

        i106 = np.where(d[site][datasource][name][fil]['depth'][i_tstart,:]>106.0)[0][0]
        dc106 = d[site][datasource][name][fil]['dcon'][i_tstart,i106]

        dtt_mean = np.mean(np.diff(d[site][datasource][name][fil]['time']))
        dtt = np.diff(d[site][datasource][name][fil]['time'])
#         dtt_all = np.append(dtt_mean,dtt)
        dtt_all = dtt_mean*np.ones(len(dtt)+1)
#         dtt = np.mean(np.diff(d[site][datasource][name][fil]['time_trun']))

        d2h[fil][name]={}
        d2h[fil][name]['crate5']=np.zeros(len(i_t))
        d2h[fil][name]['crate10']=np.zeros(len(i_t))
        d2h[fil][name]['crate15']=np.zeros(len(i_t))
        d2h[fil][name]['crate20']=np.zeros(len(i_t))
        d2h[fil][name]['crate25']=np.zeros(len(i_t))
        d2h[fil][name]['crate30']=np.zeros(len(i_t))
        d2h[fil][name]['crate40']=np.zeros(len(i_t))
        d2h[fil][name]['crate80']=np.zeros(len(i_t))
        d2h[fil][name]['crate106']=np.zeros(len(i_t))

        d2h[fil][name]['len5']=np.zeros(len(i_t))
        d2h[fil][name]['len10']=np.zeros(len(i_t))
        d2h[fil][name]['len15']=np.zeros(len(i_t))
        d2h[fil][name]['len20']=np.zeros(len(i_t))
        d2h[fil][name]['len25']=np.zeros(len(i_t))
        d2h[fil][name]['len30']=np.zeros(len(i_t))
        d2h[fil][name]['len40']=np.zeros(len(i_t))
        d2h[fil][name]['len80']=np.zeros(len(i_t))
        d2h[fil][name]['len106']=np.zeros(len(i_t))

        d2h[fil][name]['dlen5']=np.zeros(len(i_t))
        d2h[fil][name]['dlen10']=np.zeros(len(i_t))
        d2h[fil][name]['dlen15']=np.zeros(len(i_t))
        d2h[fil][name]['dlen20']=np.zeros(len(i_t))
        d2h[fil][name]['dlen25']=np.zeros(len(i_t))
        d2h[fil][name]['dlen30']=np.zeros(len(i_t))
        d2h[fil][name]['dlen40']=np.zeros(len(i_t))
        d2h[fil][name]['dlen80']=np.zeros(len(i_t))
        d2h[fil][name]['dlen106']=np.zeros(len(i_t))
#         print(len(tsteps))
#         print(len(dtt_all))
        for jj,tt in enumerate(tsteps):
            tstep = np.where(d[site][datasource][name][fil]['time']==tt)[0][0]
            
            i0   = (np.abs(d[site][datasource][name][fil]['dcon'][i_tstart+jj,:] - dc0)).argmin()
            i5   = (np.abs(d[site][datasource][name][fil]['dcon'][i_tstart+jj,:] - dc5)).argmin()
            i10  = (np.abs(d[site][datasource][name][fil]['dcon'][i_tstart+jj,:] - dc10)).argmin()
            i15  = (np.abs(d[site][datasource][name][fil]['dcon'][i_tstart+jj,:] - dc15)).argmin()
            i20  = (np.abs(d[site][datasource][name][fil]['dcon'][i_tstart+jj,:] - dc20)).argmin()
            i25  = (np.abs(d[site][datasource][name][fil]['dcon'][i_tstart+jj,:] - dc25)).argmin()
            i30  = (np.abs(d[site][datasource][name][fil]['dcon'][i_tstart+jj,:] - dc30)).argmin()
            i40  = (np.abs(d[site][datasource][name][fil]['dcon'][i_tstart+jj,:] - dc40)).argmin()
            i80  = (np.abs(d[site][datasource][name][fil]['dcon'][i_tstart+jj,:] - dc80)).argmin()
            i106 = (np.abs(d[site][datasource][name][fil]['dcon'][i_tstart+jj,:] - dc106)).argmin()

#             d2h[fil][name]['crate5'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i5])/dtt
#             d2h[fil][name]['crate10'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i10])/dtt
#             d2h[fil][name]['crate15'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i15])/dtt
#             d2h[fil][name]['crate20'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i20])/dtt
#             d2h[fil][name]['crate25'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i25])/dtt
#             d2h[fil][name]['crate30'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i30])/dtt
#             d2h[fil][name]['crate40'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i40])/dtt
#             d2h[fil][name]['crate80'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i80])/dtt
#             d2h[fil][name]['crate106'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i106])/dtt
            
            d2h[fil][name]['crate5'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i5])/dtt_all[tstep]
            d2h[fil][name]['crate10'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i10])/dtt_all[tstep]
            d2h[fil][name]['crate15'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i15])/dtt_all[tstep]
            d2h[fil][name]['crate20'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i20])/dtt_all[tstep]
            d2h[fil][name]['crate25'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i25])/dtt_all[tstep]
            d2h[fil][name]['crate30'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i30])/dtt_all[tstep]
            d2h[fil][name]['crate40'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i40])/dtt_all[tstep]
            d2h[fil][name]['crate80'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i80])/dtt_all[tstep]
            d2h[fil][name]['crate106'][jj]=np.sum(d[site][datasource][name][fil]['compaction_rate'][tstep,i0:i106])/dtt_all[tstep]

            d2h[fil][name]['len5'][jj]=d[site][datasource][name][fil]['depth'][tstep,i5]-d[site][datasource][name][fil]['depth'][tstep,i0]
            d2h[fil][name]['len10'][jj]=d[site][datasource][name][fil]['depth'][tstep,i10]-d[site][datasource][name][fil]['depth'][tstep,i0]
            d2h[fil][name]['len15'][jj]=d[site][datasource][name][fil]['depth'][tstep,i15]-d[site][datasource][name][fil]['depth'][tstep,i0]
            d2h[fil][name]['len20'][jj]=d[site][datasource][name][fil]['depth'][tstep,i20]-d[site][datasource][name][fil]['depth'][tstep,i0]
            d2h[fil][name]['len25'][jj]=d[site][datasource][name][fil]['depth'][tstep,i25]-d[site][datasource][name][fil]['depth'][tstep,i0]
            d2h[fil][name]['len30'][jj]=d[site][datasource][name][fil]['depth'][tstep,i30]-d[site][datasource][name][fil]['depth'][tstep,i0]
            d2h[fil][name]['len40'][jj]=d[site][datasource][name][fil]['depth'][tstep,i40]-d[site][datasource][name][fil]['depth'][tstep,i0]
            d2h[fil][name]['len80'][jj]=d[site][datasource][name][fil]['depth'][tstep,i80]-d[site][datasource][name][fil]['depth'][tstep,i0]
            d2h[fil][name]['len106'][jj]=d[site][datasource][name][fil]['depth'][tstep,i106]-d[site][datasource][name][fil]['depth'][tstep,i0]


        d2h[fil][name]['dlen5']=d2h[fil][name]['len5'][0]-d2h[fil][name]['len5']
        d2h[fil][name]['dlen10']=d2h[fil][name]['len10'][0]-d2h[fil][name]['len10']
        d2h[fil][name]['dlen15']=d2h[fil][name]['len15'][0]-d2h[fil][name]['len15']
        d2h[fil][name]['dlen20']=d2h[fil][name]['len20'][0]-d2h[fil][name]['len20']
        d2h[fil][name]['dlen25']=d2h[fil][name]['len25'][0]-d2h[fil][name]['len25']
        d2h[fil][name]['dlen30']=d2h[fil][name]['len30'][0]-d2h[fil][name]['len30']
        d2h[fil][name]['dlen40']=d2h[fil][name]['len40'][0]-d2h[fil][name]['len40']
        d2h[fil][name]['dlen80']=d2h[fil][name]['len80'][0]-d2h[fil][name]['len80']
        d2h[fil][name]['dlen106']=d2h[fil][name]['len106'][0]-d2h[fil][name]['len106']

        tinter = tsteps[-1]-tsteps[0]
        chold = []
        shold = []
        chold_alt = []
        for kk in dps:
            d2h[fil][name]['cry%s' %kk] = d2h[fil][name]['dlen%s' %kk][-1]/tinter #this is the mean rate over the entirety of the model run
            chold.append(d2h[fil][name]['cry%s' %kk])
            shold.append(d2h[fil][name]['cry%s' %kk]/d2h[fil][name]['len%s' %kk][0])
            chold_alt.append((d2h[fil][name]['len%s' %kk][0]-d2h[fil][name]['len%s' %kk][-1])/(tsteps[-1]-tsteps[0]))
        cra_df[name]=chold
        str_df[name]=shold
        cra_df_alt[name]=chold_alt

        d2[fil][name]=pd.DataFrame(d2h[fil][name],index=tsteps_datetime)
#         cra_df[name+'_'+fil]=chold
#         str_df[name+'_'+fil]=shold
#         cra_df_alt[name+'_'+fil]=chold_alt
#         tc_df[name+'_'+fil]

cra_df_alt['data']=crate_y_order #use 
cra_df['data']=np.array(total_compaction_y_order)/tdely
str_df['data']=strain_y_order
# tc_df['data']=total_compaction_y_order