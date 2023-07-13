import sys
sys.path.append("/home/welbert/projetos/airflow")

from sqlalchemy import create_engine
from pipelines.proj_api_cotacao_moedas.extracao import Extrator_dados

class Carreg_dados():
    def __init__(self):
        print("Instância do objeto de carregamento de dados.")

    @staticmethod
    def insere_dados(caminho_do_arquivo: str, nome_arquivo_sql: str, dados_a_inserir: list, conexao: create_engine) -> None:
        cursor = conexao.cursor()
        conteudo_sql = Extrator_dados.lendo_conteudo_sql(
            caminho_do_arquivo = caminho_do_arquivo,
            nome_arquivo_sql = nome_arquivo_sql
            )
        try:
            cursor.execute(conteudo_sql, dados_a_inserir)
            conexao.commit()
        except:
            print('Erro de carregamento de dados.')

        cursor.close()
        conexao.close()

        return None
    
