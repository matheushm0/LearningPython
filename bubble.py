import matplotlib.pyplot as plt
from random import randint
import timeit

def geraLista(arr):

    array = []

    while len(array) < arr:
        n = randint(1, 1 * arr)
        if n not in array: array.append(n)
    return array

operacoes = []
arr = [10000, 20000, 50000, 100000]
aux = []

def bubbleSort(array):
    ciclos = 0
    size = len(array)

    for i in range(size):
        for x in range(0, size - i - 1):
            if array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]
                ciclos += 1
    operacoes.append(ciclos)


def showGraph(x, y, imgName = "img", xl = "Inputs", yl = "Outputs"):
    fig = plt.figure(figsize=(12, 16))
    plt.plot(x, y, label = "Melhor Tempo")
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(imgName)

for i in arr:
  list = geraLista(i)
  aux.append(geraLista(i))

time =[]
for i in range(len(aux)):
    time.append(timeit.timeit("bubbleSort({})".format(aux[i]),setup="from __main__ import bubbleSort",number=1))

showGraph(arr, time, 'Tempo', 'Numbers', 'Time')
showGraph(arr, operacoes, 'Iterações no laço')
