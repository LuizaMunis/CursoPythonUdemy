try:
    numero = int(input('Digite um número: '))
    resposta = 'ímpar'

    if numero % 2 == 0:
        resposta = 'par'
    
    print(resposta)
except ValueError:
    print('Só digite um número inteiro.')

