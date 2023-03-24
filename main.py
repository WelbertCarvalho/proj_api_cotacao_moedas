from extracao_api import Extrator_dados_api
from conexao_db import Conexao


cotacao_usd_brl = Extrator_dados_api()
retorno = cotacao_usd_brl.captura_dados_json('https://economia.awesomeapi.com.br/last/USD-BRL')
print(retorno)

df = cotacao_usd_brl.cria_df_usando_dict(retorno)
print(df)

datalake = Conexao()
datalake_con = datalake.conexao_sqlalchemy(
    'datalake',
    'mysql+pymysql'
)

print(datalake_con)

datalake.criar_tabela(
    df = df,
    nome_tabela = 'cotacao_usd_brl',
    conexao = datalake_con,
    modo = 'append'
)

