import os

nslab=2
nvac=1

for nvac in range(1,4,1):
     os.system("python3 fcc_surf_gen.py --a 7.605 --miller "100" --k 16 --nslab %s --nvac %s --outfile Al.100.surf.%s.%s.template" % (nslab, nvac, nslab, nvac))
