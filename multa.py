print('Este programa analisa sua velocidade')

vel = int(input('Insira a sua velociadade: '))

if vel <= 80 :
    print('Você está dentro do limite')

elif vel == 80 :
    print('Você está no limite')

elif vel >= 80:
    print('Você ultrapassou o limite da velocidade\ne recebera uma multa por cada KM ultrapassado')

    final = float((vel-80)*7)
    print('sua multa é de R$',final)

else:
    ('erro')