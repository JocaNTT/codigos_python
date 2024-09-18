pessoa = {
  'Nome':'Joaquim',
  'Idade': 17,
  'Cidade':'Caratinga'
}
print(pessoa)
print('<=>'*20)

#Exibe a chave
print(pessoa.keys())

#Exibe os valores
print(pessoa.values())

#Exibe a chave e o valor
print(pessoa.items())

print('<=>'*20)
for chave,valor in pessoa.items():
  print(f'{chave} : {valor}')

#Operações
#1ª forma adicionando dados
pessoa['Peso'] = 62
print(pessoa)
print('<=>'*20)

#2ª forma adicionando dados
pessoa.update({'Profissão':'Progamador'})
print()
print('<=>'*20)

#1ª forma removendo dados
pessoa.pop('Peso')
print(pessoa)
print('<=>'*20)

#2ª forma removendo dados
del(pessoa['Cidade'])
print(pessoa)