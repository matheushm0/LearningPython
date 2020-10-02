import numpy as np

set_matrix_final = lambda weight, high: [[i * weight + j for j in range(high)] for i in range(weight)]


def trade_position(matrix, i, j, indice):
    matrix_aux = matrix.copy()

    if indice == 1:
        # Up
        aux = matrix_aux[i, j]
        matrix_aux[i, j] = matrix_aux[i + 1, j]
        matrix_aux[i + 1, j] = aux
    if indice == 2:
        # Down
        aux = matrix_aux[i, j]
        matrix_aux[i, j] = matrix_aux[i - 1, j]
        matrix_aux[i - 1, j] = aux
    if indice == 3:
        # Right
        aux = matrix_aux[i, j]
        matrix_aux[i, j] = matrix_aux[i, j + 1]
        matrix_aux[i, j + 1] = aux
    if indice == 4:
        # Left
        aux = matrix_aux[i, j]
        matrix_aux[i, j] = matrix_aux[i, j - 1]
        matrix_aux[i, j - 1] = aux

    return matrix_aux


def check_final_start(check_list):
    matrix_final_aux = matrix_final = np.array(set_matrix_final(3, 3))
    for i in range(len(check_list)):
        if np.array_equal(matrix_final_aux, check_list[i]):
            print("Start Ended")
            return True
    return False


def check_repeat_array(check_list1, check_list2):
    for i in range(len(check_list1)):
        for j in range(len(check_list2)):
            if np.array_equal(check_list1[i], check_list2[j]):
                print("Meta Matrix:\n", check_list1[i])
                return True
    return False


def check_repeat_matrix(check_list, matrix):
    for i in range(len(check_list)):
        if np.array_equal(matrix, check_list[i]):
            return False
    return True


def set_pos(pos_vector, check_list, matrix):
    matriz = matrix.copy()
    i, j = find_zero(matriz)
    weight, high = matriz.shape

    if i + 1 < high:
        matrix_aux = trade_position(matriz, i, j, 1)
        if check_repeat_matrix(check_list, matrix_aux):
            pos_vector.append(matrix_aux)
    if i - 1 > -1:
        matrix_aux = trade_position(matriz, i, j, 2)
        if check_repeat_matrix(check_list, matrix_aux):
            pos_vector.append(matrix_aux)
    if j + 1 < weight:
        matrix_aux = trade_position(matriz, i, j, 3)
        if check_repeat_matrix(check_list, matrix_aux):
            pos_vector.append(matrix_aux)
    if j - 1 > -1:
        matrix_aux = trade_position(matriz, i, j, 4)
        if check_repeat_matrix(check_list, matrix_aux):
            pos_vector.append(matrix_aux)

    return pos_vector


def find_zero(matrix):
    weight, high = matrix.shape
    for i in range(weight):
        for j in range(high):
            if matrix[i, j] == 0:
                return i, j


if __name__ == '__main__':

    matrix_start = np.array(np.random.permutation(9).reshape(3, 3))
    matrix_final = np.array(set_matrix_final(3, 3))

    #matrix_start = np.array([[3, 1, 2],
    #                        [6, 4, 5],
    #                        [7, 8, 0]])

    print("MATRIX START:\n", matrix_start)
    print("MATRIX FINAL:\n", matrix_final)
    print("\n")

    pos_start = []
    pos_final = []
    check_list_start = []
    check_list_final = []

    check_repeat_matrix(check_list_start, matrix_start)
    check_repeat_matrix(check_list_final, matrix_final)

    pos_start.append(matrix_start)
    pos_final.append(matrix_final)

    # print(pos_start)
    # print("\n")
    # print(pos_final)

    while (True):
        matrix_safe_start = pos_start[0]
        matrix_safe_final = pos_final[0]

        # pos_start = pos_start.tolist()
        # pos_final = pos_final.tolist()

        pos_start.pop(0)
        pos_final.pop(0)

        # print("Matrix Safe Start:\n", matrix_safe_start)
        # print("Matrix Safe Final:\n", matrix_safe_final)
        # print("\n")

        if check_repeat_array(check_list_start, check_list_final):
            break

        if check_final_start(check_list_start):
            break

        pos_start = set_pos(pos_start, check_list_start, matrix_safe_start)
        pos_final = set_pos(pos_final, check_list_final, matrix_safe_final)

        if check_repeat_matrix(check_list_start, matrix_safe_start):
            check_list_start.append(matrix_safe_start)

        if check_repeat_matrix(check_list_final, matrix_safe_final):
            check_list_final.append(matrix_safe_final)
