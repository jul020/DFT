import os
import shutil

# Load the Si.pw.in.template file as a template.
with open("CuAu.l10.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k = 4
alat = 7.48 # The lattice parameter for the cell in Bohr.
calat = 0.927 # c/a ratio

#for calat in range(173,175,1):
#calat=calat/100
for k in range(4,12,1):
       # This generates a string from the template with the parameters replaced
       # by the specified values.


       #s = template.format(alat=alat, calat=calat, k=k)
       s = template.format(alat=alat, k=k, calat=calat)

       # Let's define an easy jobname
       jobname = "cuau_%s_%s_%s" % (alat, calat, k)

       # Write the actual input file for PWSCF.
       with open("%s.pw.in" % jobname, "w") as f:
           f.write(s)

       #Print some status messages.
       print("Running with alat = %s, calat = %s, k = %s..." % (alat, calat, k))

       # Run PWSCF. Modify the pw.x command accordingly if needed.
       os.system("pw.x -inp {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

       print("Done. Output file is %s.out." % jobname)

# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
shutil.rmtree("tmp")
