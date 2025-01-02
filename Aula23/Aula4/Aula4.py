# main.py
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Carrega as variaveis de ambiente do arquivo .env
load_dotenv()

class DatabaseConnection:
    def __init__(self):
        # Carrega as configurações diretamente das variaveis de ambiente
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
            print("Conexao com o banco de dados estabelecida com sucesso.")
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            raise  # Re-levanta a exceçao para ser tratada em outro lugar

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexao com o banco de dados fechada.")
     
     
     
     
     
# Classe para operações CRUD na tabela funcionarios
class FuncionarioCRUD:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # Criar um novo funcionario
    def create(self, nome, cargo, salario):
        try:
            sql = "INSERT INTO funcionarios (nome, cargo, salario) VALUES (%s, %s, %s)"
            values = (nome, cargo, salario)
            self.db_connection.cursor.execute(sql, values)
            self.db_connection.connection.commit()
            print(f"Funcionario {nome} adicionado com sucesso.")
        except Error as e:
            print(f"Erro ao adicionar funcionario: {e}")
            self.db_connection.connection.rollback()  # Faz rollback em caso de erro  
            
        # Ler todos os funcionarios
    def read_all(self):
        try:
            sql = "SELECT * FROM funcionarios"
            self.db_connection.cursor.execute(sql)
            results = self.db_connection.cursor.fetchall()
            if results:
                for row in results:
                    print(row)
            else:
                print("Nenhum funcionario encontrado.")
        except Error as e:
            print(f"Erro ao ler funcionarios: {e}")              

        # Deletar um funcionario
    def delete(self, funcionario_id):
        try:
            sql = "DELETE FROM funcionarios WHERE id = %s"
            self.db_connection.cursor.execute(sql, (funcionario_id,))
            self.db_connection.connection.commit()

            if self.db_connection.cursor.rowcount > 0:
                print(f"Funcionario {funcionario_id} removido com sucesso.")
            else:
                print(f"Funcionario com ID {funcionario_id} nao encontrado.")
        except Error as e:
            print(f"Erro ao remover funcionario: {e}")
            self.db_connection.connection.rollback()

# Exemplo de uso
if __name__ == "__main__":
    # Conectar ao banco
    db = DatabaseConnection()
    db.connect()

    # Criar uma instância do CRUD
    funcionario_crud = FuncionarioCRUD(db)

    # Operações de CRUD
    funcionario_crud.create("Joao Silva", "Desenvolvedor", 5000.00)
    
    
    print("\nDeletando o funcionario com ID 5...")
    funcionario_crud.delete(5)
    
    print("\nLista de Funcionarios:")
    funcionario_crud.read_all()