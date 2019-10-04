import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle
import math

mpl.use('Agg')

def listaInvertida(tam):
    lista = list(range(1, tam + 1))
    return lista[::-1]

def listaAleatoria(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def insertion_sort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b


def hashing(array):
    m = array[0]
    for i in range(1, len(array)):
        if (m < array[i]):
            m = array[i]
    result = [m, int(math.sqrt(len(array)))]
    return result


def re_hashing(i, code):
    return int(i / code[0] * (code[1] - 1))

def bucket_sort(array):
    code = hashing(array)
    buckets = [list() for _ in range(code[1])]
    for i in array:
        x = re_hashing(i, code)
        buck = buckets[x]
        buck.append(i)
    for bucket in buckets:
        insertion_sort(bucket)

    ndx = 0
    for b in range(len(buckets)):
        for v in buckets[b]:
            array[ndx] = v
            ndx += 1

def desenhaGrafico(x, y,label, name, xl="Tamanho da Lista", yl="Tempo"):

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label )
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(name)


tam = [100000, 200000, 400000, 500000, 1000000, 2000000]
time = []

for i in range(len(tam)):
    lista = listaAleatoria(tam[i])
    time.append(
        timeit.timeit("bucket_sort({})".format(lista), setup="from __main__ import bucket_sort", number=1))

    print("executado o sort na lista de tamanho", tam[i])


desenhaGrafico(tam, time,"Lista aleatória", "tempo.png")
