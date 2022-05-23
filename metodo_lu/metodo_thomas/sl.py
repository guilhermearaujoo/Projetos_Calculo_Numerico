import numpy as np


def thomas(A, verbose=True):
    """
    Função que aplica o metodo de thomas para matrizes tridiagonais
    
    Recebe:
        A           => Matriz tridiagonal
        verbose     => Deseja ver passo à passo?
        
    Retorna:
        x           => Vetor solução
    """
    
    n = len(A)
    
    a = np.zeros(n)    
    b = np.zeros(n)    
    c = np.zeros(n)
    d = np.zeros(n)
    
    b[0] = A[0][0]
    c[0] = A[0][1]
    d[0] = A[0][-1]
    for i in range(1, n-1):
        a[i] = A[i][i-1]
        b[i] = A[i][i]
        c[i] = A[i][i+1]
        d[i] = A[i][-1]
        
    a[-1] = A[-1][-3]
    b[-1] = A[-1][-2]
    d[-1] = A[-1][-1]
    
    
    if verbose: 
        print("Matriz diagonal")
        
    den = float(b[0])
    c[0] /= den
    d[0] /= den
    
    for i in range(1, n):
        den = float(b[i] - a[i]*c[i-1])
        c[i] /= den
        d[i] = (d[i] - a[i]*d[i-1])/ den
        
    if verbose:
        print("Depois do passo regressivo")
        
    x = np.copy(d)
    for i in range(n-2, -1, -1): 
        x[i] -= c[i]*x[i+1]
        
    return x
        