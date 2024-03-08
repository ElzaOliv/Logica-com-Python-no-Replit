#Soma Valores Pares e Multiplica Valores impares

lista_de_numeros = [20,9,8,7,5]
listadePares = []
listadeImpares = []

for numero in lista_de_numeros:
  if numero % 2 == 0:
    listadePares.append(numero)
  else:
    listadeImpares.append(numero)
    
print(listadePares)
print(listadeImpares)
somaPar = 0
multiplicarImpar = 1

for numeroPar in listadePares:
  somaPar = numeroPar + somaPar
  
print(somaPar)

for numeroImpar in listadeImpares:
  multiplicarImpar = numeroImpar * multiplicarImpar
  
print(multiplicarImpar)

#Reduzido____________

valores = [20, 9, 8, 7, 100, 103]
soma = 0
multiplicacao = 1

for valor in valores:
  if valor % 2 == 0:
    soma = soma + valor
  else:
    multiplicacao = multiplicacao * valor

print("A soma dos valores pares é:", soma)
print("A multipllicação de valores ímpares é:", multiplicacao)

