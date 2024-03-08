#o fatorial de um número

valor = int(input("Digite um número para cálculo do fatorial: "))

fatorial = 1
i = 1

# Com for
# for i in range(1, valor + 1):
#   print(i)
#   #fatorial = fatorial * i
#   fatorial *= i

# Com while
while i <= valor:
  fatorial *= i
  i += 1

print(f"O fatorial de {valor} é {fatorial}")

    
