import numpy as np

def decompoeLU(A, verbose = True):
    """
    Decomposição LU
    Atenção: sobreescreve a matriz A
    
    Recebe:
        A           => Matriz de coeficientes
        verbose     => Imprime passo à passo?
        
    Retorna:
        Nada, a matriz de entrada é sobreescrita
    """
    
    n = len(A)
    
    if verbose: print(A)
    
    for j in range(n): #coluna
        for i in range(n): #linha
           
            # Parte L da matriz
            if i>=j:
                s = 0
                for k in range(0, j):
                    s += A[i][k] * A[k][j]
                A[i][j] -= s
            
            #parte U da matriz
            else:
                s = 0
                for k in range(0, i):
                    s += A[i][k] * A[k][j]
                
                A[i][j] = (A[i][j] - s)/float(A[i][i])
    
    if verbose: print(A)
    


def resolveLU(LU, B, verbose=True):
    """
    Resolve um sistema já decomposto em LU
    Atenção: Sobreescreve a matriz A
    
    Recebe: 
        LU          => Matriz LU decomposta
        B           => Vetor dos termos independentes
        verbose     => Imprime passo à passo?
        
    Retorna:
        x           => Vetor solução
    """
    
    n = len(LU)
    assert len(B) == n, "Matriz de tamanhos diferentes"
    
    #Resolve Ly = b
    y = np.zeros(n, dtype=float)
    for i in range(n):
        s = 0
        for j in range(0, i):
            s += LU[i][j]*y[j]
        y[i] = (B[i] - s)/float(LU[i][i])
        
    if verbose: print("y = ", y)   
    
    #Resolve Ux = y
    x = np.zeros(n, dtype=float)
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i+1, n):
            s += LU[i][j]*x[j]
        x[i] = y[i] - s
        
    return x
    
    
    

def lu(A, B, verbose=True):
    """
    Resolve um sistema pela decoposição LU
    Atenção: Sobreescreve a matriz A
    
    Recebe:
        A           => A matriz de coeficientes
        B           => Vetor dos termos independente
        verbose     => Imprime passo à passo?
        
    Retorna
        x           => Vetor solução
    """
    decompoeLU(A, verbose)
    return resolveLU(A, B, verbose)