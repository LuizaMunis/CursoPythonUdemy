numero=0
lista = []

for i in range(1, 6):
    numero = int(input('Digite:'))
    lista.append(numero)

for numero in lista:
    soma += numero

print(soma)