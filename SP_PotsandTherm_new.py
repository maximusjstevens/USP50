#!/usr/bin/env python

'''
SP_PotsandTherm_new.py

This script loads firn compaction and temperature data recorded 50 km
upstream of South Pole (USP50).

Raw data are loaded and converted into usable quantities: compaction was measured
using string potentiometers, which measure a voltage drop across the potentiometer.
This script converts those measurements to a length change (i.e. a measure of
how much string is pulled out of the potentiometer.)

Temperature data was measured using a 40m thermistor string; the raw data are 
converted to temperatures in this script. The (processed) temperature data
are posted at https://doi.org/10.15784/601525.

'''

import numpy as np
import pandas as pd
import scipy.signal as sps
from warnings import simplefilter
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)

SPY = 365.25*24*3600
pathtodata = '/Users/maxstev/Documents/Grad_School/Research/SouthPole/DATA'
days_to_ignore = 30 # The potentiometers take time to settle (FirnCover reference, so discard the first month of observations)

def smooth(x,window_len=11,window='hanning'):
    """
    Taken from the scipy cookbook: 
    https://scipy-cookbook.readthedocs.io/items/SignalSmooth.html
    
    smooth the data using a window with requested size.
    
    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal 
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.
    
    input:
        x: the input signal 
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal
        
    (full documentation at link above) 
    """
    if x.ndim != 1:
        raise ValueError("smooth only accepts 1 dimension arrays.")
    if x.size < window_len:
        raise ValueError("Input vector needs to be bigger than window size.")
    if window_len<3:
        return x
    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError("Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")

    s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
    if window == 'flat': #moving average
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')

    return y[int(window_len/2-1):-int(window_len/2)]

def butter_lowpass_filter(dd, cutoff, fs, order=6):
    # https://stackoverflow.com/questions/25191620/creating-lowpass-filter-in-scipy-understanding-methods-and-units
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = sps.butter(order, normal_cutoff, btype='low', analog=False)
    y = sps.filtfilt(b, a, dd)
    return y

'''
The resistor for the thermistors are either 200K or 10K ohm.
The CTE for vectran over this temperature range is -5.7_8e-6 m/(m C). Over the top 10 m, if there is a 10 degree change, that is still just a 1/2 millimeter change. 
'''

### Load data from the data loggers
pot_data_all = pd.read_csv(f'{pathtodata}/2018/CR1000_Potdata.dat',header=0,skiprows=[0,2,3],delimiter=',',na_values='NAN')
pot_data_all.columns=['TIMESTAMP','RECORD','Pots1','Pots2','Pots3','Pots4','Pots5','Pots6','Pots7','Pots8','Pots9','Pots10','Pots11','Pots12','Therms1','Therms2','Therms3','Therms4','Therms5','Therms6','Therms7','Therms8','Therms9','Therms10','Therms11','Therms12','LoggerT','BattV_Min','PTemp_C']

### Load data from the temperature string
tstring_data_all = pd.read_csv(f'{pathtodata}/2018/CR1000_ThermData.dat',header=0,skiprows=[0,2,3],delimiter=',')
tstring_data_all.columns = ['TIMESTAMP','RECORD','batt_volt','PTemp','Therm_Res1','Therm_Res2','Therm_Res3','Therm_Res4','Therm_Res5','Therm_Res6','Therm_Res7','Therm_Res8','Therm_Res9','Therm_Res10','Therm_Res11','Therm_Res12','Therm_Res13','Therm_Res14','Therm_Res15','Therm_Res16','Therm_Res17','Therm_Res18','Therm_Res19','Therm_Res20','Therm_Res21','Therm_Res22','Therm_Res23','T10_9_C1','T10_9_C2']

### lookup table for thermistors in pot boxes
therm_table = np.genfromtxt(f'{pathtodata}/ThermistorTable_extrapolated.csv',delimiter=',',skip_header=2) 
therm_temp = np.flipud(therm_table[:,0])
therm_res = np.flipud(therm_table[:,1])

pot_data_all['TIMESTAMP']=pd.to_datetime(pot_data_all['TIMESTAMP'])
tstring_data_all['TIMESTAMP']=pd.to_datetime(tstring_data_all['TIMESTAMP'])

### Lookup table for thermistor string
SH_table = pd.read_csv(f'{pathtodata}/UW_SH.csv',header=1,skiprows=0,delimiter=',')

### need to figure out where in the table the first record is, because the table repeats due to "append to end of file" feature of CR1000
last_record = pot_data_all.iloc[-1]['RECORD'] # number of the last record in the data table
# stval = -1 * (last_record - 12) #Initially remove first 3 days to reflect when we left the site (and thereby start experiment)
stval = -1 * (last_record - days_to_ignore*4) #'start value'
stval_therm = -1 * (last_record-12)
# stval = -1 * (last_record) # figure out where in the table the first record is, because the table repeats due to "append to end of file" feature of CR1000
# the 120 above cuts the first 120 records (30 days) to account for settling.

potdata = pot_data_all.iloc[stval:] #pull out just the unique records
# data = data.reset_index(drop=True) # reset the pandas index to start at 0
potdata = potdata.set_index(potdata['TIMESTAMP'],drop=True)

