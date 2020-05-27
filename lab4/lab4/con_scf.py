import os
import shutil
import numpy as np

# Load the Si.pw.in.template file as a template.
with open("Al.100.surf.template") as f:
    template = f.read()

# Set default values for various parameters
#k = 16 # k-point grid of 16x16x16
#alat = 7.595 # The lattice parameter for the cell in Bohr.
#ecut = 80
i=1

# Loop through different k-points.
for i in np.arange(1, 2, 1):
    # This generates a string from the template with the parameters replaced
    # by the specified values.
    # s = template.format(k=k, alat=alat, ecut=ecut)

    # Let's define an easy jobname.
    jobname = "Al_100_bulk_%s" % (i)

    # Write the actual input file for PWSCF.
    with open("%s.pw.in" % jobname, "w") as f:
        f.write(template)

    #Print some status messages.
    # print("Running with alat = %s..." % (alat))
    # Run PWSCF. Modify the pw.x command accordingly if needed.
    os.system("pw.x -inp {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

    print("Done. Output file is %s.out." % jobname)

# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
shutil.rmtree("tmp")
