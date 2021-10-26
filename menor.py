""" Dados três números (a, b, c), faça um algoritmo para mostrar o menor número. """

a = float(input("Digite o número a: "))
b = float(input("Digite o número b: "))
c = float(input("Digite o número c: "))

if a>c and b>c:
    print("O menor dos três números é: ",c)
else:
    if b>a and c>a:
        print("O menor dos três números é: ",a)
    else:
     if a>b and c>b:
        print("O menor dos três números é: ",b)