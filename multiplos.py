""" Faça um algoritmo para apresentar se dois números são múltiplos. """

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if (num1>num2) and (num1%num2==0):
    print("Os números são múltiplos!")
else:
     if (num2>num1) and (num2%num1==0):
        print("Os números são múltiplos!")
     else: 
        if(num1%num2!=0) or (num2%num1!=0):
            print("Os números não são múltiplos!")


