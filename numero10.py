numero = float(input("digite um numero"))

if numero > 0 and numero % 2 == 0:
    print('positivo e par')

elif numero > 0 and numero % 3 == 0:
    print('positivo e multiplo de tres')

elif numero < 0 and numero % 2 != 0:
    print('negativo e impar')

elif numero == 0:
    print('zero')

else:
    print('nao e nenhum desses')
