from database import criar_tabela, salvar_filmes
import requests
from bs4 import BeautifulSoup

def raspagem():
    url = "http://nahoradoocio.lowlevel.com.br/2020/06/01/16-filmes-sobre-a-luta-contra-o-racismo/"
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')

        filmes = soup.find_all('h2')  #teste

        titulos = [filme.get_text() for filme in filmes]

        return titulos
    else:
        print("Falha ao acessar a página.")
        return []

def main():
    criar_tabela() 
    
    titulos_filmes = raspagem()  # Fazendo a raspagem em si
    if titulos_filmes:
        salvar_filmes(titulos_filmes)  
    else:
        print("Nenhum filme foi encontrado.")

if __name__ == "__main__":
    main()
