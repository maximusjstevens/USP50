# plotmodel=True

fig2 = plt.figure(constrained_layout=False,figsize=(13,12))
spec2 = gridspec.GridSpec(ncols=2, nrows=5, figure=fig2, height_ratios=[1.065,0.5,0.5,0.5,0.5])#,width_ratios=[3,3])
spec2.update(wspace=0.14,hspace=0.35) # set the spacing between axes.

idds = dfp3.index[0]
idde = dfp3.index[-1]

f2_ax1 = fig2.add_subplot(spec2[0, :])
f2_ax1.plot(dfp3.index,dfp3.compaction_rate_yr6,color='k',ls='--',label='Data')
f2_ax1.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), color="tomato", alpha=0.3)
f2_ax1.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), color="tomato", alpha=0.3)
f2_ax1.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), color="cornflowerblue", alpha=0.3)
f2_ax1.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), color="cornflowerblue", alpha=0.3)
f2_ax1.text(DT.date(2017, 8, 5), 0.23, "WINTER",fontsize=16,fontweight='bold',ha='center')
f2_ax1.text(DT.date(2018, 2, 5), 0.23, "SUMMER",fontsize=16,fontweight='bold',ha='center')
f2_ax1.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

# f2_ax2 = fig2.add_subplot(spec2[0, 1])
f2_ax3 = fig2.add_subplot(spec2[1, 0])
f2_ax3.plot(dfp3.index,dfp3.compaction_rate_yr2,color='k',ls='--')
f2_ax3.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax3.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax3.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax3.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax3.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

f2_ax4 = fig2.add_subplot(spec2[1, 1])
f2_ax4.plot(dfp3.index,dfp3.compaction_rate_yr3,color='k',ls='--')
f2_ax4.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax4.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax4.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax4.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax4.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

f2_ax5 = fig2.add_subplot(spec2[2, 0])
f2_ax5.plot(dfp3.index,dfp3.compaction_rate_yr4,color='k',ls='--')
f2_ax5.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax5.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax5.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax5.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax5.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

f2_ax6 = fig2.add_subplot(spec2[2, 1])
f2_ax6.plot(dfp3.index,dfp3.compaction_rate_yr8,color='k',ls='--')
f2_ax6.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax6.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax6.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax6.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax6.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

f2_ax7 = fig2.add_subplot(spec2[3, 0])
f2_ax7.plot(dfp3.index,dfp3.compaction_rate_yr7,color='k',ls='--')
f2_ax7.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax7.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax7.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax7.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax7.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

f2_ax8 = fig2.add_subplot(spec2[3, 1])
f2_ax8.plot(dfp3.index,dfp3.compaction_rate_yr5,color='k',ls='--')
f2_ax8.plot(dfp3.index,dfp3.compaction_rate_yr9,color='k',ls='--')
f2_ax8.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax8.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax8.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax8.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax8.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

f2_ax9 = fig2.add_subplot(spec2[4, 0])
f2_ax9.plot(dfp3.index,dfp3.compaction_rate_yr10,color='k',ls='--')
f2_ax9.plot(dfp3.index,dfp3.compaction_rate_yr11,color='k',ls='--')
f2_ax9.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax9.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax9.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax9.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax9.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

f2_ax10 = fig2.add_subplot(spec2[4, 1])
f2_ax10.plot(dfp3.index,dfp3.compaction_rate_yr12,color='k',ls='--')
f2_ax10.plot(dfp3.index,dfp3.compaction_rate_yr1,color='k',ls='--')
f2_ax10.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax10.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
f2_ax10.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax10.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
f2_ax10.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

bbox=f2_ax1.get_position()
offset=0.03
f2_ax1.set_position([bbox.x0, bbox.y0 + offset, bbox.x1-bbox.x0, bbox.y1 - bbox.y0])

if plotmodel:
    for ll,name in enumerate(thenames): #plot model results
