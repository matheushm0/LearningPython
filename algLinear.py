from sympy import *

init_printing(use_latex='mathjax')
x=symbols('x')
y=symbols('y')
la=symbols('lambda')
f, g, p = symbols('f, g, p', cls=Function)

def poli_carac(m):
    m_i = eye( sqrt( len(m)) )*(-la) #matriz identidade vs -lambda
    poli_c = factor( det( m + m_i ) ) #polinômio característico fatorado
    return poli_c

def poli_possi(m):
    poli_c = poli_carac(m)
    a=factor_list(poli_c) #separando os fatores e expoentes em tuplas
    fixo = len(a)-1
    expoentes = []
    fatores = []
    possi = []
    #separando expoentes de fatores
    for i in range(1, len(a[fixo])+1, +1):
        exp = a[fixo] [len( a[fixo])-i] [len(a[fixo][len( a[fixo])-1])-1]
        ft = a[fixo] [len( a[fixo])-i] [len(a[fixo][len( a[fixo])-2])-2]
        expoentes.append(exp)
        fatores.append(ft)
    #fazendo todas as possibilidades para expoente de cada fator
    for i in range( 0, len(fatores), +1):
        lista_aux = []
        for j in range( 1, expoentes[i]+1, +1):
            pt1 = ( (fatores[i]-la) * eye( degree(poli_c) ) + ( fatores[i] + solve(fatores[i])[0]).subs(la,m) )**j
            lista_aux.append( (pt1, fatores[i]**j) )
        possi.append(lista_aux)
    return possi
    
#recebe a lista de todas as possibilidades, vindo da
#função poli_possi e multiplica todos, a fim de saber
#se alguma das multiplicações entre as matrizes dá a nula
def teste(a):
    lista =[]
    if len(a) == 1:
        return a
    else:
        for i in a[0]:
            for j in a[1]:
                aux = (i[0]*j[0], i[1]*j[1])
                lista.append(aux)
        a.remove(a[0])
        a.remove(a[0])
        a.append(lista)
        if len(a) > 1:
            return teste(a)
        return a
    
def minimal(m):
    poli_c = poli_carac(m)
    poli_p = poli_possi(m)
    lista = teste(poli_p)
    for i in lista[0]:
        if i[0] == zeros(degree(poli_c)):
            return i[1] * factor_list(poli_c)[0]
    return -1
                 
def eh_diag(m):
    poli_min = minimal(m)
    poli_c = poli_carac(m)
    lista_exp=[]
    
    #vendo se algum fator do polinômio min tem expoente diferente de 1
    #se tiver, não é diagonalizável
    for i in factor_list(poli_min)[1]:
        if i[1]!=1: return -1
    #verifica se os autovalores do poli min são diferentes dos
    #autovalores do poli carac
    if solve(poli_c) != solve(poli_min):
        return -1
        
    #se todos tiverem expoente 1
    #percorre a lista de fatores do poli carac
    for i in factor_list(poli_c)[1]:
        aux = solve(i[0])
        #adiciona os autovalores n vezes, sendo n o expoente referente ao fator cujo ele é raiz
        for j in range(i[1]):
            lista_exp.append(aux[0])
            
    #depois de captar tds os autovalores
    #faz a matriz diagonalizada
    m_d = eye(degree(poli_c))
    l_aux=[]
    for i in range(len(lista_exp)):
        l_aux.append(m_d.row(i)*lista_exp[i])
    return Matrix(l_aux)    
            
m = Matrix( [ [1,1],[0,1] ] ) #matriz principal
m2 = Matrix( [ [3,0,-4,1],[0,3,5,0],[0,0,-1,2],[0,0,0,1] ] ) #matriz principal
m3 = Matrix( [ [2,2,-5],[3,7,-15],[1,2,-4] ] ) #matriz principal