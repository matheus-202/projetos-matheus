print('este progrma calcula a sua media de notas')

funcao = True

n1  = float(input('digite sua primeira nota: '))
n2  = float(input('digite sua segunda nota: '))

media = (n1+n2)/2 

print('sua média é ',media)

if media >= 6.0 :
    print('parabens você foi aprovado!\ncontinue assim no próximo semestre')

elif media == 5.0 :
    print('você ficou em recuperação')
 
else :
    print ('lamentamos informar que você foi reprovado.\nestude mais no proximo semestre')