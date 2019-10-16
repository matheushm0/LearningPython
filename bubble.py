#bubble_sort
def bubblesort(lista):
    for element in lista:
        for element_index in range(len(lista) - lista.index(element) - 1):
            if lista[element_index] > lista[element_index+1]:
                lista[element_index],lista[element_index+1] = lista[element_index+1],lista[element_index]

if __name__ == '__main__':
	
	lista = [12,312,24,5,6,45,7,4,23,4,45,75,68]
	
	bubblesort(lista)

	print(lista)