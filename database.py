import sqlite3

# Para criar a conexão com o banco de dados
def criar_conexao():
    conn = sqlite3.connect('filmes.db')
    return conn

# Para criar a tabela 
def criar_tabela():
    conn = criar_conexao()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS filmes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    link TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Para salvar o filme no banco de dados
def salvar_filmes(titulo, link):
    conn = criar_conexao()
    c = conn.cursor()
    c.execute("INSERT INTO filmes (titulo, link) VALUES (?, ?)", (titulo, link))
    conn.commit()
    conn.close()
    print(f"Filme '{titulo}' salvo com sucesso!")


