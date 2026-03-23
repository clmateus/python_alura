import sqlite3

# connect - Estabelece uma conexão com o banco de dados especificado. Caso ele não exista, cria o banco de dados.
conn = sqlite3.connect('escola.db')
# cursor - Cria um objeto "cursor". Ele atua como um "apontador" e é através dele que enviamos e executamos os comandos SQL no banco.
cursor = conn.cursor()

# execute - Método que executa um comando SQL.
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER
)
""")

cursor.execute(
    "INSERT INTO estudantes (nome, idade)" \
    "VALUES (?, ?)", ("João", 20)
)

# commit - Método que confirma e salva as alterações feitas no banco de dados. Sem esse comando, a inserção de dados seria descartada ao fechar a conexão.
conn.commit()

cursor.execute("SELECT * FROM estudantes")
# fetchall - Método que recupera todas as linhas do resultado da consulta (SELECT) anterior em formato de lista.
print(cursor.fetchall())

# close - Fecha a conexão com o banco de dados. É uma boa prática sempre fechar a conexão para evitar consumo indevido de recursos.
conn.close()