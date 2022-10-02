preço = float(input('Diga qual o valor do produto R$ '))
desconto = int(input('Diga o valor do desconto em porcentagem: '))
descontoAplicado = preço * (desconto / 100)
valorFinal = preço - descontoAplicado
print('o produto de R${} com um desconto de {}% sairá por R${}'.format(preço, desconto, valorFinal))