despensa = ['açúcar', 'banana']

item = input('Digite o item que você quer verificar: ')

if item in despensa:
    print(f'O item {item} não precisa ser comprado.')
else:
    print(f'O item {item} precisa ser comprado.')