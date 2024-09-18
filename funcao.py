#Função com retorno

def soma(num1,num2):
  resultado = num1 + num2
  return resultado
num1 = int(input('Informe um valor: '))
num2 = int(input('Informe outro valor: '))
print(f'A soma de {num1} + {num2} é igual a {soma(num1,num2)}')

#Função sem retorno
def multiplica(val1,val2):
  resultado = val1 * val2
  print(f'O resultado de {val1} * {val2} é igual a {resultado}')

multiplica(20,100)