import sys
sys.path.append("/home/welbert/projetos/airflow")

from pipelines.proj_api_cotacao_moedas.extracao import Extrator_dados
from pipelines.proj_api_cotacao_moedas.conexao_db import Conexao
from pipelines.proj_api_cotacao_moedas.carregamento import Carreg_dados


def extrai_cotacao_diaria(origem: str, destino: str) -> None:
    cotacao_usd_brl = Extrator_dados()
    retorno = cotacao_usd_brl.captura_dados_json(f'https://economia.awesomeapi.com.br/last/{origem}-{destino}')
    campos = ['code', 'codein', 'name', 'high', 'low', 'varBid', 'pctChange', 'bid', 'ask', 'create_date']
    retorno_filtrado = list({chave: valor for chave, valor in retorno[f"{origem}{destino}"].items() if chave in campos}.values())
    retorno_convertido = []

    for item in retorno_filtrado:
        try:
            retorno_convertido.append(float(item))
        except ValueError:
            retorno_convertido.append(item)

    print(retorno_convertido)
    print(type(retorno_convertido))
    datalake = Conexao()
    datalake_con = datalake.conexao_sqlalchemy(
        'datalake',
        'mysql+pymysql'
    )
    print(datalake_con)

    Carreg_dados.insere_dados(
        caminho_do_arquivo = "/home/welbert/projetos/airflow/pipelines/proj_api_cotacao_moedas/sql",
        nome_arquivo_sql = 'insert_dados_cotacao_diaria',
        dados_a_inserir = retorno_convertido,
        conexao = datalake_con
        )

    return None


if __name__ == '__main__':
    captura = extrai_cotacao_diaria(origem = 'USD', destino = 'BRL')

