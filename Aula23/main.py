import mysql.connector
from mysql.connector import Error

# Classe para conexão com o banco de dados
class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
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
            raise  # Re-levanta a exceção para ser tratada em outro lugar

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexão com o banco de dados fechada.")

# Classe para operações CRUD na tabela funcionarios
class FuncionarioCRUD:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    # Criar um novo funcionário
    def create(self, nome, cargo, salario):
        try:
            sql = "INSERT INTO funcionarios (nome, cargo, salario) VALUES (%s, %s, %s)"
            values = (nome, cargo, salario)
            self.db_connection.cursor.execute(sql, values)
            self.db_connection.connection.commit()
            print(f"Funcionário {nome} adicionado com sucesso.")
        except Error as e:
            print(f"Erro ao adicionar funcionário: {e}")
            self.db_connection.connection.rollback()  # Faz rollback em caso de erro

    # Ler todos os funcionários
    def read_all(self):
        try:
            sql = "SELECT * FROM funcionarios"
            self.db_connection.cursor.execute(sql)
            results = self.db_connection.cursor.fetchall()
            if results:
                for row in results:
                    print(row)
            else:
                print("Nenhum funcionário encontrado.")
        except Error as e:
            print(f"Erro ao ler funcionários: {e}")

    # Atualizar dados de um funcionário
    def update(self, funcionario_id, nome=None, cargo=None, salario=None):
        try:
            sql = "UPDATE funcionarios SET "
            fields = []
            values = []

            if nome:
                fields.append("nome = %s")
                values.append(nome)
            if cargo:
                fields.append("cargo = %s")
                values.append(cargo)
            if salario:
                fields.append("salario = %s")
                values.append(salario)

            if not fields:
                print("Nenhum campo fornecido para atualização.")
                return

            sql += ", ".join(fields)
            sql += " WHERE id = %s"
            values.append(funcionario_id)

            self.db_connection.cursor.execute(sql, tuple(values))
            self.db_connection.connection.commit()

            if self.db_connection.cursor.rowcount > 0:
                print(f"Funcionário {funcionario_id} atualizado com sucesso.")
            else:
                print(f"Funcionário com ID {funcionario_id} não encontrado.")
        except Error as e:
            print(f"Erro ao atualizar funcionário: {e}")
            self.db_connection.connection.rollback()  # Faz rollback em caso de erro

    # Deletar um funcionário
    def delete(self, funcionario_id):
        try:
            sql = "DELETE FROM funcionarios WHERE id = %s"
            self.db_connection.cursor.execute(sql, (funcionario_id,))
            self.db_connection.connection.commit()

            if self.db_connection.cursor.rowcount > 0:
                print(f"Funcionário {funcionario_id} removido com sucesso.")
            else:
                print(f"Funcionário com ID {funcionario_id} não encontrado.")
        except Error as e:
            print(f"Erro ao remover funcionário: {e}")
            self.db_connection.connection.rollback()  # Faz rollback em caso de erro

# Exemplo de uso
if __name__ == "__main__":
    # Configurações da conexão com o banco de dados
    db = DatabaseConnection(
        host="localhost",
        user="root",
        password="mentemaker",
        database="empresa"
    )

    try:
        # Conectar ao banco
        db.connect()

        # Criar uma instância do CRUD
        funcionario_crud = FuncionarioCRUD(db)

        # Operações de CRUD
        funcionario_crud.create("João Silva", "Desenvolvedor", 5000.00)
        funcionario_crud.create("Maria Souza", "Gerente", 8000.00)
        
        print("\nLista de Funcionários:")
        funcionario_crud.read_all()

        print("\nAtualizando o salário do funcionário com ID 1...")
        funcionario_crud.update(1, salario=5500.00)

        print("\nLista de Funcionários após a atualização:")
        funcionario_crud.read_all()

        print("\nDeletando o funcionário com ID 2...")
        funcionario_crud.delete(2)

        print("\nLista de Funcionários após a exclusão:")
        funcionario_crud.read_all()

    except Error as e:
        print(f"Erro na aplicação: {e}")

    finally:
        # Fechar a conexão com o banco de dados
        db.close()
