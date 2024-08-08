nome = 'otavio'

print('a' in nome)

nome1=input('Digite nome:')
encontrar=input('Digite o que quer encontrar')

if encontrar in nome1:
    print(f'{encontrar} esta em {nome1}')
else:
    print(f'{encontrar} nao esta em {nome1}')

variavel_a = 1 or 0
variavel_b = 0 or 1
print(variavel_a, variavel_a)