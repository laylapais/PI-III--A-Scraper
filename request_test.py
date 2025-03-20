import requests

def verificar_request():
    url = "http://nahoradocio.lowlevel.com.br/"
    
    # Definir headers, emulando um navegador
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")  # Exibe o código de status da resposta

        if response.status_code == 200:
            print("Página acessada com sucesso!")
        else:
            print(f"Falha ao acessar a página, status code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ou outro problema: {e}")

if __name__ == "__main__":
    verificar_request()
