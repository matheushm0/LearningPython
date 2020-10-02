class Arvore:
	def __init__(self, valor):
		self.valor    = valor;
		self.esquerda = None;
		self.direita  = None;
	def __str__(self):
		return "{",str(valor),"}"

############# Metodos de Busca #############
def pesquisar(no, valor):
        if no == None:
            return 0
        else:
            if valor == no.valor:
                return 1
            else:
                if valor < no.valor:
                    return pesquisar(no.esquerda, valor)
                else:
                    return pesquisar(no.direita, valor)

############ Metodo de Insercao ############
def inserir(no, valor):
	if no is None:
		no = Arvore(valor);
	else:
		if valor < no.valor:
			no.esquerda = inserir(no.esquerda, valor);   
		else:
			no.direita  = inserir(no.direita, valor);  
	return no;
############################################

########### Metodos de Impressao ###########
ImprimeArvore = ''

def preOrdem(no):
	global ImprimeArvore
	if no is None:
		return
	ImprimeArvore += str(no.valor) + ', '
	preOrdem(no.esquerda)
	preOrdem(no.direita)
	
def emOrdem(no):
	global ImprimeArvore
	if no is None:
		return
	emOrdem(no.esquerda)
	ImprimeArvore += str(no.valor) + ', '
	emOrdem(no.direita)

def posOrdem(no):
	global ImprimeArvore
	if no is None:
		return
	posOrdem(no.esquerda)
	posOrdem(no.direita)
	ImprimeArvore += str(no.valor) + ', '
############################################

def excluir(no, valor):
        if pesquisar(no, valor) == 1:
            if no.valor == valor:
                if no.esquerda == no.direita:
                    no = None
                elif no.esquerda == None:
                    tmp = no.direita
                    no = None
                    return tmp
                elif no.direita == None:
                    tmp = no.esquerda
                    no = None
                    return tmp
                else:
                    tmp = no.direita
                    tmp2 = no.direita
                    while tmp.esquerda is not None:
                        tmp = tmp.esquerda
                    tmp.esquerda = no.esquerda
                    no = None
                    return tmp2;
            elif no.valor < valor:
                no.direita = excluir(no.direita, valor)
            else:
                no.esquerda = excluir(no.esquerda, valor)

            return no
        else:
            print("Número não encontrado na árvore")
#####################################################

arvore = Arvore(0)
n = int(input("Quantos valores na árvore? "))
i = 1
while (n > 0):
    print("Valor do nó", i, ": ")
    val = int(input())
    if pesquisar(arvore, val) == 0 :
        inserir(arvore, val)
        n -= 1
        i += 1
    else:
        print("Valor já está na árvore!")

print("\nÁrvore criada\n")

ImprimeArvore = ""
preOrdem(arvore)
print ("Pré-Ordem: " + ImprimeArvore + "\n")
ImprimeArvore = ""
emOrdem(arvore)
print ("Em-Ordem: " + ImprimeArvore + "\n")
ImprimeArvore = ""
posOrdem(arvore)
print ("Pós-Ordem: " + ImprimeArvore + "\n")

pesq = int(input("\nPesquisar um número: "))
if pesquisar(arvore, pesq) == 1:
    print("Número encontrado na árvore!\n")
else:
    print("Número NÃO encontrado na árvore!\n")


exc = int(input("\nExcluir um número: "))
arvore = excluir(arvore, exc)

if(arvore != None):
    print("Número excluido\n")
    ImprimeArvore = ""
    emOrdem(arvore)
    print ("EmOrdem: " + ImprimeArvore + "\n")
