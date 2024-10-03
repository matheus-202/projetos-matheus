def soma(a,b):
    cal = a+b
    print(cal)

def soma_mul(a,b):
    con = a*b
    print(con)

def dois(a,b,c):
    res = (a+b)*c
    print(res)

def soma_2(a,b):
    print(f'A = {a} B = {b}')
    s = a + b
    print(' A soma de a+b =',s )

def contador(*n):
    tam = len(n)
    print(f'você tem {n} no total são {tam} números')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst [pos] *= 2
        pos += 1

val = [1,2,4,3,5,6,8,10]
dobra(val)
print(val)


'''
contador(2,3,4,5)
contador(4,7)
contador(3,66,7,664,67833,4,6,8,2)

soma(2,3)
soma_mul(2,3)
dois(2,2,5)
soma_2(b=55,a=40)
'''