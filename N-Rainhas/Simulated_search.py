import numpy as np
import math

def visita_vetor(vetor_visitados, estado_visitado):
    for i in vetor_visitados:
        if estado_visitado == i:
            return False
    return True

def set_estado_inicial(high, weigth):
    estado = []
    for i in range(high):
        estado.append(np.random.randint(weigth))
    return estado

def count_heuristica(estado):
    count_h = 0
    for i in range(len(estado) - 1):
        for j in range(i + 1, len(estado)):
            if estado[i] + i == estado[j] + j:
                count_h = count_h + 1
            if estado[i] - i == estado[j] - j:
                count_h = count_h + 1
            if estado[i] == estado[j]:
                count_h = count_h + 1
    return count_h

if __name__ == '__main__':

    high = 8
    weigth = 8
    estado_inicial = set_estado_inicial(high, weigth)
    print(estado_inicial)
    #estado_inicial = [0, 1, 0, 1]
    estado_atual = estado_inicial
    vetor_visitados = []

    while(count_heuristica(estado_atual) != 0):
        estado_aux = estado_atual

        if visita_vetor(vetor_visitados, estado_aux) == True:
            vetor_visitados.append(estado_aux)
        else:
            estado_aux = set_estado_inicial(high, weigth)

        menor = math.factorial(len(estado_aux))
        for j in range(high):
            for i in range(weigth):
                estado_aux[j] = i
                if menor > count_heuristica(estado_aux):
                    menor = count_heuristica(estado_aux)
                    i_aux = i
                    j_aux = j

            estado_aux[j_aux] = i_aux

        estado_atual = estado_aux
    print("Estado Ideal:\n", estado_atual)
