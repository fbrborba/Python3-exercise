pdt = float(input('Qual é o preço do produto? R$'))
#print('O produto que custa {}, na promoçao com desconto de 5% vai custar R${}'.format(pdt, pdt - pdt*5/100)) # COM .FORMAT
print(f'O produto que custava R${pdt:.2f}, na promoçao com desconto de 5% vai custar R${pdt - pdt*5/100:.2f}')