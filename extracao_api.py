import requests
import json
import pandas as pd


class Extrator_dados_api:
    def __init__(self):
        print("Instância do objeto de extração\n")

    def captura_dados_json(self, url):
        r = requests.get(url)
        dados_json = json.loads(r.text)
        dados_json = dados_json.values()
        return dados_json
    
    def cria_df_usando_dict(self, dict_json):
        df = pd.DataFrame(dict_json)
        return df






