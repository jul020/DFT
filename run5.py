#!/usr/bin/env python

"""
This is a very simple python starter script to automate a series of PWSCF
calculations. If you don't know Python, get a quick primer from the official
Python documentation at https://docs.python.org/2.7/. The script is deliberately
simple so that only basic Python syntax is used and you can get comfortable with
making changes and writing programs.

Author: Shyue Ping Ong
"""

import os
import shutil

# Load the Si.pw.in.template file as a template.
with open("Fe.bcc.nospin.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k = 18 # k-point grid of 8x8x8
alat = 500 # The lattice parameter for the cell in Bohr.
#calat = 172 # The c/a ratio

#for calat in range(173,175,1):
#calat=calat/100
for alat in range(500,518,1):
       # This generates a string from the template with the parameters replaced
       # by the specified values.

       alat=alat/100

       #s = template.format(alat=alat, calat=calat, k=k)
       s = template.format(alat=alat, k=k)

       # Let's define an easy jobname.
       # jobname = "Fe_hcp_%s_%s_%s" % (alat, calat, k)
       jobname = "Fe_bcc_nospin_%s_%s" % (alat, k)

       # Write the actual input file for PWSCF.
       with open("%s.pw.in" % jobname, "w") as f:
           f.write(s)

       #Print some status messages.
       #print("Running with alat = %s, calat = %s, k = %s..." % (alat, calat, k))
       print("Running with alat = %s, k = %s..." % (alat, k))

       # Run PWSCF. Modify the pw.x command accordingly if needed.
       os.system("pw.x -inp {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

       print("Done. Output file is %s.out." % jobname)

# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
shutil.rmtree("tmp")
