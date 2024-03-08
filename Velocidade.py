# Escreva um programa que aplique uma multa caso a velocidade seja acima do limite de 80 km/h permitido:
# Até 10km/h por hora acima: multa leve
# Entre 11km/h e 20km/h: multa grave
# Acima de 20km/h: multa gravíssima
# O programa também deve verificar se a CHN está válida. Caso não esteja, deve aplicar multa gravíssima.


CNHValida = True
limitePermitido = 80
usuariosVelocidade = 101
if (usuariosVelocidade <= 90) and (usuariosVelocidade > 80):
  print("multaLeve")
elif (usuariosVelocidade >= 91 and usuariosVelocidade <= 100):
  print("multaGrave")
elif (usuariosVelocidade >100):
  print("multaGravissima")
else:
  print("limitePermitido")

if (CNHValida is True):
    print("CNH Valida")
else:
    print("Multa Gravissima")

