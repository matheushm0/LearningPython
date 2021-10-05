import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as interpolate
from timeit import timeit
from random import randint
import math

def bucketSort(lists):
	code = hashing(lists)
	buckets = [list() for _ in range(code[1])]
	for i in lists:
		x = re_hashing(i, code)
		buck = buckets[x]
		buck.append(i)
	for bucket in buckets:
		insertionsort(bucket)

	ndx = 0
	for b in range(len(buckets)):
		for v in buckets[b]:
			lists[ndx] = v
			ndx += 1
			
	return lists
			
def hashing(lists):
	m = lists[0]
	for i in range(1, len(lists)):
		if (m < lists[i]):
			 m = lists[i]
	result = [m, int(math.sqrt(len(lists)))]
	return result

def re_hashing(i, code):
	return int(i / code[0] * (code[1] - 1))
  
def insertionsort(lists):
    for i in range(1, len(lists)):
        temp = lists[i]
        j = i
        while j > 0 and temp < lists[j - 1]:
            lists[j] = lists[j - 1]
            j -= 1
        lists[j] = temp

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
	fig.savefig('bucket.png')

length = []
time1 = []
time2 = []

for tams in range(3000, 24001, 3000):
    length.append(tams)
    time1.append(timeit("bucketSort({})".format(random_list(tams), tams),setup="from __main__ import bucketSort",number=1))
    time2.append(timeit("bucketSort({})".format(reverse_list(tams), tams),setup="from __main__ import bucketSort",number=1))

desenhaGrafico(length, time1, time2)
