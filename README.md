# Captura de dados de cotação monetária com API

Projeto para captura de cotação de moedas através da API AwesomeAPI. Acesse para mais informações na documentação oficial da API: https://docs.awesomeapi.com.br/api-de-moedas
Podem ser escolhidos parâmetros como moeda origem/destino e período de extração.

## Estrutura do projeto
- Orientação a objetos com python3
- Este pipeline é utilizado em integração com o airflow versão 2.6.2
- O ideal é que seja criado um ambiente virtual contendo a versão informada do airflow (python venv)
- Há módulos separados por finalidade contendo atividades de engenharia de dados
- Uma observação importante é que no módulo de conexão existe um arquivo chamado config.py. Neste arquivo deve haver um dicionário chamado connections. Neste dicionário, a chave é o nome do database que você deseja conectar e o valor será um outro dicionário interno contendo os dados de conexão deste database sendo user, password, host, port e database.

## Módulos

### Extração API (extracao_api.py)
Este módulo dispõe de uma classe que contém um método que realiza a extração de dados de uma API recebendo uma URL e retornando um dicionário python. Também contém um método que cria um pd.DataFrame recebendo um dicionário. 

### Conexão (conexao_db.py)
O módulo de conexão contém a declaração de uma classe que dispõe de um método para armazenar um objeto de conexão SQLAlchemy, além de um método chamado criar_tabela que recebe um objeto pd.DataFrame, o nome da tabela, uma conexão SQLAlchemy e um modo: 'fail', 'replace', 'append'. Este método cria uma tabela ou adiciona dados a uma tabela já existente no banco de dados informado.

### Main (main.py)
Este é o script que contém os objetos instanciados e o exemplo de API para realizar a extração além de o carregamento dos dados em um banco MySQL de exemplo.

### Requirements (requirements.txt - com bibliotecas para instalação do Airflow)
Este é o arquivo padrão gerado pelo comando pip freeze. Este arquivo deve ser utilizado para que realizar a instação de todas as bibliotecas necessárias para a utilização do projeto.

Para instalar as bibliotecas necessárias:
`pip install -r requirements.txt` 