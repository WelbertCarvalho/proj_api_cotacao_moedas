import requests
import json

class Extrator_dados_api:
    def __init__(self):
        print("Instância do objeto de extração\n")

    def captura_dados_json(self, url):
        r = requests.get(url)
        json_data = json.loads(r.text)
        return json_data
    


cotacao_usd_brl = Extrator_dados_api()

retorno = cotacao_usd_brl.captura_dados_json("https://economia.awesomeapi.com.br/last/USD-BRL")

print(retorno)