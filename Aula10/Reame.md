**Tutorial sobre Funções em Python**

Uma função é um bloco de código reutilizável que executa uma tarefa específica. Em Python, as funções são definidas usando a palavra-chave `def`. Vamos criar um tutorial passo a passo para entender como trabalhar com funções em Python.

### 1. Definindo uma Função

Para criar uma função, use a palavra-chave `def`, seguida pelo nome da função e parênteses que podem conter parâmetros. O bloco de código da função é indentado abaixo do cabeçalho da função.

```python
def saudacao(nome):
    """Esta função saúda a pessoa com o nome fornecido."""
    print(f"Olá, {nome}!")

# Chamando a função
saudacao("Alice")
```

### 2. Parâmetros e Argumentos

Uma função pode ter parâmetros, que são variáveis usadas na definição da função, e argumentos, que são os valores reais passados para a função quando ela é chamada.

```python
def soma(a, b):
    """Esta função retorna a soma de dois números."""
    resultado = a + b
    return resultado

# Chamando a função
resultado_soma = soma(3, 5)
print(f"A soma é: {resultado_soma}")
```

### 3. Valor Padrão dos Parâmetros

Você pode fornecer valores padrão para os parâmetros, tornando-os opcionais ao chamar a função.

```python
def saudacao(nome, saudacao="Olá"):
    """Esta função saúda a pessoa com a saudação e o nome fornecidos."""
    print(f"{saudacao}, {nome}!")

# Chamando a função
saudacao("Bob")  # Usará a saudação padrão
saudacao("Alice", "Oi")  # Usará a saudação fornecida
```

### 4. Retorno de Valor

As funções podem retornar valores usando a palavra-chave `return`. Isso permite que você use o resultado da função em outras partes do seu código.

```python
def quadrado(numero):
    """Esta função retorna o quadrado do número fornecido."""
    return numero ** 2

# Chamando a função
resultado_quadrado = quadrado(4)
print(f"O quadrado é: {resultado_quadrado}")
```

### 5. Documentação da Função

É uma boa prática incluir uma docstring (string de documentação) na definição da função para descrever o que a função faz.

```python
def multiplicacao(a, b):
    """Esta função retorna o produto de dois números."""
    return a * b
```

### 6. Variáveis Locais e Globais

Variáveis dentro de uma função são locais por padrão, o que significa que elas existem apenas dentro da função. Variáveis definidas fora da função são globais.

```python
variavel_global = 10

def minha_funcao():
    variavel_local = 5
    print(f"Variável local: {variavel_local}")
    print(f"Variável global: {variavel_global}")

# Chamando a função
minha_funcao()
```

Este tutorial básico sobre funções em Python deve ajudar a construir uma base sólida. À medida que você avança, pode explorar tópicos mais avançados, como funções anônimas (lambda), funções recursivas, manipulação de argumentos arbitrários e mais.