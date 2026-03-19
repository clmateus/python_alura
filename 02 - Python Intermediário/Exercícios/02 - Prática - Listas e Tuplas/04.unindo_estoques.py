estoque1 = tuple(input('Digite os produtos do estoque 1 separados por vírgula: ').split(','))
estoque2 = tuple(input('Digite os produtos do estoque 2 separados por vírgula: ').split(','))
estoque_combinado = estoque1 + estoque2

print(f'Produtos do estoque 1: {estoque1}')
print(f'Produtos do estoque 2: {estoque2}')
print(f'Estoque combinado: {estoque_combinado}')