#tipos de variaveis (comentário)
#comentário não é uma boa prática, pq pode poluir o código e ficar desatualizado.
#No Payton eu não preciso declarar váriavel (apenas atribuir valor - Ex: Nome)
#No Java eu preciso declarar váriavel (Ex: String nome)


#Tipos de variáveis

#=============== String ou texto =================================
nome = 'Elza'
sobrenome = 'Souza'

print("O nome completo é:", nome, sobrenome)

print(type(nome))
nome = 'Maria'

print("O nome agora é: " + nome + " " + sobrenome)

#============= Integer ou número inteiro ========================
idade1 = 20
idade2 = 3

totalIdade = idade1 + idade2

# função que identifica o tipo da variável
print(type(totalIdade))

print("A soma das idades é:", totalIdade)

#============= Float ou número decimal ==========================

valorFloat01 = 20.55
valorFloat02 = 3.5

totalFloat = valorFloat01 / valorFloat02
#função que identifica o tipo da variável
print(type(totalFloat))

#função round() arredonda o valor
print("A soma dos valores é:", round(totalFloat, 3))

##============= Boolean ou lógico ===============================

#verdadeiro ou falso
existe = None

print("A variável existe é do tipo:", type(existe))

if existe:
  print("É igual a verdadeiro!", existe)
elif not existe:
  print("Existe é igual a falso!", existe)
else:
  print("Não é igual a verdadeiro nem falso!", existe)