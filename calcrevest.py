from math import ceil
largpar = float(input('Largura da parede: '))
altpar = float(input('Altura da parede: '))
largrevest = float(input('Largura do revestimento: '))
altrevest = float(input('Altura do revestimento: '))
revest = largrevest * altrevest
area = largpar * altpar
qtd = (area / revest) + (area / revest) * 10/100
print(f'Para uma área de {area:.2f}M², serão necessárias {ceil(qtd)} unidades')
