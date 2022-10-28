print('X:' * 25)
print(f'{"CALCULADORA PARA DESCONTO DE ÁREA":^25}')
print('X:' * 25)
altura = float(input('Altura parede: '))
largura = float(input('Largura parede: '))
area_bruta = altura * largura
desconto_altura = float(input('Altura desconto: '))
desconto_largura = float(input('Largura desconto: '))
total_area = (altura * largura) - (desconto_altura * desconto_largura)
print(f'A área bruta calculada é de {area_bruta:.2f}m²')
print(f'A área total é de {total_area:.2f}m²')

