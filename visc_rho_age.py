import numpy as np
import pandas as pd
import scipy as sp

### top and bottom depths of virtual holes
htda = [0.25,0.25,4.40,4.42,4.40,4.42,9.750,9.650,9.75,9.65,14.65,15.10,19.53,24.85,29.82,40.16,80.0]
hbda = [4.40,4.42,9.75,9.75,9.65,9.65,14.65,14.65,15.1,15.1,19.53,19.53,24.85,29.82,40.16,80.00,106.0]

rho126=np.genfromtxt('/Users/maxstev/Documents/Grad_School/Research/SouthPole/DATA/SPdensity_126.csv',delimiter=',',skip_header=1)
dep126=rho126[:,0]
den126=rho126[:,1]
rho106=np.genfromtxt('/Users/maxstev/Documents/Grad_School/Research/SouthPole/DATA/SPdensity_106.csv',delimiter=',',skip_header=1)
dep106=rho106[:,0]
den106=rho106[:,1]*1000
rhopit=np.genfromtxt('/Users/maxstev/Documents/Grad_School/Research/SouthPole/DATA/SPdensity_pit.csv',delimiter=',',skip_header=1)
deppit=rhopit[:,0]
denpit=rhopit[:,1]
rhonic=np.genfromtxt('/Users/maxstev/Documents/Grad_School/Research/SouthPole/DATA/SPdensity_nicl.csv',delimiter=',',skip_header=1)
depnic=rhonic[:,0]
dennic=rhonic[:,1]

dennic = np.append(290,dennic)
depnic = np.append(0,depnic)

densmooth = dennic.copy()
densmooth106 = den106.copy()
N=7
idr = int(np.floor(N/2))
densmooth[idr:-idr] = np.convolve(dennic,np.ones((N,))/N, mode='valid')
densmooth106[idr:-idr] = np.convolve(den106,np.ones((N,))/N, mode='valid')

pitsmooth=denpit.copy()
n2=7
idr2 = int(np.floor(n2/2))
pitsmooth[idr2:-idr2]=np.convolve(denpit,np.ones((n2,))/n2,mode='valid')
pitsmooth[deppit<0.2] = np.mean(pitsmooth[deppit<0.2])
# pitsmooth[0:idr2] = np.mean(pitsmooth[0:idr2])
pitsmooth[-idr2:] = np.mean(pitsmooth[-idr2:])

dep_int=np.arange(0,108.1,0.1)
rho_int = np.interp(dep_int,depnic,densmooth)
rho106_int = np.interp(dep_int,dep106,densmooth106)
rho_int_df = pd.DataFrame({'dep_int':dep_int,'rho_int':rho_int})


usp50_ts = pd.read_csv('/Users/maxstev/Documents/Grad_School/Research/SouthPole/USP50_Timescale_zero.csv')
usp50_ts['tau']=usp50_ts.BP-usp50_ts.BP[0]

USPintfun = sp.interpolate.interp1d(depnic,densmooth,fill_value='extrapolate')
usp50_ts['density'] = USPintfun(usp50_ts.Depth)
usp50_ts['mass'] = usp50_ts.Thickness*usp50_ts.density
usp50_ts['bdot_ie'] = usp50_ts.mass/917.0

usp50bdot1 = usp50_ts[['Year','bdot_ie']]
usp50bdot1.set_index('Year',inplace=True)
usp50bdot = usp50bdot1.reindex(index=usp50bdot1.index[::-1])

bdot_extend = np.concatenate((usp50bdot.to_numpy().T[0][:-1],np.array([0.1189,0.100,0.1093])))

bdot_long=np.tile(bdot_extend,(1,12)).flatten()

age_int = np.interp(dep_int,usp50_ts['Depth'].values,usp50_ts['tau'].values)
rho_int_df['age'] = age_int
rho_int_df['mass'] = rho_int_df['rho_int']*0.1

usp50_ts['bdot_mean'] = usp50_ts['bdot_ie'].cumsum()/usp50_ts['tau']
usp50_ts.loc[0,'bdot_mean'] = 0.075

def maxage(top,bot):
    return rho_int_df[((rho_int_df['dep_int']>top)&(rho_int_df['dep_int']<bot))]['age'].max()
#     return usp50_ts[(usp50_ts.Depth>=top) & (usp50_ts.Depth<=bot)].tau.max()
def meanage(top,bot):
    inds = ((rho_int_df['dep_int']>top)&(rho_int_df['dep_int']<bot))
#     return rho_int_df[((rho_int_df['dep_int']>top)&(rho_int_df['dep_int']<bot))]['age'].mean()
    return np.sum(rho_int_df[inds]['age']*rho_int_df[inds]['mass'])/np.sum(rho_int_df[inds]['mass'])
#     return usp50_ts[(usp50_ts.Depth>=top) & (usp50_ts.Depth<=bot)].tau.mean()

def maxrho(top,bot):
    return rho_int_df[((rho_int_df['dep_int']>top)&(rho_int_df['dep_int']<bot))]['rho_int'].max()
#     return usp50_ts[(usp50_ts.Depth>=top) & (usp50_ts.Depth<=bot)].tau.max()
def meanrho(top,bot):
    return rho_int_df[((rho_int_df['dep_int']>top)&(rho_int_df['dep_int']<bot))]['rho_int'].mean()
#     return usp50_ts[(usp50_ts.Depth>=top) & (usp50_ts.Depth<=bot)].tau.mean()

rmeanlist = []
rmaxlist = []
ameanlist = []
amaxlist = []
for hh in range(len(htda)):
    rmean = meanrho(htda[hh],hbda[hh])
    rmax = maxrho(htda[hh],hbda[hh])
    amean = meanage(htda[hh],hbda[hh])
    amax = maxage(htda[hh],hbda[hh])
    rmeanlist.append(rmean)
    rmaxlist.append(rmax)
    ameanlist.append(amean)
    amaxlist.append(amax)