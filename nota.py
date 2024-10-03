print('Este programa informa sua situação da escolar\nA partir de suas notas')

nota = float(input('Insira a sua nota: '))

if nota <= 6:
    print('F')
elif nota >=6.1 and nota <=6.9:
    print('E')
elif nota >=7.0 and nota <=7.9 :
    print('D')
elif nota >=8.0 and nota <=8.9:
    print('C')
elif nota >=9.0 and nota <=9.9:
    print('B')
elif nota == 10: 
    print('A\nParabens!')
else:
    print('ERRO')