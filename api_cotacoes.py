import sys
sys.path.append("/home/welbert/projetos/airflow")

import datetime as dt

from pipelines.proj_api_cotacao_moedas.extracao import Extrator_dados
from pipelines.proj_api_cotacao_moedas.conexao_db import Conexao
from pipelines.proj_api_cotacao_moedas.carregamento import Carreg_dados


def extrai_cotacao_diaria(url: str, origem: str, destino: str, nome_sql_arq: str) -> None:
    cotacao = Extrator_dados()
    retorno = cotacao.captura_dados_json(url = url)
    campos = ['code', 'codein', 'name', 'high', 'low', 'varBid', 'pctChange', 'bid', 'ask', 'create_date']
    # Retorna uma lista filtrando os valores com base nas chaves existentes na lista campos
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
        nome_arquivo_sql = nome_sql_arq,
        dados_a_inserir = retorno_convertido,
        conexao = datalake_con
        )

    return None


def extrai_cotacao_num_dias(url: str, num_dias: int, nome_sql_arq: str) -> None:
    cotacao = Extrator_dados()
    retorno = cotacao.captura_dados_json(url = f"{url}/{num_dias}")
    campos_convert_float = ['high', 'low', 'varBid', 'pctChange', 'bid', 'ask']
    campos = ['code', 'codein', 'name', 'high', 'low', 'varBid', 'pctChange', 'bid', 'ask', 'create_date']
    dict_dados_base = {'code': '', 'codein': '', 'name': ''}
    dict_iter = {}
    lista_de_dict_dados_completos = []
    for index, valor in enumerate(retorno):
        if index == 0:
            dict_dados_base['code'] = valor['code']
            dict_dados_base['codein'] = valor['codein']
            dict_dados_base['name'] = valor['name']
            dict_iter = {**dict_dados_base, **valor}
            
            for campo in campos_convert_float:
                dict_iter[campo] = float(dict_iter[campo])
            
            lista_de_dict_dados_completos.append(dict_iter)
        else:
            dict_iter = {**dict_dados_base, **valor}
            dict_iter['create_date'] = dt.datetime.fromtimestamp(int(valor['timestamp'])).strftime('%Y-%m-%d %H:%M:%S')

            for campo in campos_convert_float:
                dict_iter[campo] = float(dict_iter[campo])

            lista_de_dict_dados_completos.append(dict_iter)

    
    for dicionario in lista_de_dict_dados_completos:
        # Retorna uma lista filtrando os valores com base nas chaves existentes na lista campos
        dados_a_inserir = list({chave: valor for chave, valor in dicionario.items() if chave in campos}.values())
  
        datalake = Conexao()
        datalake_con = datalake.conexao_sqlalchemy(
            'datalake',
            'mysql+pymysql'
        )

        Carreg_dados.insere_dados(
            caminho_do_arquivo = "/home/welbert/projetos/airflow/pipelines/proj_api_cotacao_moedas/sql",
            nome_arquivo_sql = nome_sql_arq,
            dados_a_inserir = dados_a_inserir,
            conexao = datalake_con
            )

    return None


if __name__ == '__main__':
    # captura_btc = extrai_cotacao_diaria(url = 'https://economia.awesomeapi.com.br/last/BTC-BRL', origem = 'BTC', destino = 'BRL', nome_sql_arq = 'insert_dados_cotacao_diaria_btc')
    captura_btc = extrai_cotacao_num_dias(url = 'https://economia.awesomeapi.com.br/json/daily/BTC-BRL', num_dias = '10', nome_sql_arq = 'insert_dados_cotacao_diaria_btc')

