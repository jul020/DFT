import os

#os.system("python3 ./run1.py")
#os.system("python3 ./run2.py")
#os.system("rm -rf tmp")
os.system("mv PTO_alat_7.4_12.out PTO_alat_7.40_12.out")
os.system("mv PTO_alat_7.5_12.out PTO_alat_7.50_12.out")
os.system("mv PTO_alat_7.6_12.out PTO_alat_7.60_12.out")
os.system("python3 ./run3.py PTO_alat_*.out")
#os.system("python3 ./run5.py")
