nome = input('Digite nome: ')
idade = input('Digite idade: ')

if not nome or not idade:
    print('Tem que digitar, né filha!')
else:
    espaço = ' ' in nome
    print(f'{nome}\n{nome[::-1]}\n{len(nome)}\nPrimeira letra: {nome[0].upper()}\nÚltima letra: {nome[-1]}\nEspaço: {espaço}')

#espaço = 1 if ' ' in nome else 0
#podia usa if nome and idade e else seria que a pessoa não colocou nada.