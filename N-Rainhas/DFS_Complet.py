import numpy as np

# nha = np.array([[2, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 2, 0],
#                 [0, 0, 0, 2, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 2, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 2],
#                 [0, 2, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 2, 0, 0, 0],
#                 [0, 0, 2, 0, 0, 0, 0, 0]])

matrixVistas = [[[]]]


def verIgualdade(matrixSafe, matrixCorretas):
    matrixCorretasS = matrixCorretas.copy()
    matrix = np.copy(matrixSafe)
    #print("B", matrixCorretasS[0])
    #print("A", matrix)
    for i in range(np.size(matrixCorretasS)):
        if np.array_equal(matrixCorretasS[i], matrix):

            #print("False")
            return False
    matrixCorretasS.insert(0, matrix)
    #print("True")
    return True

# def foiVisto(matrixA):
#     matrix = np.copy(matrixA)
#     for i in range(np.size(matrixVistas)):
#         if np.array(matrixVistas[i]).tostring() == matrix.tostring():
#             return True
#
#     return False


def printMatrix(matrix):
    for i in range(np.size(matrix, 0)):
        print(matrix[i])
    print("\n")


def countRainha(matrix):
    return (np.array(matrix).flatten().tolist().count(2))


def marcaLocal(matrixA, i, j):
    matrix = np.copy(matrixA)
    matrix[i, j] = 2

    # Linhas
    iaux = i + 1
    jaux = j
    while iaux < 8:
        matrix[iaux, j] = 0
        iaux = iaux + 1

    iaux = i
    jaux = j + 1
    while jaux < 8:
        matrix[i, jaux] = 0
        jaux = jaux + 1

    iaux = i - 1
    jaux = j
    while iaux > -1:
        matrix[iaux, j] = 0
        iaux = iaux - 1

    iaux = i
    jaux = j - 1
    while jaux > -1:
        matrix[i, jaux] = 0
        jaux = jaux - 1

    # Diagonal
    iaux = i + 1
    jaux = j + 1
    while iaux < 8 and jaux < 8:
        # print("a", iaux, jaux, "\n")
        matrix[iaux, jaux] = 0
        # print("a\n", matrix)
        iaux = iaux + 1
        jaux = jaux + 1

    iaux = i + 1
    jaux = j - 1
    while iaux < 8 and jaux > -1:
        # print("b", iaux, jaux, "\n")
        matrix[iaux, jaux] = 0
        # print("b\n", matrix)
        iaux = iaux + 1
        jaux = jaux - 1

    iaux = i - 1
    jaux = j + 1
    while iaux > -1 and jaux < 8:
        # print("c", iaux, jaux, "\n")
        matrix[iaux, jaux] = 0
        # print("c\n", matrix)
        iaux = iaux - 1
        jaux = jaux + 1

    iaux = i - 1
    jaux = j - 1
    while iaux > -1 and jaux > -1:
        # print("d", iaux, jaux, "\n")
        matrix[iaux, jaux] = 0
        # print("d\n", matrix)
        iaux = iaux - 1
        jaux = jaux - 1

    return matrix


def findPos(allMatrix, matrixSafe):
    allMatrixAux = allMatrix.copy()
    largura, altura = matrixSafe.shape
    matrixAux = np.copy(matrixSafe)
    for i in range(largura):
        for j in range(altura):
            if matrixAux[i, j] == 1:
                matrixTest = marcaLocal(matrixAux, i, j)
                allMatrixAux.insert(0, matrixTest)
                matrixAux = matrixSafe

    return allMatrixAux


if __name__ == '__main__':
    matrix = np.ones((8, 8)).astype(int)

    # print(matrix)

    # 0 = area de atack
    # 1 = vazio
    # 2 = area de rainha

    count = 0
    allMatrix = [[[]]]
    matrixCorretas = [[[]]]
    allMatrix.insert(0, matrix.copy())
    matrixVistas.insert(0, matrix.copy())
    allMatrix.pop(1)
    matrixVistas.pop(1)

    while np.size(allMatrix) > 0:
        matrixSafe = allMatrix[0]
        #print("M", matrixSafe)
        #allMatrix = np.array(allMatrix).tolist()
        allMatrix.pop(0)
        allMatrix = findPos(allMatrix, matrixSafe)

        if countRainha(matrixSafe) == 8:

            if verIgualdade(matrixSafe, matrixCorretas):
                matrixCorretas.insert(0, matrixSafe)
                #print(np.size(matrixCorretas))

        if countRainha(matrixSafe) == 1:
            count = count + 1
            print(count)

    print(np.size(matrixCorretas))
    printMatrix(matrixCorretas)
