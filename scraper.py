import requests
from bs4 import BeautifulSoup
from database import criar_tabela, salvar_filmes

criar_tabela()

base_url = "http://nahoradoocio.lowlevel.com.br/2020/06/01/16-filmes-sobre-a-luta-contra-o-racismo/"

STATUS_OK = 200

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

response = requests.get(base_url, headers=headers)

if response.status_code == STATUS_OK:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    posts = soup.find_all('iframe')
    for post in posts:
        link = post['src']
        titulo = post['title']
        
        print(f'Título: {titulo}')
        print(f'Link: {link}')
        salvar_filmes(titulo, link)
else:
    print("Falha ao acessar a página.")
