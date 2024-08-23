nome = input('Digite seu nome: ')
n= len(nome)

if n <= 4:
    print('Nome curto')
if n <= 6 and n >=5:
    print('Nome normal')
if n >6:
    print('Nome grande')    
