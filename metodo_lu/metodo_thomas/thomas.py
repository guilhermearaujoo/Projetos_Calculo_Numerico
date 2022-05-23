import sys
import numpy as np
import sl

assert len(sys.argv) == 2
ifile = sys.argv[1]

A = np.loadtxt(ifile, dtype=float)

print(sl.thomas(A, True))