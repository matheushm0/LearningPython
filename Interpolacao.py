import numpy as np
import math
from matplotlib import pyplot as plt

Xvet = np.array([8,12], dtype=np.float)
Fvet = np.array([ 0.9030900,1.0791812], dtype=np.float)

def polinom(coefs,x):
    resultado = 0
    for i in range(0,len(coefs)):
        resultado = resultado + coefs[i]*math.pow(x,i)

    return resultado

def Interpol(xs, fs):
    M = np.zeros((len(xs),len(xs)), dtype=np.float)
    Y = fs.copy()

    for j in range(0,len(xs)):
        for i in range(0,len(xs)):
            M[i][j] = math.pow(xs[i],j)

    coefs = ElimGauss(M,Y)
    return coefs

def ElimGauss(matriz, coef):
    A = matriz.copy()
    b = coef.copy()

    for i in range(0, len(coef)):
        for j in range(0, len(coef)):
            if ( i != j) :
                fator = A[j][i]/A[i][i]
                b[j] = b[j] -fator*b[i]
                for k in range(0,len(coef)):
                    A[j][k] = A[j][k] - fator*A[i][k]

    for i in range(0,len(coef)):
        b[i] = b[i] / A[i][i]
        A[i][i] = 1

    return b

coefs = Interpol( Xvet, Fvet)
#print(coefs)
x = 10
y = polinom(coefs,x)
print("O valor do polinômio interpolador no ponto "+str(x)+" eh "+str(y))
erro = abs( math.log( x, 10) - y  )/abs(math.log( x, 10) )
print("O erro relativo eh "+str(erro*100)+"%")