import os
import shutil

# Load the Si.pw.in.template file as a template.
with open("PbTiO3.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k = 6
alat = 7.5 # The lattice parameter for the cell in Bohr.
tx=0.5
ty=0.5
tz=0.5

#for calat in range(173,175,1):
#calat=calat/100
for k in range(6,18,2):
       # This generates a string from the template with the parameters replaced
       # by the specified values.

       # alat=alat/100
       # ty=ty/1000

       #s = template.format(alat=alat, calat=calat, k=k)
       s = template.format(alat=alat, k=k, tx=tx, ty=ty, tz=tz)

       # Let's define an easy jobname
       jobname = "PTO_k_%s_%s" % (alat, k)

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
