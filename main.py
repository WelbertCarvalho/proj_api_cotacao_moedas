from extracao_api import Extrator_dados_api
from conexao_db import Conexao


cotacao_usd_brl = Extrator_dados_api()
retorno = cotacao_usd_brl.captura_dados_json('https://economia.awesomeapi.com.br/last/USD-BRL')
print(retorno)

df = cotacao_usd_brl.cria_df_usando_dict(retorno)
print(df)

datalake_con = Conexao()
datalake = datalake_con.sqlalchemy_conn(
    'datalake',
    'mysql+pymysql'
)

print(datalake)


# Criar lógica para create table com base nos dados do dataframe caso a tabela não exista
# Nesta mesma lógica, caso a tabela exista, criar mecanismo que impeça a entrada de dados duplicados com base no campo create_date