import requests
import base64
import os
import json
from dotenv import load_dotenv

# Carregar as variáveis do arquivo .env
load_dotenv()

# Obter a URL da API do .env
api_url = os.getenv('API_URL')

# Ler a imagem e codificar em base64
with open('/home/nicolas/Downloads/teste.png', 'rb') as image_file:
    image_data = base64.b64encode(image_file.read()).decode('utf-8')

# Corpo da requisição formatado corretamente com json.dumps
data = {
    'file_name': 'medina.png',
    'image': image_data
}

# Enviar a requisição para a API com o corpo JSON
response = requests.post(api_url, json=data)

# Verificar a resposta
try:
    print(response.json())
except requests.exceptions.JSONDecodeError as e:
    print("Error decoding JSON response:", e)
    print("Response text:", response.text)
