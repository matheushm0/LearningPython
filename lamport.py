# Processo e Pipe de multiprocessamento para executar vários processos Python com um script
from multiprocessing import Process, Pipe
# obter a id do processo de cada processo
from os import getpid
# obter a hora atual 
from datetime import datetime

# imprime o carimbo de data / hora Lamport local e a hora real da máquina que está executando os processos
##PS: imprimir a hora "real" não faz sentido em um sistema distribuído real, uma vez que os relógios 
##    locais não serão sincronizados entre si.
def local_time(counter):
    return ' (LAMPORT_TIME={}, LOCAL_TIME={})'.format(counter,
                                                     datetime.now())
# novo timestamp quando um processo recebe uma mensagem. A função pega o máximo do carimbo de data / hora 
# recebido e seu contador local e o incrementa com um.
def calc_recv_timestamp(recv_time_stamp, counter):
    return max(recv_time_stamp, counter) + 1

# função para cada evento que possa ocorrer
def event(pid, counter):
    counter += 1
    #evento de evento pega o contador local e o id do processo (pid), incrementa o contador em um, imprime uma linha para que saibamos que o evento ocorreu
    print('Something happened in {} !'.\
          format(pid) + local_time(counter))
    #as funções de evento retornarão o timestamp atualizado para o processo em que o evento ocorre
    return counter

# Pipe é um objeto da biblioteca de multiprocessamento que representa uma conexão bidirecional entre dois processos
# envia uma mensagem real e seu carimbo de data / hora incrementado e imprime uma instrução curta incluindo a nova hora Lamport local e a hora real na máquina. 
# retorna o novo carimbo de data / hora local
def send_message(pipe, pid, counter):
    counter += 1
    pipe.send(('Empty shell', counter))
    print('Message sent from ' + str(pid) + local_time(counter))
    return counter

# recebe a mensagem real e o carimbo de data / hora invocando a função recv no pipe
# calcula o novo timestamp com nossa função calc_recv_timestamp criada anteriormente e imprime uma linha incluindo o contador atualizado e a hora real na máquina
def recv_message(pipe, pid, counter):
    message, timestamp = pipe.recv()
    counter = calc_recv_timestamp(timestamp, counter)
    print('Message received at ' + str(pid)  + local_time(counter))
    return counter

#definições de nossos três processos
#processo começa com a obtenção de seu id de processo exclusivo e definindo seu próprio contador para 0
#o contador é atualizado invocando as diferentes funções de evento e passando o valor retornado para o contador
def process_one(pipe12):
    pid = getpid()
    counter = 0
    counter = event(pid, counter)
    counter = send_message(pipe12, pid, counter)
    counter  = event(pid, counter)
    counter = recv_message(pipe12, pid, counter)
    counter  = event(pid, counter)

def process_two(pipe21, pipe23):
    pid = getpid()
    counter = 0
    counter = recv_message(pipe21, pid, counter)
    counter = send_message(pipe21, pid, counter)
    counter = send_message(pipe23, pid, counter)
    counter = recv_message(pipe23, pid, counter)


def process_three(pipe32):
    pid = getpid()
    counter = 0
    counter = recv_message(pipe32, pid, counter)
    counter = send_message(pipe32, pid, counter)

#criar os dois pipes (Pipe ()) e três processos (Process ()), necessários para executar o nosso script com sucesso. 
#para iniciar os processos, precisamos chamar start e join em cada processo. 
#join nos garante que todos os processos serão concluídos antes de sair.
if __name__ == '__main__':    
    oneandtwo, twoandone = Pipe()
    twoandthree, threeandtwo = Pipe()

    process1 = Process(target=process_one, 
                       args=(oneandtwo,))
    process2 = Process(target=process_two, 
                       args=(twoandone, twoandthree))
    process3 = Process(target=process_three, 
                       args=(threeandtwo,))

    process1.start()
    process2.start()
    process3.start()

    process1.join()
    process2.join()
    process3.join()
