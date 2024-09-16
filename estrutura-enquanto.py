#1ª forma de utilizar while - semelhante ao FOR

contador = 1

while contador <= 5:
  print(contador)
  contador += 1
print("<=>"*40)

#2ª forma de utilizar while - loop condicional normal

valor = 0

while valor >= 0:
  valor = int(input("Informe um valor qualquer (digite um valor negativo para terminar): "))

  print(f"Você digitou {valor}")

#3ª forma de utilizar while - semelhante a estrtura faça...enquanto

while True:
  senha = input("Informe sua senha: ")
  if senha == "123":
    print("Parabéns, senha correta")
    break
  else:
    print("Essa senha ja pertence à Eduardo_332, tente novamente")