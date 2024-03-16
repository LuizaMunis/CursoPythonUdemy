try :
  n1= int(input('Digite 1 numero:'))
  n2= int(input('digite 2 numero:'))

except ValueError:
  print('digitEs dois')

else:
  resultado = n1/n2
  print(resultado)