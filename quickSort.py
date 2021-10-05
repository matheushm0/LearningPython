import matplotlib.pyplot as plt
from timeit import timeit
from random import randint

def quickSort(lista):
        L = []
        R = []
        if len(lista)<=1:
                return lista
        chave = lista[len(lista)//2]
        for i in lista:
                if i < chave:
                        L.append(i)
                if i > chave:
                        R.append(i)
        return quickSort(L) + [chave] + quickSort(R)
 
def quickSort2(lista):
        L = []
        R = []
        if len(lista)<=1:
                return lista
        chave = lista[0]
        for i in lista:
                if i < chave:
                        L.append(i)
                if i > chave:
                        R.append(i)
        return quickSort(L) + [chave] + quickSort(R)
 
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

def desenhaGrafico(x,y,z, w, xl = "Tamanho", yl = "Tempo(s)"):
	fig = plt.figure(figsize=(10, 8))
	ax = fig.add_subplot(111)
	ax.plot(x,y, label = "Pior Caso")
	plt.plot(x, z, label= "Caso Medio")
	plt.plot(x, w, label= "Caso Medio(Pivo 1º elemento)")
	ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
	plt.ylabel(yl)
	plt.xlabel(xl)
	fig.savefig("quicksort00.png")

length = []
time1 = []
time2 = []
time3 = []

for tams in range (3000, 24001, 3000):
	length.append(tams)
	lista1 = random_list(tams)
	lista2 = reverse_list(tams)
	time1.append(timeit("quickSort({})".format(lista1),setup="from __main__ import quickSort",number=1))
	time2.append(timeit("quickSort({})".format(lista2),setup="from __main__ import quickSort",number=1))
	time3.append(timeit("quickSort2({})".format(lista2),setup="from __main__ import quickSort2",number=1))

desenhaGrafico(length, time1, time2, time3)
