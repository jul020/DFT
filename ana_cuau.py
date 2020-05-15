#!/usr/bin/env python
import os
import re
import sys
import csv
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

v_nkpts=[]
v_alat=[]
v_ene=[]
v_tf=[]


# This defines the patterns for extracting relevant data from the output
# files.
patterns = {
    "energy": re.compile(r"total energy\s+=\s+([\d\.\-]+)\sRy"),
  # "ecut": re.compile(r"kinetic\-energy cutoff\s+=\s+([\d\.\-]+)\s+Ry"),
    "alat": re.compile(r"celldm\(1\)=\s+([\d\.]+)\s"),
    "nkpts": re.compile(r"number of k points=\s+([\d]+)"),
    "total_force": re.compile(r"Total force =\s+([\d\.]+)")
}


def get_results(filename):
    data = {}
    with open(filename) as f:
        for l in f:
            for k, p in patterns.items():
                m = p.search(l)
                if m:
                    
                    data[k] = float(m.group(1))
                    continue
    return data


def analyze(filenames):
    fieldnames = ['nkpts', 'alat', 'energy','total_force']
    os.system("rm cuau_k.csv")
    with open('cuau_k.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for f in filenames:
            r = get_results(f)
            writer.writerow(r)
    print("Results written to res.csv!")


if __name__ == "__main__":
     parser = argparse.ArgumentParser(
          description='''Tool for analysis of PWSCF calculations.''')
     parser.add_argument(
          'filenames', metavar='filenames', type=str, nargs="+",
          help='Files to process. You may use wildcards, e.g., "python analyze.py *.out".')
     args = parser.parse_args()
     analyze(args.filenames)

 
from itertools import islice
with open('cuau_k.csv', 'r') as res1:
    for line in islice(res1, 0, None):
        data1=csv.reader(res1, delimiter=',')
        for row in data1:
             v_nkpts.append(float(row[0]))
             v_alat.append(float(row[1]))
             v_ene.append(float(row[2]))
             v_tf.append(float(row[3]))
            # v_ti_dy.append(float(row[5]))
res1.close()

# make changes here
# Force 1 Ry/Bohr = 25.711043 eV/Angstrom
# Energy 1 Ry = 13.605698 eV

yy=np.array(v_ene)*13.605698*1000
xx=np.array(v_nkpts)
# 0.529177208
# time=np.array(v_rt)

#ind=np.where(yy==np.amin(yy))
#print(xx[ind])

plt.plot(xx,yy,marker='o',color='purple',linewidth=1.5,markersize=5)
plt.grid(color='b',lw=0.75)
plt.title('Y axis displacement vs. energy')
plt.xlabel('Coordination displacement (a.u.)')
plt.ylabel('Absolute energy (meV/cell)')
plt.savefig('myfig2')
plt.clf()
'''

plt.plot(xx,time,marker='o',color='blue',linewidth=1.5,markersize=5)
plt.grid(color='b',lw=0.75)
plt.title('Cutoff vs. run time')
plt.xlabel('Cutoff energy (eV)')
plt.ylabel('Run time (min)')
plt.savefig('myfig2')
plt.clf()
'''
length=len(yy)
diff=yy[1:length:1]-yy[0:(length-1):1]
plt.plot(xx[1:length:1],diff,marker='o',color='green',linewidth=1.5,markersize=5)
plt.grid(color='b',lw=0.75)
plt.title('Convergence (CuAu)')
plt.xlabel('K-points')
plt.ylabel('Absolute energy difference (meV/cell)')
plt.savefig('myfig3')
plt.clf()


os.system("sudo fbi myfig2.png")
