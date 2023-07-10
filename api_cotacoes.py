import sys
sys.path.append("/home/welbert/projetos/airflow")

from pipelines.proj_api_cotacao_moedas.extracao import Extrator_dados
from pipelines.proj_api_cotacao_moedas.conexao_db import Conexao


def extrai_cotacao_diaria(origem: str, destino: str) -> None:
    cotacao_usd_brl = Extrator_dados()
    retorno = cotacao_usd_brl.captura_dados_json(f'https://economia.awesomeapi.com.br/last/{origem}-{destino}')
    campos = ['code', 'codein', 'name', 'high', 'low', 'varBid', 'pctChange', 'bid', 'ask', 'create_date']
    retorno_filtrado = {chave: valor for chave, valor in retorno[f"{origem}{destino}"].items() if chave in campos}
    print(retorno_filtrado)

    datalake = Conexao()
    datalake_con = datalake.conexao_sqlalchemy(
        'datalake',
        'mysql+pymysql'
    )
    print(datalake_con)



    return None


if __name__ == '__main__':
    captura = extrai_cotacao_diaria(origem = 'USD', destino = 'BRL')

