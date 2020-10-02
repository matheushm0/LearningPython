import numpy as np


def made_matrix():
    cidades = [[0, 1, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [1, 0, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, 2, 0, 5, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, 5, 0, -1, 6, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [4, -1, 3, -1, 0, -1, -1, -1, -1, 11, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, 6, -1, 0, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, 7, 0, 8, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, 8, 0, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, 9, 0, 10, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, 11, -1, -1, -1, 10, 0, -1, 13, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, 12, -1, -1, -1, -1, -1, 0, -1, 15, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, 14, 13, -1, 0, 16, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, 16, 0, 18, 17, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 18, 0, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 17, -1, 0, 19, -1, 21, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 19, 0, 20, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 20, 0, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 21, -1, -1, 0, 22, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 22, 0, 23],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 23, 0]]

    return cidades


def busca_pos(cidade_atual, cidade_vis, pos):
    pos_aux = pos

    for j in range(len(cidade_atual)):
        if cidade_atual[j] > 0 and visitados(cidade_vis, j):
            pos_aux.insert(0, j)

    return pos_aux


def visitados(vetor_visitados, j):
    for i in range(len(vetor_visitados)):
        if vetor_visitados[i] == j:
            return False

    return True


def destino(cidade_atual, k, x):
    for i in range(len(cidade_atual)):
        if k == x:
            print("Destino Encontrado")
            return True
    return False


def nome(cidade):
    nomes = ["Oradea", "Zerind", "Arad", "Timisoara", "Sibiu", "Lugoj", "Mehadia", "Dobreta", "Caraiova", "Rimnieu",
             "Fagaras", "Pitesti", "Bucareste", "Giurgiu", "Urziceni", "Hirsova", "Eforie", "Vaslui", "Iasi", "Neant"]

    for i in range(len(nomes)):
        if cidade == nomes[i]:
            return i


def trad(cidades):
    nomes = ["Oradea", "Zerind", "Arad", "Timisoara", "Sibiu", "Lugoj", "Mehadia", "Dobreta", "Caraiova", "Rimnieu",
             "Fagaras", "Pitesti", "Bucareste", "Giurgiu", "Urziceni", "Hirsova", "Eforie", "Vaslui", "Iasi", "Neant"]

    vetor_cidade = np.array(nomes)[cidades]
    return vetor_cidade


def verifica_vizinho(cidade1, cidade2, cidade):
    if cidade[cidade1][cidade2] > 0:
        return True
    else:
        return False


def way(caminho, cidade, k):
    aux = caminho.copy()
    for i in range(len(aux) - 1):
        if caminho[i] == k:
            break
        if verifica_vizinho(caminho[i], caminho[i+1], cidade) == False:
            j = i + 1
            while(verifica_vizinho(caminho[i], caminho[j], cidade) == False):
                caminho.pop(j)

    return caminho




if __name__ == '__main__':
    cidade = np.array(made_matrix())
    pos = []
    pos_trad = []
    cidade_atual = []
    cidade_vis = []
    cidade_aux = cidade
    caminho = []
    #local_atual = (input("Qual a cidade atual :"))
    #destino_local = (input("Qual a cidade de destino desejada :"))
    #local_atual = nome(local_atual)
    #destino_local = nome(destino_local)
    local_atual = 0
    destino_local = 2
    local_atual_aux = local_atual
    trail = [local_atual]

    while (1):
        cidade_atual = cidade_aux[local_atual]
        pos = busca_pos(cidade_atual, cidade_vis, pos)
        local_atual = np.array(pos[0])

        cidade_vis.append(local_atual)
        trail.append(pos.pop(0))

        if destino(cidade_atual, local_atual, destino_local):
            break

    trail.reverse()

    trail = way(trail, cidade, local_atual_aux)
    print(trad(trail))
