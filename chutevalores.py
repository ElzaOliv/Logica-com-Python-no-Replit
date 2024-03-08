#Escreva um programa que gere um numero aleatório de 10 e permita ao usuario chutar um numero até que o aleatório seja igual ao chute.
#Ao chutar, caso o valor esteja errado, informar se o valor está abaixo ou acima do chute.
#O proigrama deve permitir que no máximo 3 chutes sejam tentados.

from random import randint

valor_random = randint(1,10)
numero_tentativas = 0
acertou = False

while (numero_tentativas < 3) and (acertou is False):
  numero_tentativas = numero_tentativas + 1

  valor_chute = int(input("Digite o valor do chute: "))

  if valor_chute == valor_random:
    print("Você acertou!")
    acertou = True
  elif valor_chute > valor_random:
    print("Seu chute foi acima do valor gerado!")
  else:
    print("Seu chute foi abaixo do valor gerado!")

if (acertou is False):
  print("Você errou as 3 tentativas! O valor randômico era:", valor_random)

