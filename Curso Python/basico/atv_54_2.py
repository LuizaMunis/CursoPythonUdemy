try:
    horas=int(input('Digite as horas:'))

    if horas >=0 and horas <=11:
        print('Bom dia')
    elif horas >=12 and horas<17:
        print('Boa Tarde')
    elif horas >= 18 and horas<=23:
        print('Boa Noite')
    else:
        print('O dia só tem 24 horas.')    

except: 
    print('Diita um numero inteiro!!!')   
26