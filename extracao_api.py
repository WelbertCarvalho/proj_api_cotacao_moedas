import requests
import json
import pandas as pd

import sys
sys.path.append("/home/welbert/projetos/airflow")


class Extrator_dados_api:
    def __init__(self):
        print('Instância do objeto de extração')

    def captura_dados_json(self, url: str) -> dict:
        r = requests.get(url)
        dados_json = json.loads(r.text)
        dados_json = dict(dados_json).values()
        return dados_json
    
    def cria_df_usando_dict(self, dict_json: dict) -> pd.DataFrame:
        df = pd.DataFrame(dict_json)
        return df
    


if __name__ == '__main__':
    from pipelines.proj_api_cotacao_moedas.conexao_db import Conexao
    datalake = Conexao()
    datalake_con = datalake.conexao_sqlalchemy(
    'datalake',
    'mysql+pymysql'
    )

    extrator = Extrator_dados_api()
    dados_cot_diaria = extrator.captura_dados_json('https://economia.awesomeapi.com.br/last/USD-BRL')
    print(dados_cot_diaria)
    print(type(dados_cot_diaria))

    df = extrator.cria_df_usando_dict(dados_cot_diaria)

    print(df.head())