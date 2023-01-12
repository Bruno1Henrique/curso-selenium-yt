carteira = int(input('Quanto eu tenho? '))
tenis = int(input('Quanto custa o tenis? '))
necessidade = input('Preciso mesmo? [s/n] ')

if carteira > tenis and necessidade == 's':
    print('Deu boa')
elif carteira == tenis:
    print('Vou ficar zerado')
else:
    print('deixa quieto')