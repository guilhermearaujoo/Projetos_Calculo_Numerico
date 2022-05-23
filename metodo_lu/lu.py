import sys 
import numpy as np
import sl

assert len(sys.argv) == 2, "Número errado de parametros"
ifile = sys.argv[1]

Aumentada = np.loadtxt( sys.argv[1], dtype=float)
n = len(Aumentada)

#posso colocar um for aqui para copiar essas matrizes
B = Aumentada.transpose()[-1]
A = Aumentada.transpose()[:-1].transpose() #as primeiras linhas menos a ultima

print(Aumentada)
print("- - - - - - - -")
print(A)
print(B)

x = sl.lu(A, B, True)
print(x)

### interessante usar lu quando tenho, varios b e uma matriz A fixa.
### deocompõe uma vez e faz substituicao para b varias outras vezes

### problema quando a o pivo é zero