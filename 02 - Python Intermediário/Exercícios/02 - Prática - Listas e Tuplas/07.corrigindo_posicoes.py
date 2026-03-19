lista = ['João', 'Maria', 'Jozé']

nome_incorreto = input('Digite o nome incorreto: ')
lista.remove(nome_incorreto)

nome_correto = input('Digite o nome correto: ')
lista.append(nome_correto)

print(f'O nome {nome_incorreto} foi substituído por {nome_correto}')
print(f'Lista atualizada: {lista}')