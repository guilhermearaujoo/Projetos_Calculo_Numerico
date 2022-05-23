#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 20:38:06 2022

@author: guilherme
"""

def escalona(A, tol=1.0e-10, verbose=False):
    
    """
    Input:
        A: a amtriz a ser escalonada
        tol: tolerância numérica suportada 
        verbose: se TRUE imprime o passo a passso da função
        
    Return:
        A: a matriz A escalonada
    """
    
    n=len(A)
    
    if verbose: print(A)
        
    
    # escalonamento para cada uma das colunas
    for c in range(n-1):
        
        if verbose:
            print("\n\n--------------------")
            print("Eliminação Gaussiana na coluna %d." % c, end="\n")
        
        
        #Procuro um Pivô 
        p=c
        while abs(A[p,c])<tol and p<n-1:
            p+=1
        if abs(A[p,c])<tol:
            sys.exit("O Pivo é nulo o algoritimo falha\n")
        
        
        # Se for necessário, troca linhas!
        if p==c:
            if verbose:
                print("Pivo A[%d,%d] = %.6g, não preciso trocar as linhas\n"
                      % (p, c, A[p,c]))
            else: 
                # o pivo não está na linha atual faço uma troca de linhas
                if verbose:
                    print("Pivo A[%d,%d] = %.6g, trocando as linhas %d <=> %d\n"
                          % (p, c, A[p,c], p, c))
                x = -A[c].copy()

                A[c] = A[p]
                A[p] = x
            
            # Faz o escalonamento para coluna c
            if verbose: print('')
            for l in range(c+1, n):
                coef = A[l, c]/ A[c,c]
                if verbose: print("E_%d - %.2f E_%d -> E_%d)" % (l, coef, c, l))
                A[l] = A[l] - coef*A[c] 
            if verbose: print(A, "\n\n")
            
    return A 
    


def subs_regressiva(A, verbose=False):
    
    n=len(A)
            
    #Não posso inicar a substituição regressiva
    if A[n-1, n-1] == 0:
        sys.exit("A[%d, %d] = 0, Não existe solução única" % (n-1, n-1))
      
        
    #Substituição Regressiva
    
    if verbose:
        print("\n\n--------------------")
        print("Substituicão Regressiva\n")
        
    x = [0]*n
    x[n-1] = A[n-1, n]/A[n-1, n-1]
    
    if verbose:
        print("x_%d = %.6g / %.6g = %.6g" % (n-1, A[n-1, n], A[n-1, n-1], x[n-1]))
    
    
    for i in range(n-2, -1, -1):
        s = 0
        strsoma = ""
        if verbose: print("x_%d = " % (i), end ='')
        for j in range(i+1, n):
            s+= A[i,j]*x[j]
            if verbose: strsoma += "%.6g x_%d + " % (A[i,j], j)
        x[i] = (A[i,n] - s)/A[i,i]
        
        if verbose: 
            print("(%.6g - (%s) )/ %.6g = %.6g" % (A[i,n], strsoma, A[i,i], x[i]))
        if verbose: print("{} \n".format(x))
        
    return x
    
    


def subs_progressiva(A, verbose=False):

    n=len(A)

            
    #Não posso inicar a substituição regressiva
    if A[0, 0] == 0:
        sys.exit("A[%d, %d] = 0, Não existe solução única" % (0, 0))
        
    if verbose:
        print("\n\n--------------------")
        print("Substituicão Progressiva\n")
        
        
    x = [0]*n
    x[0] = A[0, n]/A[0, 0]
    
    if verbose:
        print("x_%d = %.6g / %.6g = %.6g" % (0, A[0, n], A[0, 0], x[0]))
        
    for i in range(1, n, 1):
        s = 0
        strsoma = ""
        if verbose: print("x_%d = " % (i), end ='')
        for j in range(i-1, -1, -1):
            s+= A[i,j]*x[j]
            if verbose: strsoma += "%.6g x_%d + " % (A[i,j], j)
        x[i] = (A[i,n] - s)/A[i,i]
        
        if verbose: 
            print("(%.6g - (%s) )/ %.6g = %.6g" % (A[i,n], strsoma, A[i,i], x[i]))
        if verbose: print("{} \n".format(x))
        
    return x
    
    


def eliminacao_guassiana(A, verbose=False):
    """
    Algoritimo de Eliminação Gaussiana
    
    Recebe:
        A       => Matriz aumentada de coeficientes
        verbode => Imprime passo a passo?
        
    Retorna:
        x       => Vetor solução
    """
    size = A.shape
    assert(size[0] < size[1]), "Matriz inválida"
    
    A = escalona(A, True)
    x = subs_regressiva(A, True)
    

    return(x)



def Octave(A, n):
    """
    input: 
        n: número de linhas da matriz A
        A: matriz escalonada
    
    return:
        det: Determinante da matriz A
    """
    
    
    
    
    
    
    
    
    
    
    
    