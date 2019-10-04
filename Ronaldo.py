#Bubble sort em ordem descrescente com pilha#

from sys import maxsize 

lista = [1,2,3,4,5,6,7,8,9,10]

def bubbleDecrescente(lista):
    for i in range(len(lista)-1,0,-1):
        for i in range(i):
            if lista[i]<lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    return(lista)

print(bubbleDecrescente(lista))

def criaPilha(): 
    pilha = [] 
    return pilha 
  

def isEmpty(pilha): 
    return len(pilha) == 0
  

def push(pilha, item): 
    pilha.append(item) 
      

def pop(pilha): 
    if (isEmpty(pilha)): 
        return str(-maxsize -1)
      
    return pilha.pop() 
  

def peek(pilha): 
    if (isEmpty(pilha)): 
        return str(-maxsize -1)
    return pilha[len(pilha) - 1] 
     
pilha = criaPilha() 

x = []

for i in range(10):
    push(pilha, str(lista[i])) 

for i in range(10):
    x.append((pop(pilha)))

print(x)
