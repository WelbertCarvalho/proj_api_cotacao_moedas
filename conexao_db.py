from sqlalchemy import create_engine
from config import conexoes as c

class Conexao:
    def __init__(self):
        print("Instância do objeto de conexão com DB\n")

    def sqlalchemy_conn(self, nome_database, tipo_conexao):
        user = c[nome_database]["user"]
        password = c[nome_database]["password"]
        host = c[nome_database]["host"]
        port = c[nome_database]["port"]
        database = c[nome_database]["database"]

        url = f"{tipo_conexao}://{user}:{password}@{host}:{port}/{database}"

        con = create_engine(
            url = url
        )
        
        print(f"Connection stablished: {nome_database}")
        return con