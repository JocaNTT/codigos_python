#1ª forma de operação do for
for contador in range(1,6):
  print(contador)

print("-"*40)
#2ª forma de operação do for
for contador in range(1,11,2):# o 3ª parâmetro indica como os valores serão incrementados(altera de valor)
  print(contador)

print('<>'*20)

#3ª forma de operação do for
for contador in range(10,0,-1):
  print(contador,end=" ")# a função end informa como os valores serão exibidos ao final, por padrâo é dado um enter(\n)