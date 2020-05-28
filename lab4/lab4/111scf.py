import os
import shutil
import numpy as np

# Load the Si.pw.in.template file as a template.
with open("Al.111.bulk.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k1 = 16 # k-point grid of 16x16x16
k3 = 7
alat = 7.605 # The lattice parameter for the cell in Bohr.
ecut = 60

# Loop through different k-points.
for ecut in np.arange(60, 70, 10):
    # This generates a string from the template with the parameters replaced
    # by the specified values.
    s = template.format(k1=k1, k3=k3, alat=alat, ecut=ecut)

    # Let's define an easy jobname.
    jobname = "Al_111_bulk_%s" % (ecut)

    # Write the actual input file for PWSCF.
    with open("%s.pw.in" % jobname, "w") as f:
        f.write(s)

    #Print some status messages.
    # print("Running with ecut = %s..." % (ecut))
    # Run PWSCF. Modify the pw.x command accordingly if needed.
    os.system("pw.x -inp {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

    print("Done. Output file is %s.out." % jobname)

# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
shutil.rmtree("tmp")
