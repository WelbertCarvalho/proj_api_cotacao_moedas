import requests
import json

class Extrator_dados_api:
    def __init__(self):
        print("Instância do objeto de extração\n")

    def get_json_data(self, url):
        r = requests.get(url)
        json_data = json.loads(r.text)
        return json_data
    


cotacao_usd_brl = Extrator_dados_api()

retorno = cotacao_usd_brl.get_json_data("https://economia.awesomeapi.com.br/last/USD-BRL")

print(retorno)