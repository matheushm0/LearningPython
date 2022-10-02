dias = int(input('Digite a quantidade de diárias: '))
km = float(input('Digite os km percorridos: '))
total = (dias * 60) + (km * 0.15)
print('Com {} dias e {} km rodados, o valor total do aluguel ficou R${:.2f}'.format(dias, km, total))