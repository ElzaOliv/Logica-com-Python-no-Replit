# Crie um programa que recebe um número e o incrementa por 1 por 10 vezes
# valor = 10;
# em cada repetição: valor = valor + 1 (por 10 vezes)
# valor final deve ser 20

valor = int(input("Digite um número: "))

#loop de X a Y
for _i in range(10):  
  valor = valor + 1
  #print(valor)

print("O valor final é:", valor)
