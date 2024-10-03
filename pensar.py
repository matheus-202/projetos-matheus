print('Tente adivinhar o número')

import random

num = random.randint(0,5)
numer = ''

while num != numer:

    numer = int(input('Adivinhe um número de 0 a 5: ')) 

    if num >= numer:
        print('o número sorteado é maior')

    elif num <= numer:
        print('o número sorteado é menor')

else:
    print('PARABENS')



    





