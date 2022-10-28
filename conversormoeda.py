from time import sleep
r = 'S'
print('\033[1;35;7m$\033[m'*20)
print('{:^27}'.format('\033[1;35mCONVERSOR DE MOEDA\033[m'))
print('\033[1;35;7m$\033[m'*20)
while r == 'S':
    print('''Qual moeda deseja converter?
[1]Real/Dólar
[2]Dólar/Real
[3]Real/Libra Esterlina
[4]Libra Esterlina/Real
[5]Real/Euro
[6]Euro/Real''')
    converter = int(input('\033[1;35mQual moeda deseja converter? '))
    if converter == 1:
        real = float(input('REAL: R$'))
        dólar = float(input('DÓLAR: U$D'))
        converter = real / dólar
        print('\033[1;36mConvertendo REAL para DÓLAR...')
        sleep(2)
        print(f'\033[1;36mR${real:.2f} corresponde a: U$D{converter:.2f}\033[m')
    elif converter == 2:
        dólar = float(input('D0LAR: U$D'))
        real = float(input('REAL: R$'))
        converter = dólar * real
        print('\033[1;32mConvertendo DÓLAR para REAL...')
        sleep(2)
        print(f'\033[1;32mU$S{dólar:.2f} corresponde a: R${converter:.2f}\033[m')
    if converter == 3:
        real = float(input('REAL: R$'))
        libra = float(input('LIBRA ESTERLINA: £'))
        converter = real / libra
        print('\033[1;35mConvertendo REAL para LIBRA ESTERLINA...')
        sleep(2)
        print(f'\033[1;35mR${real:.2f} corresponde a: £{converter:.2f}')
    elif converter == 4:
        libra = float(input('LIBRA ESTERLINA: £'))
        real = float(input('REAL: R$'))
        converter = libra * real
        print('\033[1;33mConvertendo LIBRA ESTERLINA para REAL...')
        sleep(2)
        print(f'\033[1;33mCom £{libra:.2f} corresponde a: R${converter:.2f}')
    if converter == 5:
        real = float(input('REAL: R$'))
        euro = float(input('EURO: €'))
        converter = real / euro
        print('\033[1;32mConvertendo REAL para EURO...')
        sleep(2)
        print(f'\033[1;32mR${real:.2f} corresponde a: €{converter:.2f}')
    elif converter == 6:
        euro = float(input('EURO: €'))
        real = float(input('REAL: R$'))
        converter = euro * real
        print('\033[1;31mConvertendo EURO para REAL...')
        sleep(2)
        print(f'\033[1;31m€{euro:.2f} corresponde a: R${converter:.2f}')
    r = str(input('Deseja continuar? [S/N] ')).upper()
print('PROGRAMA FINALIZADO!')
