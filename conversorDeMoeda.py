real = float(input('Quantos reais você tem: '))
dolar = real / 4.15
print('com RS${} você pode comprar US${:.2f}'.format(real,dolar))