tstringdata = tstring_data_all.iloc[stval_therm:] #pull out just the unique records
tstringdata = tstringdata.set_index(tstringdata['TIMESTAMP'],drop=True) # reset the pandas index to start at 0

# data = data.resample('14D').asfreq()
# data = data.resample('14D').mean()
deltat=float(np.diff(potdata.index)[0])/1e9 # put into seconds

######################################
### First deal with the potentiometers
### all the data gets put into pandas dataframes

pot_ranges_mm=np.array([546.0,550.0,550.0,551.0,550.0,550.0,550.0,550.0,551.0,542.0,550.0,309.0])
pot_ranges = 1.0e-3*pot_ranges_mm
# pot_range_13 = 542 # the range of the instrument that replaced old #10, mm
# pot_range_10 = 550 # original #10 that failed. 

### initialize empty dataframes (just the timestamps and record number)
dp = {'RECORD':potdata['RECORD']} 
dfp2 = pd.DataFrame(data=dp,index=potdata.index) 
dfp2a = dfp2.copy()
dfp3 = pd.DataFrame(data=dp,index=potdata.index) 
dfp4 = pd.DataFrame(data=dp,index=potdata.index) 
dfp5 = pd.DataFrame(data=dp,index=potdata.index)
dfp6 = pd.DataFrame(data=dp,index=potdata.index)
dfp6a=dfp6.copy()

drilled_hole_lengths = np.array([4.4,80.0,40.16,29.82,15.1,106.0,19.53,24.85,14.65,9.65,9.75,4.42])
platform_below_surface_cm = np.array([25,25,23,25,25,25,25,20,22,20,15,25])
platform_below_surface = 1e-2*platform_below_surface_cm

init_hole_lengths = drilled_hole_lengths - platform_below_surface
init_hl = np.copy(init_hole_lengths)
hole_length = np.copy(init_hole_lengths)
init_hl_no10 = np.concatenate((init_hole_lengths[:9],init_hole_lengths[10:]))

### Density
'''
density data from firn cores and snow pit
getting the diameter wrong by 1mm adds ~2 percent error.
Accumulation at pole is ~0.07 m W.E per year, or 64 kg/m^3 per year.
Adds ~3.6% more stress to the ~4-5 m depth per year.
'''
rho12_6=np.genfromtxt(f'{pathtodata}/DATA/SPdensity_126.csv',delimiter=',',skip_header=1)
dep12_6=rho12_6[:,0] #depth
den12_6=rho12_6[:,1] #density
rho106=np.genfromtxt(f'{pathtodata}/DATA/SPdensity_106.csv',delimiter=',',skip_header=1)
dep106=rho106[:,0]
den106=rho106[:,1]*1000
rhopit=np.genfromtxt(f'{pathtodata}/DATA/SPdensity_pit.csv',delimiter=',',skip_header=1)
deppit=rhopit[:,0]
denpit=rhopit[:,1]
rhonic=np.genfromtxt(f'{pathtodata}/DATA/SPdensity_nicl.csv',delimiter=',',skip_header=1)
depnic=rhonic[:,0]
dennic=rhonic[:,1]

ind = np.where(dep106>dep12_6[-1])[0]

den_c=np.concatenate((den12_6,den106[ind]))
dep_c=np.concatenate((dep12_6,dep106[ind]))

midpoints = (dep_c[1:]+dep_c[0:-1])/2
mid2=np.append(0,midpoints)
mid3= np.append(mid2,(dep_c[-1]+(dep_c[-1]-mid2[-1])))
layer_thickness = np.diff(mid3)
layer_mass = layer_thickness*den_c
mass_cu = np.cumsum(layer_mass)
stress_cu = mass_cu * 9.8

stress_holebot= -1 * np.interp(drilled_hole_lengths,dep_c,stress_cu)
######

### filter info
### if using butterworth:
fs = 4 / (24*3600) #s^-1
filter_days = 14
cutoff = 1/(filter_days*24*3600)
### if using hanning:
hfildays = 14
wind = 4 * hfildays

# R_ref = 1.0e4 
R_ref = 2.e5 # reference resistors

