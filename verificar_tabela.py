import sqlite3

def verificar_filmes():
    conn = sqlite3.connect('scraping.db')
    c = conn.cursor()

    c.execute("SELECT * FROM filmes")
    filmes = c.fetchall()

    if filmes:
        print("Filmes encontrados no banco de dados:")
        for filme in filmes:
            print(f"{filme[0]}. {filme[1]}")
    else:
        print("Nenhum filme encontrado.")

    conn.close()

if __name__ == "__main__":
    verificar_filmes()
