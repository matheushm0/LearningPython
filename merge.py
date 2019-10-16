#merge_sort
def intercala(lista,lista1,lista2):
	x,y,z = (0,0,0)
	tam = len(lista1)+len(lista2)
	while x != tam:
		if len(lista1) == 0:
			lista[x] = lista2[0]
			lista2.pop(0)
		elif len(lista2) == 0:
			lista[x] = lista1[0]
			lista1.pop(0)	
		elif lista1[0]<lista2[0] or len(lista2)==0:
			lista[x] = lista1[0]
			lista1.pop(0)	
		else:
			lista[x] = lista2[0]
			lista2.pop(0)
		x += 1

def mergeSort(lista):
	if len(lista)>1:
		meio = len(lista)//2

		lista1 = lista[:meio]

		lista2 = lista[meio:]

		mergeSort(lista1)

		mergeSort(lista2)

		intercala(lista,lista1,lista2)

if __name__ == '__main__':

	lista= [12,312,4,1,5,12,312,3,41,25,2,34,23,42,34,12,3,12]
	
	mergeSort(lista)

	print(lista)