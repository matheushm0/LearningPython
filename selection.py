#selection_sort

def selection_sort(lista):
    for i in range(len(lista)):

        menor = i
        for j in range(i + 1, len(lista)):
            if lista[menor] > lista[j]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

if __name__ == '__main__':
	lista = [12,123,4,12,3,2,534,645,74,5,34,52,34,2]
	
	selection_sort(lista)

	print(lista)