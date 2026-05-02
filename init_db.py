import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    categoria TEXT,
    resumo TEXT,
    conteudo TEXT,
    imagem TEXT,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Tabela criada com sucesso!")