### now loop through the instruments and fill the dataframes
for ii in range(12):
    pot = ii+1 # which pot we are dealing with

    v_ratio = potdata['Pots%s' %pot] # the measured voltage ratio from the data logger

    t_ratio = potdata['Therms%s' %pot] # the voltage ratio for the thermistor
    r_therm = R_ref * (1 - t_ratio) / t_ratio
    t_box = np.interp(r_therm,therm_res,therm_temp)

    pot_length_unfilt = pot_ranges[ii]*v_ratio # the length of string that is out of the pot

    if pot == 10: #pot 10 had issues (did not work during first year)
        plu11 = pot_ranges[ii+1]*potdata['Pots11'] # Pot length unfiltered, instrument 11.
        # plu11[potdata.index<'2018-01-01']=np.nan
        pot_length_unfilt['2017'] = plu11['2017']+(pot_length_unfilt['2018-01-01'][0]-plu11['2018-01-01'][0])
        # pot_length_unfilt[potdata.index<'2018-01-01']=np.nan

    pot_length_butter = butter_lowpass_filter(pot_length_unfilt, cutoff, fs, order=5)
    pot_length_hanning = smooth(pot_length_unfilt,wind)
    
    pot_length = pot_length_unfilt

    for qq in range(len(pot_length)): # immediately discard any values that are more than 1% different than the 5-day median 
        if ((qq<10) or (qq>len(pot_length)-10)):
            continue
        medint = np.median(pot_length[qq-10:qq+10])
        if ((pot_length[qq]>1.01*medint) or (pot_length[qq]<0.99*medint)):
            pot_length[qq]=np.nan

    pot_length.interpolate(inplace=True) #Fill in any nan
    
    dfp2['pot_length%s' %pot] = pot_length
    dfp2a['pot_length%s' %pot] = pot_length

    ### Apply gaussian filter
    rollsize = 30
    dfp2['pot_length%s' %pot] = dfp2['pot_length%s' %pot].rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
    dfp2.fillna(method='bfill',inplace=True)
    dfp2.fillna(method='ffill',inplace=True)

    if pot==10:
        pot_length[potdata.index<'2018-01-01']=np.nan
    
    dfp6['pot_length_unfilt%s' %pot] = pot_length
    dfp6['pot_length_butter%s' %pot] = pot_length_butter
    dfp6['pot_length_hanning%s' %pot] = pot_length_hanning
    dfp6a['pot_length_unfilt%s' %pot] = pot_length

    # compaction = pot_length[0]-pot_length
    compaction = dfp2['pot_length%s' %pot][0] - dfp2['pot_length%s' %pot]
    if pot==10:
        i_st10 = np.where(np.isnan(dfp6['pot_length_unfilt10'].values)==False)[0][0]
        compaction_unfilt = pot_length[i_st10] - pot_length
    else:    
        compaction_unfilt = pot_length[0] - pot_length
    dfp3['compaction%s' %pot] = compaction
    dfp6['compaction%s' %pot] = compaction_unfilt
    if pot == 10:
        dfp2.loc[:'2018-01-01','pot_length%s' %pot]=np.nan
        dfp2a.loc[:'2018-01-01','pot_length%s' %pot]=np.nan
        dfp6.loc[:'2018-01-01','pot_length_unfilt%s' %pot]=np.nan
        dfp3.loc[:'2018-01-01','compaction%s' %pot]=np.nan
    compaction_rate = np.gradient(compaction,deltat)
    compaction_rate_yr = compaction_rate * SPY
    compaction_rate_unfilt = np.gradient(compaction_unfilt,deltat)
    compaction_rate_yr_unfilt = compaction_rate_unfilt * SPY
    dfp3['compaction_rate%s' %pot] = compaction_rate
    dfp3['compaction_rate_yr%s' %pot] = compaction_rate_yr
    dfp6['compaction_rate%s' %pot] = compaction_rate_unfilt
    dfp6['compaction_rate_yr%s' %pot] = compaction_rate_yr_unfilt
    hole_l = init_hole_lengths[ii] - compaction
    hole_l_unfilt = init_hole_lengths[ii] - compaction_unfilt
    dfp4['hole_length%s' %pot] = hole_l
    dfp6['hole_length%s' %pot] = hole_l_unfilt

    strain = np.log(hole_l / init_hole_lengths[ii]) # This is log strain.
    strain_unfilt = np.log(hole_l_unfilt / init_hole_lengths[ii])
    eng_strain = -1*compaction / init_hole_lengths[ii] # This is log strain.
    eng_strain_unfilt = -1*compaction_unfilt / init_hole_lengths[ii]
    
    dfp4['strain%s' %pot] = strain
    dfp6['strain%s' %pot] = strain_unfilt
    strain_rate = np.gradient(strain,deltat)
    strain_rate_unfilt = np.gradient(strain_unfilt,deltat)
    dfp4['strain_rate%s' %pot] = strain_rate
    dfp4['stress_holebot%s' %pot] = stress_holebot[ii]
    dfp6['strain_rate%s' %pot] = strain_rate_unfilt
    dfp6['stress_holebot%s' %pot] =stress_holebot[ii]
    viscosity = 0.5 * stress_holebot[ii]/strain_rate
    viscosity_unfilt = 0.5 * stress_holebot[ii]/strain_rate_unfilt
    dfp4['viscosity%s' %pot] = viscosity
    dfp6['viscosity%s' %pot] = viscosity_unfilt
    if pot ==10:
        dfp4.loc[:'2018-01-01','viscosity%s' %pot]=np.nan
        dfp4.loc[:'2018-01-01','strain%s' %pot]=np.nan
        dfp4.loc[:'2018-01-01','strain_rate%s' %pot]=np.nan
        dfp4.loc[:'2018-01-01','hole_length%s' %pot]=np.nan
        dfp6.loc[:'2018-01-01','viscosity%s' %pot]=np.nan
        dfp6.loc[:'2018-01-01','strain%s' %pot]=np.nan
        dfp6.loc[:'2018-01-01','strain_rate%s' %pot]=np.nan
        dfp6.loc[:'2018-01-01','hole_length%s' %pot]=np.nan
    dfp5['T_box%s' %pot] = t_box
### done loop


panel_v = potdata['LoggerT']
panel_r = R_ref * (panel_v/(1 - panel_v))
dfp5['LoggerTemp'] = np.interp(panel_r,therm_res,therm_temp)
dfp5['PanelTemp'] = potdata['PTemp_C']

