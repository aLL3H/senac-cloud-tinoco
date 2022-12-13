import requests


link = 'https://minhaAPI.alessandroda4.repl.co/ping'

requisicao = requests.get(link)

print(requisicao)
print(requisicao.json())