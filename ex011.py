larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = alt * larg
# print('Sua parede tem dimensoes de {}x{}, e sua área é de {:.1f}m²'.format(larg, alt, área)) # COM .FORMAT
print(f'Sua parede tem dimensoes de {larg:.0f}x{alt:.0f}, e sua área é de {larg*alt:.1f}m². ')
print(f'Voce terá que usar {área/2:.1f}l de tinta. ')