#get rid of first 2 weeks of data (when filter days == 14)
# dfp2 = dfp2.iloc[4*filter_days:-4*filter_days]
# dfp3 = dfp3.iloc[4*filter_days:-4*filter_days]
# dfp4 = dfp4.iloc[4*filter_days:-4*filter_days]
# dfp5 = dfp5.iloc[4*filter_days:-4*filter_days]

# Get rid of first 4 weeks
# drop_days = 0
# dr_st = int(drop_days*4)
dr_st = 16
dr_en = -15
dfp2 = dfp2.iloc[dr_st:dr_en]
dfp3 = dfp3.iloc[dr_st:dr_en]
dfp4 = dfp4.iloc[dr_st:dr_en]
dfp5 = dfp5.iloc[dr_st:dr_en]

dfp6.iloc[0:13_22,dfp6.columns.get_loc('pot_length_unfilt10')] = dfp6.pot_length_unfilt10.iloc[13_22] + (dfp6.pot_length_unfilt11.iloc[0:13_22]-dfp6.pot_length_unfilt11.iloc[13_21])

# dfp6.drop(['RECORD','pot_length_unfilt10'],axis=1,inplace=True)
dfp6.drop(['RECORD'],axis=1,inplace=True)
dfp6a.drop(['RECORD'],axis=1,inplace=True)
dfp7=dfp6a.resample('7d').median()
dfp8=-1*(dfp7-dfp7.iloc[0])
tdels=(dfp8.index[-1]-dfp8.index[0]).total_seconds()
tdely  = tdels/SPY
crate_s = dfp8.iloc[-1]/tdels
crate_y = dfp8.iloc[-1]/tdely #mean compaction rate for the year
# strain_y = crate_y/init_hl_no10
strain_y = crate_y/init_hl
dps = [5,10,15,20,25,30,40,80,106]



total_compaction_y_order = [np.mean((dfp8['pot_length_unfilt1'][-1],dfp8['pot_length_unfilt12'][-1])),
    np.nanmean((dfp8['pot_length_unfilt11'][-1],dfp8['pot_length_unfilt10'][-1])),
    np.mean((dfp8['pot_length_unfilt5'][-1],dfp8['pot_length_unfilt9'][-1])),
    dfp8['pot_length_unfilt7'][-1],
    dfp8['pot_length_unfilt8'][-1],
    dfp8['pot_length_unfilt4'][-1],
    dfp8['pot_length_unfilt3'][-1],
    dfp8['pot_length_unfilt2'][-1],
    dfp8['pot_length_unfilt6'][-1]]

crate_y_order = [np.mean((crate_y.loc['pot_length_unfilt1'],crate_y.loc['pot_length_unfilt12'])),
    np.nanmean((crate_y.loc['pot_length_unfilt11'],crate_y.loc['pot_length_unfilt10'])),
    np.mean((crate_y.loc['pot_length_unfilt5'],crate_y.loc['pot_length_unfilt9'])),
    crate_y.loc['pot_length_unfilt7'],
    crate_y.loc['pot_length_unfilt8'],
    crate_y.loc['pot_length_unfilt4'],
    crate_y.loc['pot_length_unfilt3'],
    crate_y.loc['pot_length_unfilt2'],
    crate_y.loc['pot_length_unfilt6']]

strain_y_order = [np.mean((strain_y.loc['pot_length_unfilt1'],strain_y.loc['pot_length_unfilt12'])),
    np.nanmean((strain_y.loc['pot_length_unfilt11'],strain_y.loc['pot_length_unfilt10'])),
    np.mean((strain_y.loc['pot_length_unfilt5'],strain_y.loc['pot_length_unfilt9'])),
    strain_y.loc['pot_length_unfilt7'],
    strain_y.loc['pot_length_unfilt8'],
    strain_y.loc['pot_length_unfilt4'],
    strain_y.loc['pot_length_unfilt3'],
    strain_y.loc['pot_length_unfilt2'],
    strain_y.loc['pot_length_unfilt6']]

# drilled_hole_lengths = np.array([4.4,80.0,40.16,29.82,15.1,106.0,19.53,24.85,14.65,9.65,9.75,4.42])
hole_l_order = [np.mean((init_hl[0],init_hl[11])),
    np.mean((init_hl[9],init_hl[10])),
    np.mean((init_hl[4],init_hl[8])),
    init_hl_no10[6],
    init_hl_no10[7],
    init_hl_no10[3],
    init_hl_no10[2],
    init_hl_no10[1],
    init_hl_no10[5]]

# option to get rid of the first one (edge effects?)
# dfp2=dfp2[2:]
# dfp3=dfp3[2:]
# dfp4=dfp4[2:]
# dfp5=dfp5[2:]

'''
HOLES:
1   4.4 (25)
2   80  (25)
3   40.16   (23)
4   29.82   (25)
5   15.1    (25)
6   106     (25)
7   19.53   (25)
8   24.85   (20)
9   14.65   (22)
10  9.65    (20)
11  9.75    (15)
12  4.42    (25)

[25,25,23,25,25,25,25,20,22,20,15,25]
'''


