import re
import sys
import csv
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

v_ecut=[]
v_nkpts=[]
v_alat=[]
v_ene=[]
v_tf=[]
v_rt=[]

from itertools import islice
with open('Fe_hcp_alat2_res173.csv', 'r') as res1:
    for line in islice(res1, 0, None):
        data1=csv.reader(res1, delimiter=',')
        for row in data1:
             v_ecut.append(float(row[0]))
             v_nkpts.append(float(row[1]))
             v_alat.append(float(row[2]))
             v_ene.append(float(row[3]))
             v_tf.append(float(row[4]))
         #   v_rt.append(float(row[5]))
res1.close()

vv_ecut=[]
vv_nkpts=[]
vv_alat=[]
vv_ene=[]
vv_tf=[]
vv_rt=[]

from itertools import islice
with open('Fe_bcc_alat1_res.csv','r') as res2:
    for line in islice(res2,0,None):
        data2=csv.reader(res2,delimiter=',')
        for row in data2:
             vv_ecut.append(float(row[0]))
             vv_nkpts.append(float(row[1]))
             vv_alat.append(float(row[2]))
             vv_ene.append(float(row[3]))
             vv_tf.append(float(row[4]))
        #    vv_rt.append(float(row[5]))
res2.close()

x=np.array(v_alat)
xx=np.array(vv_alat)
y1=np.array(v_ene)*13.605698*(1.6*10**(-19))
y2=np.array(vv_ene)*13.605698*(1.6*10**(-19))

X_val=np.arange(np.amin(x),np.amax(x),0.0001)
XX_val=np.arange(np.amin(xx),np.amax(xx),0.0001)
X_val=(X_val*0.529177208*10**(-10))**3*1.73*0.8660254038 
XX_val=(XX_val*0.529177208*10**(-10))**3
x=(x*0.529177208*10**(-10))**3*1.73*0.8660254038
xx=(xx*0.529177208*10**(-10))**3

p_val=np.polyfit(x,y1,5)
pp_val=np.polyfit(xx,y2,5)
Y_val=np.polyval(p_val,X_val)
YY_val=np.polyval(pp_val,XX_val)

plt.plot(X_val,Y_val,label='Fitting curve',color='blue',linewidth=1.5)
plt.plot(x,y1,'or',label='Raw data',linewidth=1.5,markersize=3)
plt.grid(color='b',lw=0.75)
plt.legend(loc='best')
plt.title('HCP volume vs. energy (1.73)')
plt.xlabel('Cell volume (m^3)')
plt.ylabel('Absolue energy (Joule/cell)')
plt.savefig('myfig1')
plt.clf()

plt.plot(XX_val,YY_val,label='Fitting curve',color='blue',linewidth=1.5)
plt.plot(xx,y2,'or',label='Raw data',linewidth=1.5,markersize=3)
plt.grid(color='b',lw=0.75)
plt.legend(loc='best')
plt.title('BCC volume vs. energy')
plt.xlabel('Cell volume (m^3)')
plt.ylabel('Absolue energy (Joule/cell)')
plt.savefig('myfig2')
plt.clf()

max_index=np.where(Y_val==np.amin(Y_val))
print('HCP')
print(X_val[max_index])
max_index=np.where(YY_val==np.amin(YY_val))
print('BCC')
print(XX_val[max_index])

p_hcp=-(p_val[0]*5*X_val**4+p_val[1]*4*X_val**3+p_val[2]*3*X_val**2+p_val[3]*2*X_val+p_val[4])
p_bcc=-(pp_val[0]*5*XX_val**4+pp_val[1]*4*XX_val**3+pp_val[2]*3*XX_val**2+pp_val[3]*2*XX_val+pp_val[4])

plt.plot(XX_val,p_bcc,label='BCC Fe',color='blue',linewidth=1.5)
plt.plot(X_val,p_hcp,label='HCP 1.73 Fe',color='Green',linewidth=1.5)
plt.grid(color='b',lw=0.75)
plt.legend(loc='best')
plt.title('Cell volume vs. pressure')
plt.xlabel('Cell volume (m^3)')
plt.ylabel('Pressure (Pa/cell)')
plt.savefig('myfig3')
plt.clf()

plt.plot(p_bcc,YY_val,label='BCC Fe',color='blue',linewidth=1.5)
plt.plot(p_hcp,Y_val/2,label='HCP 1.73 Fe',color='Green',linewidth=1.5)
plt.grid(color='b',lw=0.75)
plt.legend(loc='best')
plt.title('Pressure vs. energy')
plt.ylabel('Absolute energy (Joule/atom)')
plt.xlabel('Pressure (Pa/cell)')
plt.savefig('myfig4')
plt.clf()


'''
# make changes here
# Force 1 Ry/Bohr = 25.711043 eV/Angstrom
# Energy 1 Ry = 13.605698 eV

yy=np.array(v_ene)/2*13.605698*1000
xx=np.array(v_alat)*0.529177208
# time=np.array(v_rt)

plt.plot(xx,yy,marker='o',color='purple',linewidth=1.5,markersize=5)
plt.grid(color='b',lw=0.75)
plt.title('Lattice parameter vs. energy (c/a=1.72)')
plt.xlabel('Lattice parameter (Angstrom)')
plt.ylabel('Absolute energy (meV/atom)')
plt.savefig('myfig1')
plt.clf()


plt.plot(xx,time,marker='o',color='blue',linewidth=1.5,markersize=5)
plt.grid(color='b',lw=0.75)
plt.title('Cutoff vs. run time')
plt.xlabel('Cutoff energy (eV)')
plt.ylabel('Run time (min)')
plt.savefig('myfig2')
plt.clf()


length=len(yy)
diff=yy[1:length:1]-yy[0:(length-1):1]
plt.plot(xx[1:length:1],diff,marker='o',color='green',linewidth=1.5,markersize=5)
plt.grid(color='b',lw=0.75)
plt.title('Convergence (c/a=1.74)')
plt.xlabel('K-points')
plt.ylabel('Absolute energy difference (meV/atom)')
plt.savefig('myfig3')
plt.clf()
'''