#         colo,legname = palette[ll],name
        colo, legname = get_plotdeets(name)
        if name=='MaxSP':
            legname = 'This work'


        f2_ax1.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate106'][idds:idde],label=legname,color=colo)
        f2_ax3.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate80'][idds:idde],label=legname,color=colo)
        f2_ax4.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate40'][idds:idde],label=legname,color=colo)
        f2_ax5.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate30'][idds:idde],label=legname,color=colo)
        f2_ax6.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate25'][idds:idde],label=legname,color=colo)
        f2_ax7.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate20'][idds:idde],label=legname,color=colo)
        f2_ax8.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate15'][idds:idde],label=legname,color=colo)
        f2_ax9.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate10'][idds:idde],label=legname,color=colo)
        f2_ax10.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate5'][idds:idde],label=legname,color=colo)

f2_ax1.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))
f2_ax9.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))
f2_ax10.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))
f2_ax3.tick_params(labelbottom=False)
f2_ax4.tick_params(labelbottom=False)
f2_ax5.tick_params(labelbottom=False)
f2_ax6.tick_params(labelbottom=False)
f2_ax7.tick_params(labelbottom=False)
f2_ax8.tick_params(labelbottom=False)

f2_ax1.set_title('106 m hole')
f2_ax3.set_title('80 m hole',fontsize=18)
f2_ax4.set_title('40 m hole',fontsize=18)
f2_ax5.set_title('30 m hole',fontsize=18)
f2_ax6.set_title('25 m hole',fontsize=18)
f2_ax7.set_title('20 m hole',fontsize=18)
f2_ax8.set_title('15 m holes',fontsize=18)
f2_ax9.set_title('10 m holes',fontsize=18)
f2_ax10.set_title('4 m holes',fontsize=18)

syl = True
if syl:
    f2_ax1.set_ylim((0.08,0.25))
    f2_ax3.set_ylim((0.06,0.21))
    f2_ax4.set_ylim((0.06,0.21))
    f2_ax5.set_ylim((0.05,0.21))
    f2_ax6.set_ylim((0.05,0.21))
    f2_ax7.set_ylim((0.0,0.18))
    f2_ax8.set_ylim((0.0,0.18))
    f2_ax9.set_ylim((0,0.18))
    f2_ax10.set_ylim((0,0.18))
f2_ax3.tick_params(axis = 'both', which = 'major', labelsize = 14)
f2_ax4.tick_params(axis = 'both', which = 'major', labelsize = 14)
f2_ax5.tick_params(axis = 'both', which = 'major', labelsize = 14)
f2_ax6.tick_params(axis = 'both', which = 'major', labelsize = 14)
f2_ax7.tick_params(axis = 'both', which = 'major', labelsize = 14)
f2_ax8.tick_params(axis = 'both', which = 'major', labelsize = 14)
f2_ax9.tick_params(axis = 'both', which = 'major', labelsize = 14)
f2_ax10.tick_params(axis = 'both', which = 'major', labelsize = 14)
# f2_ax10.tick_params(axis = 'both', which = 'minor', labelsize = 16)

# fig2.text(0.001, 0.5, r'Compaction rate (m a$^{-1}$)', va='center', rotation='vertical',fontsize=20))
# f2_ax1.set_ylabel('Compaction rate\n(m a$^{-1}$)')
fig2.text(0.04, 0.5, 'Compaction rate (m a$^{-1}$)', va='center', rotation='vertical',fontsize=20)
fig2.text(0.5, 0.08, 'Date (month/year)', va='center', ha='center',fontsize=20)

# fig2.tight_layout()
if plotmodel:
    if not KJtest:
        f2_ax1.legend(ncol=1,prop={'size': 10})
        fig2.savefig('CompRate_panel_model.pdf')
        fig2.savefig('/Users/maxstev/Documents/Grad_School/Manuscripts/Stevens_SPfirn/texfigures/CompRate_panel_model.pdf')
    elif KJtest:
        f2_ax1.legend(ncol=1,prop={'size': 10})
        fig2.savefig('CompRate_panel_KJtest.pdf')
        fig2.savefig('/Users/maxstev/Documents/Grad_School/Manuscripts/Stevens_SPfirn/texfigures/CompRate_panel_KJtest.pdf')
        
else:
    fig2.savefig('CompRate_panel_dataonly.pdf')
    fig2.savefig('/Users/maxstev/Documents/Grad_School/Manuscripts/Stevens_SPfirn/texfigures/CompRate_panel_dataonly.pdf')



