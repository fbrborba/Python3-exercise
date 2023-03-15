dias = int(input('Quantos dias alugados? '))
km = float(input('Quandos Km rodados? '))

# print('O total a pagar é de R$ {}'.format(dias*60 + km*0.15))
print(f'O total a pagar é de R${dias*60+km*0.15:.2f}')