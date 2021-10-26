""" Dada a distância A e o combustível gasto B, faça um algoritmo para calcular o consumo médio. """

D = float(input("Digite a distância percorrida: ")) 
C = float(input("Digite a quantidade de combustível gasta no percurso: "))

consumoMedio = float(D/C)
print("O consumo médio de combustível foi: ", consumoMedio, "litro(s) por km percorrido.")

