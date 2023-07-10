import sys
sys.path.append("/home/welbert/projetos/airflow")

from pipelines.proj_api_cotacao_moedas.conexao_db import Conexao

class Carreg_dados():
    def __init__(self):
        print("Instância do objeto de carregamento de dados.")

    def insere_dados(self, nome_arquivo_sql: str, conexao: Conexao.conexao_sqlalchemy) -> None:
        cursor = conexao.cursor()
        conteudo_sql = self._lendo_conteudo_sql(nome_arquivo_sql)
        cursor.execute(conteudo_sql)

        cursor.close()
        conexao.close()

        return None
    
