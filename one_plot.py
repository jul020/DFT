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
with open('Fe_hcp_alat2_res172.csv', 'r') as res1:
    for line in islice(res1, 0, None):
        data1=csv.reader(res1, delimiter=',')
        for row in data1:
             v_ecut.append(float(row[0]))
             v_nkpts.append(float(row[1]))
             v_alat.append(float(row[2]))
             v_ene.append(float(row[3]))
             v_tf.append(float(row[4]))
res1.close()

vv_ecut=[]
vv_nkpts=[]
vv_alat=[]
vv_ene=[]
vv_tf=[]
vv_rt=[]

from itertools import islice
with open('Fe_hcp_alat2_res173.csv','r') as res2:
    for line in islice(res2,0,None):
        data2=csv.reader(res2,delimiter=',')
        for row in data2:
             vv_ecut.append(float(row[0]))
             vv_nkpts.append(float(row[1]))
             vv_alat.append(float(row[2]))
             vv_ene.append(float(row[3]))
             vv_tf.append(float(row[4]))
res2.close()

vvv_ecut=[]
vvv_nkpts=[]
vvv_alat=[]
vvv_ene=[]
vvv_tf=[]
vvv_rt=[]

from itertools import islice
with open('Fe_hcp_alat2_res174.csv', 'r') as res3:
    for line in islice(res3, 0, None):
        data3=csv.reader(res3, delimiter=',')
        for row in data3:
            vvv_ecut.append(float(row[0]))
            vvv_nkpts.append(float(row[1]))
            vvv_alat.append(float(row[2]))
            vvv_ene.append(float(row[3]))
            vvv_tf.append(float(row[4]))
res3.close()

y1=np.array(v_ene)/2*13.605698*1000
y2=np.array(vv_ene)/2*13.605698*1000
y3=np.array(vvv_ene)/2*13.605698*1000
x1=np.array(v_alat)*0.529177208
x2=np.array(vv_alat)*0.529177208
x3=np.array(vvv_alat)*0.529177208

ind1=np.where(y1==np.amin(y1))
ind2=np.where(y2==np.amin(y2))
ind3=np.where(y3==np.amin(y3))

print('c/a=1.72 energy & lattice: ')
print(np.amin(y1))
print(x1[ind1])
print('c/a=1.73 energy & lattice: ')
print(np.amin(y2))
print(x2[ind2])
print('c/a=1.74 energy & lattice: ')
print(np.amin(y3))
print(x3[ind3])

plt.plot(x1,y1,label='c/a 1.72',color='red',linewidth=1.5)
plt.plot(x2,y2,label='c/a 1.73',color='blue',linewidth=1.5)
plt.plot(x3,y3,label='c/a 1.74',color='Green',linewidth=1.5)
plt.grid(color='b',lw=0.75)
plt.legend(loc='best')
plt.title('Lattice parameter vs. energy')
plt.xlabel('Lattice parameter (Angstrom)')
plt.ylabel('Energy (meV/atom)')
plt.savefig('myfig0')
plt.clf()

plt.plot(x1[16:24],y1[16:24],label='c/a 1.72',color='red',linewidth=1.5)
plt.plot(x2[16:24],y2[16:24],label='c/a 1.73',color='blue',linewidth=1.5)
plt.plot(x3[16:24],y3[16:24],label='c/a 1.74',color='Green',linewidth=1.5)
plt.grid(color='b',lw=0.75)
plt.legend(loc='best')
plt.title('Lattice parameter vs. energy')
plt.xlabel('Lattice parameter (Angstrom)')
plt.ylabel('Energy (meV/atom)')
plt.savefig('myfig0')
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
