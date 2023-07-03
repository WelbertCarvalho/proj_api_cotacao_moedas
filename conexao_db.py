import sys
sys.path.append("/home/welbert/projetos/airflow")

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
import pandas as pd
from typing import Literal
from pipelines.proj_api_cotacao_moedas.config import connections as c

class Conexao:
    def __init__(self):
        print('Instância do objeto de conexão com DB')

    def conexao_sqlalchemy(self, nome_database: str, tipo_conexao: str) -> create_engine:
        user = c[nome_database]['user']
        password = c[nome_database]['password']
        host = c[nome_database]['host']
        port = c[nome_database]['port']
        database = c[nome_database]['database']

        url = f'{tipo_conexao}://{user}:{password}@{host}:{port}/{database}'

        con = create_engine(
            url = url
        )
        
        print(f'Conexão estabelecida: {nome_database}')
        return con
    
    def criar_tabela(
            self, df: pd.DataFrame, 
            nome_tabela: str, 
            conexao: Engine, 
            modo: Literal['fail', 'replace', 'append'] = 'append') -> None:
        
        df.to_sql(
            name = nome_tabela,
            con = conexao,
            if_exists = modo,
            index = False
        )

        print(f'A tabela {nome_tabela} foi criada no modo {modo}')


if __name__ == '__main__':
    print(c["datalake"])
    datalake = Conexao()
    datalake_con = datalake.conexao_sqlalchemy(
    'datalake',
    'mysql+pymysql'
    )
    
    print(datalake_con)

    