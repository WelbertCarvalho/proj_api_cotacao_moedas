import requests
import json

class Data_api_extractor:
    def __init__(self):
        print("Instance of extractor object\n")

    def get_json_data(self, url):
        r = requests.get(url)
        json_data = json.loads(r.text)
        return json_data
    


cotacao_usd_brl = Data_api_extractor()

retorno = cotacao_usd_brl.get_json_data("https://economia.awesomeapi.com.br/last/USD-BRL")

print(retorno)