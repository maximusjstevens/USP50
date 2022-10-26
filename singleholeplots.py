### PLOT FOR EACH OF THE INDIVIDUAL HOLES, DATA RESAMPLED DAILY TO COMPARE WITH MODEL
dfp_daily = dfp3.resample('d').mean()
daily_index = dfp_daily.index
# idds = 28#28
idds='01-01-2017'
# idde = -28#-28
idde = '12-20-2018'
# %matplotlib inline
palette = sns.color_palette()
figex = '_211207.pdf'
# plt.rcParams.update({'figure.max_open_warning': 0})
plt.rcParams['figure.figsize'] = [12,6]
fcr5,acr5=plt.subplots()
fcr10,acr10=plt.subplots()
fcr15,acr15=plt.subplots()
fcr20,acr20=plt.subplots()
fcr25,acr25=plt.subplots()
fcr30,acr30=plt.subplots()
fcr40,acr40=plt.subplots()
fcr80,acr80=plt.subplots()
fcr106,acr106=plt.subplots()

data_decimaldates=np.zeros(len(dfp3.index))
for kk,dat in enumerate(dfp3.index):
    data_decimaldates[kk]=toYearFraction(dfp3.index[kk])

datacolor = 'k'
datacolor2 = 'k'
# thenames = ['HLdynamic','GSFC2020','MaxSP']
for ll,name in enumerate(thenames): #plot model results
#     try:
#         colo,legname = get_plotdeets(name)
#     except:
#         colo,legname = 'b','SP_10m'
#     colo='b'
#     legname = 'manT'
#     if name == 'MaxSP':
#         continue
    colo, legname = get_plotdeets(name)

#     colo,legname = palette[ll],name
#     if name=='MaxSP':
#         legname = 'This work'
#         colo = 'tab:red'
        # continue
    # else:
    #     continue

    acr5.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate5'][idds:idde],label=legname,color=colo)
    acr10.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate10'][idds:idde],label=legname,color=colo)
    acr15.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate15'][idds:idde],label=legname,color=colo)
    acr20.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate20'][idds:idde],label=legname,color=colo)
    acr25.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate25'][idds:idde],label=legname,color=colo)
    acr30.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate30'][idds:idde],label=legname,color=colo)
    acr40.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate40'][idds:idde],label=legname,color=colo)
    acr80.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate80'][idds:idde],label=legname,color=colo)
    acr106.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate106'][idds:idde],label=legname,color=colo)

data_decimaldates=np.zeros(len(dfp3.index))
for kk,dat in enumerate(dfp3.index):
    data_decimaldates[kk]=toYearFraction(dfp3.index[kk])
    
    
### now plot data from SP50
acr5.plot(dfp_daily[idds:idde].index,dfp_daily.compaction_rate_yr1[idds:idde],color = datacolor,linestyle='--',label='data')
acr5.plot(dfp_daily[idds:idde].index,dfp_daily.compaction_rate_yr12[idds:idde],color = datacolor2,linestyle='--')
acr10.plot(dfp_daily[idds:idde].index,dfp_daily.compaction_rate_yr11[idds:idde],color = datacolor,linestyle='--',label='data')
acr15.plot(dfp_daily[idds:idde].index,dfp_daily.compaction_rate_yr5[idds:idde],color = datacolor,linestyle='--')
acr15.plot(dfp_daily[idds:idde].index,dfp_daily.compaction_rate_yr9[idds:idde],color = datacolor2,linestyle='--')
acr20.plot(dfp_daily[idds:idde].index,dfp_daily.compaction_rate_yr7[idds:idde],color = datacolor,linestyle='--')
acr25.plot(dfp_daily[idds:idde].index,dfp_daily.compaction_rate_yr8[idds:idde],color = datacolor,linestyle='--')
acr30.plot(dfp_daily[idds:idde].index,dfp_daily.compaction_rate_yr4[idds:idde],color = datacolor,linestyle='--')
acr40.plot(dfp_daily[idds:idde].index,dfp_daily.compaction_rate_yr3[idds:idde],color = datacolor,linestyle='--')
acr80.plot(dfp_daily[idds:idde].index,dfp_daily.compaction_rate_yr2[idds:idde],color = datacolor,linestyle='--')
acr106.plot(dfp_daily[idds:idde].index,dfp_daily.compaction_rate_yr6[idds:idde],color = datacolor,linestyle='--')

