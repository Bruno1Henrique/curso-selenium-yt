resposta = input('Vamos sair hoje? [s/n]')

n = 1

while resposta != 's':
   resposta = input(f'Bora{"a" *n} [s/n]?? ')
   n = n + 1
   if 'chato' in resposta:
    print(f'Foi mal')
    break        
else:
    print(f'Entao, bora{"a" * n}')