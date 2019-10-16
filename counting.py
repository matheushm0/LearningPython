#counting_sort
def counting_sort(lista):
    aux_list = [0] * (max(lista) + 1)
    for item in lista:
        aux_list[item] += 1
    i = 0
    lista.clear()
    for item_index in range(len(aux_list)):
        lista.extend([item_index+1]*aux_list[item_index])

if __name__ == '__main__':
	
	lista = [5,1,23,4,12,4,345,36,45,4,52,3,234]
	
	counting_sort(lista)
	
	print(lista)