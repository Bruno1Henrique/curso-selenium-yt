lista_de_numeros = [1, 2, 3, 4, 5, 6, 6, 8, 9, 10]
resposta = int(input('Qual e o numero? '))

for numero in lista_de_numeros:
    print(f'{numero} X {resposta} = {resposta * numero}')