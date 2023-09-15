import requests
import json
import pandas as pd

import sys
sys.path.append("/home/welbert/projetos/airflow")
from pipelines.proj_api_cotacao_moedas.conexao_db import Conexao


class Extrator_dados:
    def __init__(self):
        print('Instância do objeto de extração')

    def captura_dados_json(self, url: str) -> dict:
        r = requests.get(url)
        dados_json = json.loads(r.text)
        return dados_json
    
    @staticmethod
    def lendo_conteudo_sql(caminho_do_arquivo: str, nome_arquivo_sql: str) -> str:
        arquivo_sql = open(f'{caminho_do_arquivo}/{nome_arquivo_sql}.sql', 'r')
        conteudo_sql = arquivo_sql.read()
        arquivo_sql.close()
        return conteudo_sql
    
    def cria_df_lendo_sql_sem_param(self, nome_arquivo_sql: str, conexao: Conexao.conexao_sqlalchemy) -> pd.DataFrame:
        conteudo_sql = self.lendo_conteudo_sql(nome_arquivo_sql)
        df = pd.read_sql_query(conteudo_sql, conexao)
        conexao.close()
        return df

    def cria_df_usando_dict(self, dict_json: dict) -> pd.DataFrame:
        df = pd.DataFrame(dict_json)
        return df

if __name__ == '__main__':
    datalake = Conexao()
    datalake_con = datalake.conexao_sqlalchemy(
    'datalake',
    'mysql+pymysql'
    )

    extrator = Extrator_dados()
    dados_cot_diaria = extrator.captura_dados_json('https://economia.awesomeapi.com.br/last/USD-BRL')
    dict_cot_diaria = dados_cot_diaria.values()

    print(dict_cot_diaria)

    df = extrator.cria_df_usando_dict(dict_cot_diaria)

    print(df.head())
    