#########################
# older with legend stuff below


# plotmodel=True

# fig2 = plt.figure(constrained_layout=False,figsize=(13,12))
# spec2 = gridspec.GridSpec(ncols=2, nrows=5, figure=fig2, height_ratios=[1.065,0.5,0.5,0.5,0.5])#,width_ratios=[3,3])
# spec2.update(wspace=0.14,hspace=0.35) # set the spacing between axes.

# idds = dfp3.index[0]
# idde = dfp3.index[-1]

# f2_ax1 = fig2.add_subplot(spec2[0, :])
# f2_ax1.plot(dfp3.index,dfp3.compaction_rate_yr6,color='k',ls='--',label='Data')
# f2_ax1.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax1.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax1.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax1.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax1.text(DT.date(2017, 8, 5), 0.24, "WINTER",fontsize=16,fontweight='bold',ha='center')
# f2_ax1.text(DT.date(2018, 2, 5), 0.24, "SUMMER",fontsize=16,fontweight='bold',ha='center')
# f2_ax1.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

# # f2_ax2 = fig2.add_subplot(spec2[0, 1])
# f2_ax3 = fig2.add_subplot(spec2[1, 0])
# f2_ax3.plot(dfp3.index,dfp3.compaction_rate_yr2,color='k',ls='--')
# f2_ax3.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax3.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax3.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax3.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax3.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

# f2_ax4 = fig2.add_subplot(spec2[1, 1])
# f2_ax4.plot(dfp3.index,dfp3.compaction_rate_yr3,color='k',ls='--')
# f2_ax4.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax4.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax4.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax4.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax4.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

# f2_ax5 = fig2.add_subplot(spec2[2, 0])
# f2_ax5.plot(dfp3.index,dfp3.compaction_rate_yr4,color='k',ls='--')
# f2_ax5.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax5.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax5.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax5.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax5.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

# f2_ax6 = fig2.add_subplot(spec2[2, 1])
# f2_ax6.plot(dfp3.index,dfp3.compaction_rate_yr8,color='k',ls='--')
# f2_ax6.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax6.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax6.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax6.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax6.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

# f2_ax7 = fig2.add_subplot(spec2[3, 0])
# f2_ax7.plot(dfp3.index,dfp3.compaction_rate_yr7,color='k',ls='--')
# f2_ax7.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax7.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax7.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax7.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax7.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

# f2_ax8 = fig2.add_subplot(spec2[3, 1])
# f2_ax8.plot(dfp3.index,dfp3.compaction_rate_yr5,color='k',ls='--')
# f2_ax8.plot(dfp3.index,dfp3.compaction_rate_yr9,color='k',ls='--')
# f2_ax8.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax8.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax8.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax8.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax8.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

# f2_ax9 = fig2.add_subplot(spec2[4, 0])
# f2_ax9.plot(dfp3.index,dfp3.compaction_rate_yr10,color='k',ls='--')
# f2_ax9.plot(dfp3.index,dfp3.compaction_rate_yr11,color='k',ls='--')
# f2_ax9.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax9.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax9.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax9.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax9.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

# f2_ax10 = fig2.add_subplot(spec2[4, 1])
# f2_ax10.plot(dfp3.index,dfp3.compaction_rate_yr12,color='k',ls='--')
# f2_ax10.plot(dfp3.index,dfp3.compaction_rate_yr1,color='k',ls='--')
# f2_ax10.axvspan(date2num(datetime(2017,12,20)), date2num(datetime(2018,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax10.axvspan(date2num(datetime(2016,12,20)), date2num(datetime(2017,3,20)), label="Summer", color="tomato", alpha=0.3)
# f2_ax10.axvspan(date2num(datetime(2017,6,20)), date2num(datetime(2017,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax10.axvspan(date2num(datetime(2018,6,20)), date2num(datetime(2018,9,20)), label="Winter", color="cornflowerblue", alpha=0.3)
# f2_ax10.set_xlim(date2num(dfp3.index[0]), date2num(dfp3.index[-1]))