dcs = ['1','12','1_11','12_11','1_10','12_10','11_9','10_9','11_5','10_5','9_7','5_7','7_8','8_4','4_3','3_2','2_6']
# holenumber = ['1','12','11','10','9','5','7','7','8','4','3','2','6']
holenumber = ['1','12','11','11','10','10','9','9','5','5','7','7','8','4','3','2','6']

df_dc = pd.DataFrame(data=dp,index=potdata.index)
# df_dc=df_dc[2:] # comment this out if commenting the above out
# df_dc['compaction1']=dfp3['compaction1']
# df_dc['compaction12']=dfp3['compaction12']
# df_dc['compaction1_11']=dfp3['compaction11']-dfp3['compaction1']
# df_dc['compaction12_11']=dfp3['compaction11']-dfp3['compaction12']
# df_dc['compaction1_10']=dfp3['compaction10']-dfp3['compaction1']
# df_dc['compaction12_10']=dfp3['compaction10']-dfp3['compaction12']
# df_dc['compaction11_9']=dfp3['compaction9']-dfp3['compaction11']
# df_dc['compaction10_9']=dfp3['compaction9']-dfp3['compaction10']
# df_dc['compaction11_5']=dfp3['compaction5']-dfp3['compaction11']
# df_dc['compaction10_5']=dfp3['compaction5']-dfp3['compaction10']
# df_dc['compaction9_7']=dfp3['compaction7']-dfp3['compaction9']
# df_dc['compaction5_7']=dfp3['compaction7']-dfp3['compaction5']
# df_dc['compaction7_8']=dfp3['compaction8']-dfp3['compaction7']
# df_dc['compaction8_4']=dfp3['compaction4']-dfp3['compaction8']
# df_dc['compaction4_3']=dfp3['compaction3']-dfp3['compaction4']
# df_dc['compaction3_2']=dfp3['compaction2']-dfp3['compaction3']
# df_dc['compaction2_6']=dfp3['compaction6']-dfp3['compaction2']

# df_dc['hole_length12']=dfp4['hole_length12']
# df_dc['hole_length1']=dfp4['hole_length1']
# df_dc['hole_length1_11']=dfp4['hole_length11']-dfp4['hole_length1']
# df_dc['hole_length12_11']=dfp4['hole_length11']-dfp4['hole_length12']
# df_dc['hole_length1_10']=dfp4['hole_length10']-dfp4['hole_length1']
# df_dc['hole_length12_10']=dfp4['hole_length10']-dfp4['hole_length12']
# df_dc['hole_length11_9']=dfp4['hole_length9']-dfp4['hole_length11']
# df_dc['hole_length10_9']=dfp4['hole_length9']-dfp4['hole_length10']
# df_dc['hole_length11_5']=dfp4['hole_length5']-dfp4['hole_length11']
# df_dc['hole_length10_5']=dfp4['hole_length5']-dfp4['hole_length10']
# df_dc['hole_length9_7']=dfp4['hole_length7']-dfp4['hole_length9']
# df_dc['hole_length5_7']=dfp4['hole_length7']-dfp4['hole_length5']
# df_dc['hole_length7_8']=dfp4['hole_length8']-dfp4['hole_length7']
# df_dc['hole_length8_4']=dfp4['hole_length4']-dfp4['hole_length8']
# df_dc['hole_length4_3']=dfp4['hole_length3']-dfp4['hole_length4']
# df_dc['hole_length3_2']=dfp4['hole_length2']-dfp4['hole_length3']
# df_dc['hole_length2_6']=dfp4['hole_length6']-dfp4['hole_length2']

# pot_length_butter = butter_lowpass_filter(pot_length_unfilt, cutoff, fs, order=5)

# df_dc['hole_length12%s' %pot] = dfp2['pot_length%s' %pot].rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()

