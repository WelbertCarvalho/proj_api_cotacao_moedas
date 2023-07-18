# Captura de dados de cotação monetária com API

Projeto para captura de cotação de moedas através da API AwesomeAPI. Acesse para mais informações na documentação oficial da API: https://docs.awesomeapi.com.br/api-de-moedas
Podem ser escolhidos parâmetros como moeda origem/destino e período de extração.

## Estrutura do projeto
- Orientação a objetos com python3
- Este pipeline é utilizado em integração com o airflow versão 2.6.2
- O ideal é que seja criado um ambiente virtual contendo a versão informada do airflow (python venv)
- Há classes separadas por finalidade contendo atividades de engenharia de dados
- Uma observação importante é que na classe de conexão é importado um arquivo chamado config.py. Neste arquivo deve haver um dicionário chamado connections. Neste dicionário, a chave é o nome da database que você deseja conectar e o valor será um outro dicionário interno contendo os dados de conexão deste database sendo user, password, host, port e database.

## Classes

### Conexão a bancos de dados (conexao_db.py)
A classe de conexão contém um método para armazenar um objeto de conexão SQLAlchemy. É possível realizar conexão em diversos tipos de bancos de dados.

### Extração de dados via API ou leitura de scripts SQL (extracao.py)
Esta classe contém métodos que realizam a extração de dados via API e também realizando a leitura de scripts SQL. 

### Carregamento (carregamento.py)
Nesta classe, há um método para realizar a inserção de dados realizando a leitura de um script sql e tendo também uma conexão SQLAlchemy.

### Instanciando os métodos das classes do projeto (api_cotacoes.py)
Este é o script que contém os objetos instanciados e o exemplo de API para realizar a extração além de o carregamento dos dados em um banco MySQL de exemplo.
São 2 funções que são chamadas pelas DAGs do airflow com o objetivo de inserir os dados na tabela do banco. Uma das funções carrega os dados do dia e a outra carrega os dados de um período a contar do dia de hoje passando um número de dias retroativos.

### Requirements (requirements.txt - com bibliotecas para instalação do Airflow)
Este é o arquivo padrão gerado pelo comando pip freeze. Este arquivo deve ser utilizado para que realizar a instação de todas as bibliotecas necessárias para a utilização do projeto.

Para instalar as bibliotecas necessárias:
`pip install -r requirements.txt`