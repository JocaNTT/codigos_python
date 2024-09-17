animais = ['Cachorro','Gato','Jacaré','Anthony']
print(type(animais))
print(animais)

print('<=>'*20)
for itens in animais:
  print(itens, end=', ')

print()
print('<=>'*20)
animais[0] = 'Coelho'
print(animais)

print('<=>'*20)
animais.append('Cavalo')
print(animais)

print('<=>'*20)
animais.insert(1,'Camelo')
print(animais)

print('<=>'*20)
animais.pop()
print(animais)

print('<=>'*20)
animais.pop(0)
print(animais)

print('<=>'*20)
animais.remove('Camelo')
print(animais)