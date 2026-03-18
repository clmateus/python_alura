livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for i in livros:
    # if i["estoque"] > 0:
    #     print(f"Livro disponível: {i['nome']}")
    if i["estoque"] == 0:
        continue
    print(f"Livro disponível: {i['nome']}")