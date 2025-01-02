

### Adições à Classe `FuncionarioCRUD`

#### Método `read_all`

```python
    # Ler todos os funcionários
    def read_all(self):
```
- **`def read_all(self):`**: Define o método `read_all`, que será responsável por recuperar e exibir todos os funcionários da tabela `funcionarios`.

```python
        try:
```
- **`try:`**: Início de um bloco `try` para capturar possíveis exceções que podem ocorrer durante a execução do código.

```python
            sql = "SELECT * FROM funcionarios"
```
- **`sql = "SELECT * FROM funcionarios"`**: Define a consulta SQL que seleciona todos os registros da tabela `funcionarios`.

```python
            self.db_connection.cursor.execute(sql)
```
- **`self.db_connection.cursor.execute(sql)`**: Executa a consulta SQL usando o cursor associado à conexão do banco de dados.

```python
            results = self.db_connection.cursor.fetchall()
```
- **`results = self.db_connection.cursor.fetchall()`**: Recupera todos os resultados da consulta e os armazena na variável `results`.

```python
            if results:
                for row in results:
                    print(row)
```
- **`if results:`**: Verifica se existem resultados. Se sim, itera sobre cada linha nos resultados.
- **`print(row)`**: Exibe cada linha (registro) da tabela `funcionarios`.

```python
            else:
                print("Nenhum funcionário encontrado.")
```
- **`else:`**: Se não houver resultados, exibe uma mensagem informando que nenhum funcionário foi encontrado.

```python
        except Error as e:
            print(f"Erro ao ler funcionários: {e}")
```
- **`except Error as e:`**: Captura exceções do tipo `Error` que podem ocorrer durante a execução da consulta.
- **`print(...)`**: Exibe uma mensagem de erro se a leitura dos funcionários falhar.

### Exemplo de Uso

```python
if __name__ == "__main__":
```
- **`if __name__ == "__main__":`**: Verifica se o script está sendo executado diretamente. Se for o caso, o bloco abaixo será executado.

```python
    db = DatabaseConnection()
    db.connect()
```
- **`db = DatabaseConnection()`**: Cria uma nova instância da classe `DatabaseConnection`.
- **`db.connect()`**: Estabelece a conexão com o banco de dados chamando o método `connect`.

```python
    funcionario_crud = FuncionarioCRUD(db)
```
- **`funcionario_crud = FuncionarioCRUD(db)`**: Cria uma nova instância da classe `FuncionarioCRUD`, passando a conexão do banco de dados (`db`) como argumento.

```python
    funcionario_crud.create("Joao Silva", "Desenvolvedor", 5000.00)
```
- **`funcionario_crud.create(...)`**: Chama o método `create` para adicionar um novo funcionário com os dados fornecidos.

```python
    print("\nLista de Funcionários:")
    funcionario_crud.read_all()
```
- **`print("\nLista de Funcionários:")`**: Exibe um cabeçalho para a lista de funcionários.
- **`funcionario_crud.read_all()`**: Chama o método `read_all` para recuperar e exibir todos os funcionários cadastrados na tabela.

### Resumo das Melhorias

1. **Leitura de Funcionários**: A adição do método `read_all` permite que o programa não apenas insira dados, mas também leia e exiba todos os registros de funcionários da tabela. Isso torna o sistema mais funcional.
2. **Tratamento de Erros**: O uso do bloco `try-except` nos métodos de CRUD ajuda a lidar com exceções, garantindo que erros sejam informados ao usuário de maneira clara.
3. **Estrutura de Código**: A estrutura de classes e métodos ajuda a manter o código organizado e modular, facilitando a manutenção e futuras expansões.

