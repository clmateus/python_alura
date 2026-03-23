import sqlite3

conn = sqlite3.connect("escola.db")
cursor = conn.cursor()

cursor.execute("""SELECT * FROM estudantes WHERE id = 1""")
print(cursor.fetchall())

cursor.execute("""SELECT estudantes.nome, disciplinas.nome_disciplina FROM disciplinas JOIN estudantes ON disciplinas.estudante_id""")
print(cursor.fetchall())