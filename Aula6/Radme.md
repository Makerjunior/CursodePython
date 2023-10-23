

# Tutorial de Tipos de Dados em Python

Python é uma linguagem de programação dinâmica, o que significa que você não precisa declarar explicitamente o tipo de uma variável. No entanto, Python suporta vários tipos de dados nativos, que são fundamentais para a programação. Vamos explorar os principais tipos de dados em Python:

## 1. Números

Python suporta diversos tipos de números, incluindo inteiros (int) e números de ponto flutuante (float).

```python
inteiro = 42
ponto_flutuante = 3.14
```

## 2. Strings

Strings são usadas para armazenar texto. Elas podem ser criadas com aspas simples ou duplas.

```python
string1 = 'Olá, mundo!'
string2 = "Python é incrível!"
```

## 3. Listas

Listas são coleções ordenadas e mutáveis de elementos. Os elementos podem ser de qualquer tipo.

```python
minha_lista = [1, 2, 3, 'quatro', 5.0]
```

## 4. Tuplas

Tuplas são semelhantes às listas, mas são imutáveis, o que significa que seus elementos não podem ser alterados após a criação.

```python
minha_tupla = (1, 2, 3, 'quatro', 5.0)
```

## 5. Dicionários

Dicionários são coleções de pares chave-valor. Cada chave é única e associada a um valor.

```python
meu_dicionário = {'nome': 'João', 'idade': 30, 'cidade': 'Exemplo'}
```

## 6. Conjuntos

Conjuntos são coleções não ordenadas de elementos únicos. Eles são úteis para remover duplicatas.

```python
meu_conjunto = {1, 2, 3, 4, 5}
```

## 7. Booleanos

Os booleanos representam os valores verdadeiro (True) e falso (False) e são usados para lógica condicional.

```python
verdadeiro = True
falso = False
```

## 8. None

None é usado para representar a ausência de valor ou a falta de um valor válido.

```python
valor_nulo = None
```

Agora que você conhece os principais tipos de dados em Python, pode começar a utilizá-los em seus programas. Lembre-se de que, em Python, as variáveis são dinamicamente tipadas, o que significa que o tipo da variável pode ser alterado durante a execução do programa. Além disso, você pode verificar o tipo de uma variável usando a função `type()`.

```python
numero = 42
print(type(numero))  # Isso imprimirá <class 'int'>, indicando que a variável é do tipo inteiro.
```

Explore e pratique o uso desses tipos de dados para desenvolver programas eficazes em Python. Eles são a base para a construção de aplicativos Python eficientes e versáteis.