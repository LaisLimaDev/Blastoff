"""  Faça um algoritmo que receba um número e retorne se o número é primo ou não. """

num=int(input("Digite um número: "))
div=0
for c in range(1, num+1):
    if num%c==0:
        print('\033[33m', end='')
        div+=1
    else:
        print('\033[31m', end='')
if div==2:
    print('O número é primo!')
else:
    print('O número não é primo!')