df_dc['hole_length12'] = dfp6['hole_length12'].rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length1'] = dfp6['hole_length1'].rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length1_11'] = (dfp6['hole_length11'] - dfp6['hole_length1']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length12_11'] = (dfp6['hole_length11'] - dfp6['hole_length12']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length1_10'] = (dfp6['hole_length10'] - dfp6['hole_length1']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length12_10'] = (dfp6['hole_length10'] - dfp6['hole_length12']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length11_9'] = (dfp6['hole_length9'] - dfp6['hole_length11']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length10_9'] = (dfp6['hole_length9'] - dfp6['hole_length10']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length11_5'] = (dfp6['hole_length5'] - dfp6['hole_length11']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length10_5'] = (dfp6['hole_length5'] - dfp6['hole_length10']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length9_7'] = (dfp6['hole_length7'] - dfp6['hole_length9']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length5_7'] = (dfp6['hole_length7'] - dfp6['hole_length5']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length7_8'] = (dfp6['hole_length8'] - dfp6['hole_length7']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length8_4'] = (dfp6['hole_length4'] - dfp6['hole_length8']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length4_3'] = (dfp6['hole_length3'] - dfp6['hole_length4']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length3_2'] = (dfp6['hole_length2'] - dfp6['hole_length3']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
df_dc['hole_length2_6'] = (dfp6['hole_length6'] - dfp6['hole_length2']).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()

for hhl in dcs:
    df_dc['hole_length{}'.format(hhl)].fillna(method='bfill',inplace=True)
    df_dc['hole_length{}'.format(hhl)].fillna(method='ffill',inplace=True)


# df_dc['hole_length12'] = butter_lowpass_filter((dfp6['hole_length12']), cutoff, fs, order=5)
# df_dc['hole_length1'] = butter_lowpass_filter((dfp6['hole_length1']), cutoff, fs, order=5)
# df_dc['hole_length1_11'] = butter_lowpass_filter((dfp6['hole_length11'] - dfp6['hole_length1']), cutoff, fs, order=5)
# df_dc['hole_length12_11'] = butter_lowpass_filter((dfp6['hole_length11'] - dfp6['hole_length12']), cutoff, fs, order=5)
# df_dc['hole_length1_10'] = butter_lowpass_filter((dfp6['hole_length10'] - dfp6['hole_length1']), cutoff, fs, order=5)
# df_dc['hole_length12_10'] = butter_lowpass_filter((dfp6['hole_length10'] - dfp6['hole_length12']), cutoff, fs, order=5)
# df_dc['hole_length11_9'] = butter_lowpass_filter((dfp6['hole_length9'] - dfp6['hole_length11']), cutoff, fs, order=5)
# df_dc['hole_length10_9'] = butter_lowpass_filter((dfp6['hole_length9'] - dfp6['hole_length10']), cutoff, fs, order=5)
# df_dc['hole_length11_5'] = butter_lowpass_filter((dfp6['hole_length5'] - dfp6['hole_length11']), cutoff, fs, order=5)
# df_dc['hole_length10_5'] = butter_lowpass_filter((dfp6['hole_length5'] - dfp6['hole_length10']), cutoff, fs, order=5)
# df_dc['hole_length9_7'] = butter_lowpass_filter((dfp6['hole_length7'] - dfp6['hole_length9']), cutoff, fs, order=5)
# df_dc['hole_length5_7'] = butter_lowpass_filter((dfp6['hole_length7'] - dfp6['hole_length5']), cutoff, fs, order=5)
# df_dc['hole_length7_8'] = butter_lowpass_filter((dfp6['hole_length8'] - dfp6['hole_length7']), cutoff, fs, order=5)
# df_dc['hole_length8_4'] = butter_lowpass_filter((dfp6['hole_length4'] - dfp6['hole_length8']), cutoff, fs, order=5)
# df_dc['hole_length4_3'] = butter_lowpass_filter((dfp6['hole_length3'] - dfp6['hole_length4']), cutoff, fs, order=5)
# df_dc['hole_length3_2'] = butter_lowpass_filter((dfp6['hole_length2'] - dfp6['hole_length3']), cutoff, fs, order=5)
# df_dc['hole_length2_6'] = butter_lowpass_filter((dfp6['hole_length6'] - dfp6['hole_length2']), cutoff, fs, order=5)

dclistt = ['1','12','11','5','9','7','8','4','3','2','1','12','11','5','9','7','8','4','3','1','12','11','5','9','7','8','4','1','12','11','5','9','7','8','1','2','1','12','11','11']
dclistb = ['6','6','6','6','6','6','6','6','6','6','2','2','2','2','2','2','2','2','2','3','3','3','3','3','3','3','3','4','4','4','4','4','4','4','11','11','5','5','5','9']

for rr in range(len(dclistt)):
    df_dc['hole_length{}_{}'.format(dclistt[rr],dclistb[rr])] = (dfp6['hole_length{}'.format(dclistb[rr])] - dfp6['hole_length{}'.format(dclistt[rr])]).rolling(rollsize,win_type='gaussian',center=True).mean(std=rollsize/3).copy()
    df_dc['hole_length{}_{}'.format(dclistt[rr],dclistb[rr])].fillna(method='bfill',inplace=True)
    df_dc['hole_length{}_{}'.format(dclistt[rr],dclistb[rr])].fillna(method='ffill',inplace=True)
    df_dc['compaction{}_{}'.format(dclistt[rr],dclistb[rr])] = df_dc['hole_length{}_{}'.format(dclistt[rr],dclistb[rr])][0] - df_dc['hole_length{}_{}'.format(dclistt[rr],dclistb[rr])]
    df_dc['compaction_rate{}_{}'.format(dclistt[rr],dclistb[rr])]=np.gradient(df_dc['compaction{}_{}'.format(dclistt[rr],dclistb[rr])],deltat)
    df_dc[((df_dc.columns.str.contains('compaction')) & (df_dc<0))]=0
    df_dc['strain{}_{}'.format(dclistt[rr],dclistb[rr])]=df_dc['compaction{}_{}'.format(dclistt[rr],dclistb[rr])]/df_dc['hole_length{}_{}'.format(dclistt[rr],dclistb[rr])]

for ii,xx in enumerate(dcs):
    df_dc['compaction{}'.format(xx)] = df_dc['hole_length{}'.format(xx)][0] - df_dc['hole_length{}'.format(xx)]


# df_dc['compaction1'] = dfp6['compaction1']
# df_dc['compaction12'] = dfp6['compaction12']
# df_dc['compaction1_11'] = dfp6['compaction11'] - dfp6['compaction1']
# df_dc['compaction12_11'] = dfp6['compaction11'] - dfp6['compaction12']
# df_dc['compaction1_10'] = dfp6['compaction10'] - dfp6['compaction1']
# df_dc['compaction12_10'] = dfp6['compaction10'] - dfp6['compaction12']
# df_dc['compaction11_9'] = dfp6['compaction9'] - dfp6['compaction11']
# df_dc['compaction10_9'] = dfp6['compaction9'] - dfp6['compaction10']
# df_dc['compaction11_5'] = dfp6['compaction5'] - dfp6['compaction11']
# df_dc['compaction10_5'] = dfp6['compaction5'] - dfp6['compaction10']
# df_dc['compaction9_7'] = dfp6['compaction7'] - dfp6['compaction9']
# df_dc['compaction5_7'] = dfp6['compaction7'] - dfp6['compaction5']
# df_dc['compaction7_8'] = dfp6['compaction8'] - dfp6['compaction7']
# df_dc['compaction8_4'] = dfp6['compaction4'] - dfp6['compaction8']
# df_dc['compaction4_3'] = dfp6['compaction3'] - dfp6['compaction4']
# df_dc['compaction3_2'] = dfp6['compaction2'] - dfp6['compaction3']
# df_dc['compaction2_6'] = dfp6['compaction6'] - dfp6['compaction2']



# df_dc['hole_bottom12']=dfp4['hole_length12']
# df_dc['hole_bottom1']=dfp4['hole_length1']
# df_dc['hole_bottom1_11']=dfp4['hole_length11']
# df_dc['hole_bottom12_11']=dfp4['hole_length11']
# df_dc['hole_bottom1_10']=dfp4['hole_length10']
# df_dc['hole_bottom12_10']=dfp4['hole_length10']
# df_dc['hole_bottom11_9']=dfp4['hole_length9']
# df_dc['hole_bottom10_9']=dfp4['hole_length9']
# df_dc['hole_bottom11_5']=dfp4['hole_length5']
# df_dc['hole_bottom10_5']=dfp4['hole_length5']
# df_dc['hole_bottom9_7']=dfp4['hole_length7']
# df_dc['hole_bottom5_7']=dfp4['hole_length7']
# df_dc['hole_bottom7_8']=dfp4['hole_length8']
# df_dc['hole_bottom8_4']=dfp4['hole_length4']
# df_dc['hole_bottom4_3']=dfp4['hole_length3']
# df_dc['hole_bottom3_2']=dfp4['hole_length2']
# df_dc['hole_bottom2_6']=dfp4['hole_length6']

df_dc['compaction_rate1']=np.gradient(df_dc['compaction1'],deltat)
df_dc['compaction_rate12']=np.gradient(df_dc['compaction12'],deltat)
df_dc['compaction_rate1_11']=np.gradient(df_dc['compaction1_11'],deltat)
df_dc['compaction_rate12_11']=np.gradient(df_dc['compaction12_11'],deltat)
df_dc['compaction_rate1_10']=np.gradient(df_dc['compaction1_10'],deltat)
df_dc['compaction_rate12_10']=np.gradient(df_dc['compaction12_10'],deltat)
df_dc['compaction_rate11_9']=np.gradient(df_dc['compaction11_9'],deltat)
df_dc['compaction_rate10_9']=np.gradient(df_dc['compaction10_9'],deltat)
df_dc['compaction_rate11_5']=np.gradient(df_dc['compaction11_5'],deltat)
df_dc['compaction_rate10_5']=np.gradient(df_dc['compaction10_5'],deltat)
df_dc['compaction_rate9_7']=np.gradient(df_dc['compaction9_7'],deltat)
df_dc['compaction_rate5_7']=np.gradient(df_dc['compaction5_7'],deltat)
df_dc['compaction_rate7_8']=np.gradient(df_dc['compaction7_8'],deltat)
df_dc['compaction_rate8_4']=np.gradient(df_dc['compaction8_4'],deltat)
df_dc['compaction_rate4_3']=np.gradient(df_dc['compaction4_3'],deltat)
df_dc['compaction_rate3_2']=np.gradient(df_dc['compaction3_2'],deltat)
df_dc['compaction_rate2_6']=np.gradient(df_dc['compaction2_6'],deltat)

df_dc[((df_dc.columns.str.contains('compaction')) & (df_dc<0))]=0

# df_dc['strain1']=dfp4['strain1']
# df_dc['strain12']=dfp4['strain12']
# df_dc['strain1_11']=dfp4['strain11']-dfp4['strain1']
# df_dc['strain12_11']=dfp4['strain11']-dfp4['strain12']
# df_dc['strain1_10']=dfp4['strain10']-dfp4['strain1']
# df_dc['strain12_10']=dfp4['strain10']-dfp4['strain12']
# df_dc['strain11_9']=dfp4['strain9']-dfp4['strain11']
# df_dc['strain10_9']=dfp4['strain9']-dfp4['strain10']
# df_dc['strain11_5']=dfp4['strain5']-dfp4['strain11']
# df_dc['strain10_5']=dfp4['strain5']-dfp4['strain10']
# df_dc['strain9_7']=dfp4['strain7']-dfp4['strain9']
# df_dc['strain5_7']=dfp4['strain7']-dfp4['strain5']
# df_dc['strain7_8']=dfp4['strain8']-dfp4['strain7']
# df_dc['strain8_4']=dfp4['strain4']-dfp4['strain8']
# df_dc['strain4_3']=dfp4['strain3']-dfp4['strain4']
# df_dc['strain3_2']=dfp4['strain2']-dfp4['strain3']
# df_dc['strain2_6']=dfp4['strain6']-dfp4['strain2']

df_dc['strain1']=df_dc['compaction1']/df_dc['hole_length1']
df_dc['strain12']=df_dc['compaction12']/df_dc['hole_length12']
df_dc['strain1_11']=df_dc['compaction1_11']/df_dc['hole_length1_11']
df_dc['strain12_11']=df_dc['compaction12_11']/df_dc['hole_length12_11']
df_dc['strain1_10']=df_dc['compaction1_10']/df_dc['hole_length1_10']
df_dc['strain12_10']=df_dc['compaction12_10']/df_dc['hole_length12_10']
df_dc['strain11_9']=df_dc['compaction11_9']/df_dc['hole_length11_9']
df_dc['strain10_9']=df_dc['compaction10_9']/df_dc['hole_length10_9']
df_dc['strain11_5']=df_dc['compaction11_5']/df_dc['hole_length11_5']
df_dc['strain10_5']=df_dc['compaction10_5']/df_dc['hole_length10_5']
df_dc['strain9_7']=df_dc['compaction9_7']/df_dc['hole_length9_7']
df_dc['strain5_7']=df_dc['compaction5_7']/df_dc['hole_length5_7']
df_dc['strain7_8']=df_dc['compaction7_8']/df_dc['hole_length7_8']
df_dc['strain8_4']=df_dc['compaction8_4']/df_dc['hole_length8_4']
df_dc['strain4_3']=df_dc['compaction4_3']/df_dc['hole_length4_3']
df_dc['strain3_2']=df_dc['compaction3_2']/df_dc['hole_length3_2']
df_dc['strain2_6']=df_dc['compaction2_6']/df_dc['hole_length2_6']

for ind,kk in enumerate(dcs):
    holeno = holenumber[ind]
    ### the following for finding strain by subtracting compaction
    # strain_d = df_dc['compaction%s' %kk]/df_dc['hole_length%s' %kk]
    # df_dc['strain%s' %kk] = strain_d
    #strain_rate_d = np.gradient(strain_d,deltat)
    
    ### following for using the individual holes' strain, subtracted
    strain_rate_d = np.gradient(df_dc['strain%s' %kk],deltat)
    # print(np.where(np.isnan(strain_rate_d)))
    strain_rate_d[strain_rate_d<0.0] = 0.0
    strain_rate_d = strain_rate_d * -1.0
    df_dc['strain_rate%s' %kk] = strain_rate_d
    viscosity_d = 0.5 * dfp6['stress_holebot%s' %holeno]/strain_rate_d
    df_dc['viscosity%s' %kk] = viscosity_d

df_dc.replace([np.inf,-np.inf],np.nan,inplace=True)

# dfp6 = dfp6.iloc[FD_mult*4*filter_days:-4*filter_days]
# df_dc = df_dc.iloc[FD_mult*4*filter_days:-4*filter_days]

dfp6 = dfp6.iloc[dr_st:dr_en]
df_dc = df_dc.iloc[dr_st:dr_en]

###############################
###############################
### now the thermistor string
therm_depths = np.array([0, 0.75, 1.5, 3, 6, 12, 20, 35, 0.25, 1.00, 2.0, 4, 8, 14, 25, 40, 0.5, 1.25, 2.5, 5, 10, 17, 30]) # depths of the thermistors
dth = {'TIMESTAMP':tstringdata['TIMESTAMP'], 'RECORD':tstringdata['RECORD']} 
dft2 = pd.DataFrame(data=dth) #dataframe that is initially just the timestamps and record number, and will also get the temperatures in the loop.

tt1=np.zeros((len(dft2),23))

for ii in range(23): #there are 23 thermistors

    therm = ii + 1
    C0 = SH_table['C0'][ii]
    C1 = SH_table['C1'][ii]
    C3 = SH_table['C3'][ii]

    R = tstringdata['Therm_Res%s' %therm]

    Tc = 1/ (C0+C1*np.log(R)+C3*(np.log(R))**3) - 273.15
    Tc_r = np.round(Tc*2,decimals=1)/2

    dft2['Therm_temp%s' %therm] = Tc_r
    tt1[:,ii]=Tc


# df2 = df2.reset_index(drop=True)
dft3 = dft2.set_index('RECORD').T
dft3['depth']=np.append(-9999, therm_depths)

dft4 = dft3.sort_values(by='depth') # the final dataframe that has temperatures and depths for each thermistor.

dft5 = dft4.T.set_index('TIMESTAMP')
tdeps = dft5.iloc[-1].values
dft5.drop(-9999,inplace=True)
dft5.index=pd.to_datetime(dft5.index)
dft5 = dft5.apply(pd.to_numeric)

# with open('/Users/maxstev/Documents/Grad_School/Research/SouthPole/ens_data_SP50.pkl','rb') as f:
    # md=pickle.load(f)

