## Banco de dados

```
CREATE DATABASE empresa;

USE empresa;

CREATE TABLE funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    cargo VARCHAR(100),
    salario DECIMAL(10, 2)
);

select * from funcionarios;


```



Variáveis de ambiente com um arquivo `.env`. Primeiro, você precisará instalar a biblioteca `python-dotenv`, se ainda não tiver feito isso. Você pode instalar usando o seguinte comando:

```bash
pip install mysql-connector-python python-dotenv

```

### Estrutura do Projeto

1. **Crie um arquivo `.env`** no mesmo diretório do seu script `main.py`:

**`.env`:**

```plaintext
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=senha123
DB_DATABASE=empresa
```

2. **Código `main.py`:**


```python
# main.py
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class DatabaseConnection:
    def __init__(self):
        # Carrega as configurações diretamente das variáveis de ambiente
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_DATABASE')
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Conexão com o banco de dados estabelecida com sucesso.")
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexão com o banco de dados fechada.")

# Exemplo de uso
if __name__ == "__main__":
    db = DatabaseConnection()
    db.connect()
    db.close()
```

### Explicação

1. **`load_dotenv()`**: Essa função carrega as variáveis definidas no arquivo `.env` para o ambiente do Python.

2. **Uso de `os.getenv()`**: Utilizamos `os.getenv()` para acessar as variáveis de ambiente que definimos no arquivo `.env`.

### Segurança

- **Não inclua o arquivo `.env` no controle de versão (Git)**. Para isso, adicione `.env` ao seu arquivo `.gitignore`.

**`.gitignore`:**

```
# Ignorar arquivo de configuração sensível
.env
```

Agora você pode executar o seu script `main.py`, e ele deve conectar-se ao banco de dados usando as credenciais definidas no arquivo `.env`. 