# bbox=f2_ax1.get_position()
# offset=0.03
# f2_ax1.set_position([bbox.x0, bbox.y0 + offset, bbox.x1-bbox.x0, bbox.y1 - bbox.y0])

# if plotmodel:
#     for ll,name in enumerate(thenames): #plot model results
#         colo,legname = palette[ll],name
#         if name=='MaxSP':
#             legname = 'This work'

#         f2_ax1.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate106'][idds:idde],label=legname,color=colo)
#         f2_ax3.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate80'][idds:idde],label=legname,color=colo)
#         f2_ax4.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate40'][idds:idde],label=legname,color=colo)
#         f2_ax5.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate30'][idds:idde],label=legname,color=colo)
#         f2_ax6.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate25'][idds:idde],label=legname,color=colo)
#         f2_ax7.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate20'][idds:idde],label=legname,color=colo)
#         f2_ax8.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate15'][idds:idde],label=legname,color=colo)
#         f2_ax9.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate10'][idds:idde],label=legname,color=colo)
#         f2_ax10.plot(d2[fil][name][idds:idde].index,d2[fil][name]['crate5'][idds:idde],label=legname,color=colo)

# f2_ax1.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))
# f2_ax9.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))
# f2_ax10.xaxis.set_major_formatter(mpl.dates.DateFormatter('%-m/%y'))
# f2_ax3.tick_params(labelbottom=False)
# f2_ax4.tick_params(labelbottom=False)
# f2_ax5.tick_params(labelbottom=False)
# f2_ax6.tick_params(labelbottom=False)
# f2_ax7.tick_params(labelbottom=False)
# f2_ax8.tick_params(labelbottom=False)

# f2_ax1.set_title('106 m hole')
# f2_ax3.set_title('80 m hole',fontsize=18)
# f2_ax4.set_title('40 m hole',fontsize=18)
# f2_ax5.set_title('30 m hole',fontsize=18)
# f2_ax6.set_title('25 m hole',fontsize=18)
# f2_ax7.set_title('20 m hole',fontsize=18)
# f2_ax8.set_title('15 m holes',fontsize=18)
# f2_ax9.set_title('10 m holes',fontsize=18)
# f2_ax10.set_title('4 m holes',fontsize=18)

# f2_ax10.set_ylim((0,0.21))
# f2_ax3.tick_params(axis = 'both', which = 'major', labelsize = 14)
# f2_ax4.tick_params(axis = 'both', which = 'major', labelsize = 14)
# f2_ax5.tick_params(axis = 'both', which = 'major', labelsize = 14)
# f2_ax6.tick_params(axis = 'both', which = 'major', labelsize = 14)
# f2_ax7.tick_params(axis = 'both', which = 'major', labelsize = 14)
# f2_ax8.tick_params(axis = 'both', which = 'major', labelsize = 14)
# f2_ax9.tick_params(axis = 'both', which = 'major', labelsize = 14)
# f2_ax10.tick_params(axis = 'both', which = 'major', labelsize = 14)
# # f2_ax10.tick_params(axis = 'both', which = 'minor', labelsize = 16)

# # fig2.text(0.001, 0.5, r'Compaction rate (m a$^{-1}$)', va='center', rotation='vertical',fontsize=20))
# # f2_ax1.set_ylabel('Compaction rate\n(m a$^{-1}$)')
# fig2.text(0.04, 0.5, 'Compaction rate (m a$^{-1}$)', va='center', rotation='vertical',fontsize=20)
# fig2.text(0.5, 0.08, 'Date (month/year)', va='center', ha='center',fontsize=20)

# # fig2.tight_layout()
# if plotmodel:
#     f2_ax1.legend(ncol=2)
#     fig2.savefig('CompRate_panel_model.pdf')
#     fig2.savefig('/Users/maxstev/Documents/Grad_School/Manuscripts/Stevens_SPfirn/texfigures/CompRate_panel_model.pdf')
# else:
#     fig2.savefig('CompRate_panel_dataonly.pdf')
#     fig2.savefig('/Users/maxstev/Documents/Grad_School/Manuscripts/Stevens_SPfirn/texfigures/CompRate_panel_dataonly.pdf')



