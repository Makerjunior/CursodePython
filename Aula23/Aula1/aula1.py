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
            print("Conexao com o banco de dados estabelecida com sucesso.")
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexao com o banco de dados fechada.")

# Exemplo de uso
if __name__ == "__main__":
    db = DatabaseConnection()
    db.connect()
    db.close()
