Vamos construir um código em Python que evolui gradualmente para ilustrar conceitos de Programação Orientada a Objetos (POO). Começaremos com um exemplo simples e vamos adicionando complexidade à medida que introduzimos novos conceitos.

### 1. Código Inicial: Classes e Objetos Simples

Vamos começar com um exemplo básico de uma classe e objetos. Suponha que estamos modelando um conceito simples: um "Livro".

```python
# Definindo a classe Livro
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def mostrar_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")

# Criando instâncias da classe Livro
livro1 = Livro("1984", "George Orwell", 1949)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

# Usando o método mostrar_informacoes
livro1.mostrar_informacoes()
livro2.mostrar_informacoes()
```

### 2. Adicionando Encapsulamento

Agora, vamos adicionar encapsulamento para proteger os atributos de serem modificados diretamente. Vamos adicionar métodos para acessar e modificar o título do livro.

```python
# Definindo a classe Livro com encapsulamento
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.__titulo = titulo  # Atributo privado
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def mostrar_informacoes(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

# Criando instâncias da classe Livro
livro1 = Livro("1984", "George Orwell", 1949)

# Modificando o título usando o método setter
livro1.set_titulo("1984 - Edição Especial")
livro1.mostrar_informacoes()
```

### 3. Introduzindo Herança

Vamos criar uma subclasse chamada `LivroDigital` que herda de `Livro` e adiciona um novo atributo para o formato digital.

```python
# 1 Definindo a classe Livro com encapsulamento
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.__titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def mostrar_informacoes(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

# Definindo a subclasse LivroDigital
class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano_publicacao, formato):
        super().__init__(titulo, autor, ano_publicacao)
        self.formato = formato

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Formato: {self.formato}")

# Criando instâncias das classes
livro_digital = LivroDigital("Fundação", "Isaac Asimov", 1951, "EPUB")

# Usando o método mostrar_informacoes da subclasse
livro_digital.mostrar_informacoes()
```

### 4. Adicionando Polimorfismo

Vamos introduzir polimorfismo criando um método `resumir` que terá uma implementação diferente para `Livro` e `LivroDigital`.

```python
# Definindo a classe Livro com encapsulamento
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.__titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def mostrar_informacoes(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")

    def resumir(self):
        return f"{self.__titulo} - {self.autor} ({self.ano_publicacao})"

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

class LivroDigital(Livro):
    def __init__(self, titulo, autor, ano_publicacao, formato):
        super().__init__(titulo, autor, ano_publicacao)
        self.formato = formato

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Formato: {self.formato}")

    def resumir(self):
        return f"{self.__titulo} - {self.autor} ({self.ano_publicacao}) - Formato: {self.formato}"

# Função para imprimir resumo de livro
def imprimir_resumo(livro):
    print(livro.resumir())

# Criando instâncias das classes
livro_fisico = Livro("1984", "George Orwell", 1949)
livro_digital = LivroDigital("Fundação", "Isaac Asimov", 1951, "EPUB")

# Usando a função imprimir_resumo
imprimir_resumo(livro_fisico)
imprimir_resumo(livro_digital)
```

### Resumo da Evolução do Código

1. **Código Inicial**: Definimos uma classe simples (`Livro`) e criamos objetos.
2. **Encapsulamento**: Adicionamos encapsulamento para proteger atributos e fornecer métodos de acesso.
3. **Herança**: Introduzimos herança com uma subclasse (`LivroDigital`) que adiciona novos atributos e métodos.
4. **Polimorfismo**: Implementamos polimorfismo com métodos que têm comportamentos diferentes nas subclasses, usando o mesmo nome (`resumir`).

Cada etapa construiu sobre a anterior, ilustrando como conceitos de POO podem ser aplicados e expandidos para criar soluções mais robustas e organizadas.