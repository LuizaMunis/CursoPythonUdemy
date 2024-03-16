idade= int (input('Digite a idade:'))
if (idade >0) and (idade <=12):
    print('Criança')
else:
  if (idade>12) and(idade<=17):
    print('Adolescente')
  else:
    if  idade>18:
      print('Adulto')
    else:
        if idade<0:
          print('Idade invalida!')