

### Importações e Carregamento de Variáveis de Ambiente

```python
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
```
- **`import mysql.connector`**: Importa a biblioteca que permite a conexão e interação com bancos de dados MySQL.
- **`from mysql.connector import Error`**: Importa a classe `Error` para tratar exceções relacionadas ao MySQL.
- **`import os`**: Importa o módulo `os` para interagir com variáveis de ambiente do sistema operacional.
- **`from dotenv import load_dotenv`**: Importa a função `load_dotenv`, que carrega variáveis de ambiente a partir de um arquivo `.env`.

```python
load_dotenv()
```
- **`load_dotenv()`**: Carrega as variáveis definidas no arquivo `.env` para que possam ser acessadas pelo programa.

### Classe `DatabaseConnection`

```python
class DatabaseConnection:
```
- **`class DatabaseConnection`**: Define a classe `DatabaseConnection`, que gerenciará a conexão com o banco de dados.

```python
    def __init__(self):
```
- **`def __init__(self):`**: Método construtor da classe, chamado ao criar uma nova instância da classe.

```python
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_DATABASE')
```
- **`self.host = os.getenv('DB_HOST')`**: Obtém o valor da variável de ambiente `DB_HOST` e o armazena na instância como `self.host`.
- **`self.user`, `self.password`, `self.database`**: Faz o mesmo para as outras configurações de conexão.

```python
        self.connection = None
        self.cursor = None
```
- **`self.connection = None`**: Inicializa `self.connection` como `None`. Isso será usado para armazenar a conexão com o banco de dados.
- **`self.cursor = None`**: Inicializa `self.cursor` como `None`. Isso será usado para executar comandos SQL.

### Método de Conexão

```python
    def connect(self):
```
- **`def connect(self):`**: Define o método `connect`, que tentará estabelecer uma conexão com o banco de dados.

```python
        try:
```
- **`try:`**: Início de um bloco `try` para capturar possíveis exceções.

```python
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
```
- **`self.connection = mysql.connector.connect(...)`**: Tenta estabelecer uma conexão com o banco de dados MySQL usando as credenciais armazenadas.

```python
            self.cursor = self.connection.cursor()
```
- **`self.cursor = self.connection.cursor()`**: Cria um cursor que será usado para executar comandos SQL.

```python
            print("Conexao com o banco de dados estabelecida com sucesso.")
```
- **`print(...)`**: Exibe uma mensagem confirmando que a conexão foi bem-sucedida.

```python
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
```
- **`except Error as e:`**: Captura exceções do tipo `Error`.
- **`print(...)`**: Exibe a mensagem de erro se a conexão falhar.

### Método de Fechamento

```python
    def close(self):
```
- **`def close(self):`**: Define o método `close`, que fechará a conexão com o banco de dados.

```python
        if self.cursor:
            self.cursor.close()
```
- **`if self.cursor:`**: Verifica se o cursor foi criado.
- **`self.cursor.close()`**: Fecha o cursor, se ele existir.

```python
        if self.connection:
            self.connection.close()
```
- **`if self.connection:`**: Verifica se a conexão foi estabelecida.
- **`self.connection.close()`**: Fecha a conexão com o banco de dados, se existir.

```python
        print("Conexao com o banco de dados fechada.")
```
- **`print(...)`**: Exibe uma mensagem confirmando que a conexão foi fechada.

### Classe `FuncionarioCRUD`

```python
class FuncionarioCRUD:
```
- **`class FuncionarioCRUD`**: Define a classe `FuncionarioCRUD`, que gerenciará as operações de CRUD (Criar, Ler, Atualizar, Deletar) para a tabela `funcionarios`.

```python
    def __init__(self, db_connection):
```
- **`def __init__(self, db_connection):`**: Método construtor que recebe uma instância da classe `DatabaseConnection`.

```python
        self.db_connection = db_connection
```
- **`self.db_connection = db_connection`**: Armazena a instância de `DatabaseConnection` na classe `FuncionarioCRUD`.

### Método de Criação

```python
    def create(self, nome, cargo, salario):
```
- **`def create(self, nome, cargo, salario):`**: Define o método `create`, que adicionará um novo funcionário à tabela.

```python
        try:
```
- **`try:`**: Início de um bloco `try` para capturar possíveis exceções.

```python
            sql = "INSERT INTO funcionarios (nome, cargo, salario) VALUES (%s, %s, %s)"
```
- **`sql = ...`**: Define a consulta SQL para inserir um novo funcionário, usando placeholders `%s`.

```python
            values = (nome, cargo, salario)
```
- **`values = (nome, cargo, salario)`**: Armazena os valores a serem inseridos na tabela.

```python
            self.db_connection.cursor.execute(sql, values)
```
- **`self.db_connection.cursor.execute(...)`**: Executa a consulta SQL com os valores fornecidos.

```python
            self.db_connection.connection.commit()
```
- **`self.db_connection.connection.commit()`**: Confirma a transação, salvando as mudanças no banco de dados.

```python
            print(f"Funcionario {nome} adicionado com sucesso.")
```
- **`print(...)`**: Exibe uma mensagem confirmando que o funcionário foi adicionado com sucesso.

```python
        except Error as e:
            print(f"Erro ao adicionar funcionario: {e}")
            self.db_connection.connection.rollback()  # Faz rollback em caso de erro
```
- **`except Error as e:`**: Captura exceções do tipo `Error`.
- **`print(...)`**: Exibe uma mensagem de erro se a inserção falhar.
- **`self.db_connection.connection.rollback()`**: Reverte a transação em caso de erro, evitando alterações parciais no banco de dados.

### Exemplo de Uso

```python
if __name__ == "__main__":
```
- **`if __name__ == "__main__":`**: Verifica se o script está sendo executado diretamente (não importado como um módulo).

```python
    db = DatabaseConnection()
    db.connect()
```
- **`db = DatabaseConnection()`**: Cria uma nova instância de `DatabaseConnection`.
- **`db.connect()`**: Chama o método `connect` para estabelecer a conexão com o banco de dados.

```python
    funcionario_crud = FuncionarioCRUD(db)
```
- **`funcionario_crud = FuncionarioCRUD(db)`**: Cria uma nova instância da classe `FuncionarioCRUD`, passando a conexão do banco de dados.

```python
    funcionario_crud.create("Joao Silva", "Desenvolvedor", 5000.00)
```
- **`funcionario_crud.create(...)`**: Chama o método `create` para adicionar um novo funcionário com os dados fornecidos.