acr15.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
acr15.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
acr15.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
acr15.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
acr15.text(DT.date(2017, 7, 9), 0.202, "WINTER",fontsize=16,fontweight='bold')
acr15.text(DT.date(2018, 1, 7), 0.202, "SUMMER",fontsize=16,fontweight='bold')

acr106.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
acr106.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
acr106.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
acr106.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
acr106.text(DT.date(2017, 7, 9), 0.24, "WINTER",fontsize=16,fontweight='bold')
acr106.text(DT.date(2018, 1, 7), 0.24, "SUMMER",fontsize=16,fontweight='bold')

########
hs = ['5','10','15','20','25','30','40','80','106','106_5','106_10','106_15','106_20','106_25','106_30','106_40','106_80','80_5','80_10','80_15','80_20','80_25','80_30','80_40','40_5','40_10','40_15','40_20','40_25','40_30','30_5','30_10','30_15','30_20','30_25']
# acr5.legend()
acr5.set_title('5-m hole')
acr5.set_xlabel('Date')
acr5.set_ylabel('Compaction rate (m yr$^{-1}$)')
acr5.grid(True)
acr5.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))

acr10.set_title('10-m hole')
acr10.set_xlabel('Date')
acr10.set_ylabel('Compaction rate (m yr$^{-1}$)')
acr10.grid(True)
acr10.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))

acr15.set_title('15-m hole')
acr15.set_xlabel('Date')
acr15.set_ylabel('Compaction rate (m yr$^{-1}$)')
acr15.grid(True)
acr15.set_xlim(date2num(datetime(2017,2,5)),date2num(datetime(2018,12,1)))
acr15.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))

acr20.set_title('20-m hole')
acr20.set_xlabel('Date')
acr20.set_ylabel('Compaction rate (m yr$^{-1}$)')
acr20.grid(True)
acr20.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))

acr25.set_title('25-m hole')
acr25.set_xlabel('Date')
acr25.set_ylabel('Compaction rate (m yr$^{-1}$)')
acr25.grid(True)
acr25.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))

acr30.set_title('30-m hole')
acr30.set_xlabel('Date')
acr30.set_ylabel('Compaction rate (m yr$^{-1}$)')
acr30.grid(True)
acr30.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))

acr40.set_title('40-m hole')
acr40.set_xlabel('Date')
acr40.set_ylabel('Compaction rate (m yr$^{-1}$)')
acr40.grid(True)
acr40.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))

acr80.set_title('80-m hole')
acr80.set_xlabel('Date')
acr80.set_ylabel('Compaction rate (m yr$^{-1}$)')
acr80.grid(True)
acr80.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))

# acr106.set_title('106-m hole')
acr106.set_xlabel('Date')
acr106.set_ylabel('Compaction rate (m yr$^{-1}$)')
acr106.grid(True)
# acr106.legend()
acr106.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))
acr106.set_xlim(date2num(datetime(2017,2,5)),date2num(datetime(2018,12,1)))
acr106.set_ylim(0.09,0.26)
# acr106.set_xlim(2017.2,2018.0)
###############

fcr5.savefig('figures/compaction_5m_data_model_%s' %fil + figex)
fcr10.savefig('figures/compaction_10m_data_model_%s' %fil + figex)
fcr15.savefig('figures/compaction_15m_data_model_%s' %fil + figex)
fcr20.savefig('figures/compaction_20m_data_model_%s' %fil + figex)
fcr25.savefig('figures/compaction_25m_data_model_%s' %fil + figex)
fcr30.savefig('figures/compaction_30m_data_model_%s' %fil + figex)
fcr40.savefig('figures/compaction_40m_data_model_%s' %fil + figex)
fcr80.savefig('figures/compaction_80m_data_model_%s' %fil + figex)
fcr106.savefig('figures/compaction_106m_data_model_%s' %fil + figex)


handles,labels = acr10.get_legend_handles_labels()
fxe,axe=plt.subplots()
axe.legend(handles, labels)
axe.xaxis.set_visible(False)
axe.yaxis.set_visible(False)
for v in axe.spines.values():
    v.set_visible(False)
fxe.savefig('figures/LegendModelData' + figex)