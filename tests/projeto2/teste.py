import requests

resposta = requests.get("https://www.google.com")
print(resposta.status_code)