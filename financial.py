print(100 * "-")
print("""Olá, esse é um programa pra calcular o seu lucro economizando uma quantia
por um determinado periodo de tempo.\n""")

total = 0
meses_economizados = int(input("Diga quantos meses você quer economizar: "))
valor_mensal = int(input("Quanto você quer guardar por mês? "))
ja_tem_dinheiro = input("você ja tem dinheiro guardado ? digite sim ou nao: ")

if ja_tem_dinheiro == "sim":
    valor = int(input("Quanto? "))
    total = valor + (meses_economizados * valor_mensal)
    print(f'Com R${valor} ja guardado, você irá ter {total} guardando {valor_mensal} por {meses_economizados} meses')
elif ja_tem_dinheiro == "nao":
    total = meses_economizados * valor_mensal
    print(f'Você irá ter {total} guardando {valor_mensal} por {meses_economizados} meses')
print(100 * "-")