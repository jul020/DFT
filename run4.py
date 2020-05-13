import shutil
import os
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

# This defines the patterns for extracting relevant data from the output
# files.
patterns = {
    "energy": re.compile(r"total energy\s+=\s+([\d\.\-]+)\sRy"),
    "ecut": re.compile(r"kinetic\-energy cutoff\s+=\s+([\d\.\-]+)\s+Ry"),
    "alat": re.compile(r"celldm\(1\)=\s+([\d\.]+)\s"),
    "nkpts": re.compile(r"number of k points=\s+([\d]+)"),
    "total_force": re.compile(r"Total force =\s+([\d\.]+)"),
    "run_time": re.compile(r"PWSCF\s+:\s+([\d\.]*)minutes\sCPU")
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
    fieldnames = ['ecut', 'nkpts', 'alat', 'energy','total_force','run_time']
    with open('PTO_alat2.csv', 'w') as csvfile:
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
with open('PTO_alat2.csv', 'r') as res1:
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

# make changes here
# Force 1 Ry/Bohr = 25.711043 eV/Angstrom
# Energy 1 Ry = 13.605698 eV

yy=np.array(v_ene)*13.605698*1000
xx=np.array(v_alat)*0.529177208
# time=np.array(v_rt)

ind=np.where(yy==np.amin(yy))
best_a=xx[ind]

plt.plot(xx,yy,marker='o',color='purple',linewidth=1.5,markersize=5)
plt.grid(color='b',lw=0.75)
plt.title('Lattice vs. energy (k=16)')
plt.xlabel('Lattice parameter (Angstrom)')
plt.ylabel('Absolute energy (meV/cell)')
plt.savefig('myfig_alat')
plt.clf()

with open("PbTiO3.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k = 16
alat = best_a/0.529177208 # The lattice parameter for the cell in Bohr.
tx=0.5
ty=485
tz=0.5

for ty in range(485,516,1):
       # This generates a string from the template with the parameters replaced
       # by the specified values.

       ty=ty/1000

       #s = template.format(alat=alat, calat=calat, k=k)
       s = template.format(alat=alat, k=k, tx=tx, ty=ty, tz=tz)

       # Let's define an easy jobname
       jobname = "PTO_dis_%s_%s" % (alat, k)

       # Write the actual input file for PWSCF.
       with open("%s.pw.in" % jobname, "w") as f:
           f.write(s)

       #Print some status messages.
       print("Running with alat = %s, k = %s..." % (alat, k))

       # Run PWSCF. Modify the pw.x command accordingly if needed.
       os.system("pw.x -inp {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

       print("Done. Output file is %s.out." % jobname)

# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
shutil.rmtree("tmp")
