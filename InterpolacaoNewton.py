import numpy as np

def  polinom(dif, xs,x):
    resultado = dif[0]
    erro = dif[len(dif)-1]*( x-xs[0] )

    for i in range(1, len(xs)):
        prod = 1
        erro = erro * ( x - xs[i] )
        for j in range(0,i):
            prod = prod*( x-xs[j] )
        resultado = resultado + dif[i]*prod

    #print("O erro associado a interpolação eh "+str(abs(erro)))
    return resultado

#criar a matriz dos operadores diferença de Newton
def differ(Fvet, xs):
    num = np.zeros((len(Fvet),len(Fvet)), dtype=np.float )
    #preencher coluna da matriz com os f(x) conhecidos
    for i in range(0,len(Fvet)):
        num[i][0] = Fvet[i]

    #calcular o restante dos operadores diferenca
    for i in range(1, len(Fvet)):
        for j in range(0, len(Fvet) - i):
                num[j][i] = ( num[j+1][i-1] - num[j][i-1] ) / ( xs[i+j] - xs[j] )

    return num[0]

Fvet = [3,6,19,99,291]
xs = [1,2,3,5,7]

operadores = differ(Fvet,xs)
k = polinom(operadores, xs, 4)
print("O valor do polin. interpolador de Newton no ponto "+str(4)+" eh "+str( k ))