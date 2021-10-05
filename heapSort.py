import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from timeit import timeit
from random import randint

def heapsort(lista):
  for start in range((len(lista)-2)//2, -1, -1):
    siftdown(lista, start, len(lista)-1)
 
  for end in range(len(lista)-1, 0, -1):
    lista[end], lista[0] = lista[0], lista[end]
    siftdown(lista, 0, end - 1)
  return lista
 
def siftdown(lista, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lista[child] < lista[child + 1]:
      child += 1
    if lista[root] < lista[child]:
      lista[root], lista[child] = lista[child], lista[root]
      root = child
    else:
      break

def reverse_list(tam):
    lista = []
    i = 0
    while i < tam:
        lista.append(tam - i)
        i = i + 1
    return lista
      
def random_list(tam):
    lista = [ ]
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def desenhaGrafico(x,y,z,xl = "Elementos", yl = "Tempo"):
	fig = plt.figure(figsize=(10, 10))
	ax = fig.add_subplot(111)
	ax.plot(x,y, label = "Pior Caso")
	plt.plot(x, z, label="Caso Medio")
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig('heapsort.png')

length = []
time1 = []
time2 = []

for tams in range(3000, 24001, 3000):
    length.append(tams)
    time1.append(timeit("heapsort({})".format(random_list(tams), tams),setup="from __main__ import heapsort",number=1))
    time2.append(timeit("heapsort({})".format(reverse_list(tams), tams),setup="from __main__ import heapsort",number=1))

desenhaGrafico(length, time1, time2)
