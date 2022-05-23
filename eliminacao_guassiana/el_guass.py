# -*- coding: utf-8 -*-
import numpy as np
import sys
import sl


assert len(sys.argv) == 2, "Número errado de argumentos"
ifile = sys.argv[1]

A = np.loadtxt(ifile, dtype=float)
print(A)

print(sl.escalona(A, verbose=True))


