

# Dicionários em Python

## O que é um dicionário?

Um dicionário em Python é uma estrutura de dados que permite armazenar um conjunto de pares chave-valor. As chaves são únicas e usadas para acessar os valores associados a elas. Os dicionários são muito úteis quando você precisa mapear informações de uma maneira flexível.

## Criando um dicionário

Para criar um dicionário em Python, você pode usar chaves `{}` ou a função `dict()`. Aqui está um exemplo de um dicionário simples:

```python
# Criando um dicionário
meu_dicionario = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}
```

## Acessando valores em um dicionário

Para acessar um valor em um dicionário, você pode usar a chave correspondente dentro de colchetes `[]`:

```python
# Acessando valores em um dicionário
nome = meu_dicionário["nome"]
idade = meu_dicionário["idade"]
```

## Adicionando ou modificando valores

Você pode adicionar um novo par chave-valor ou modificar um valor existente em um dicionário desta forma:

```python
# Adicionando ou modificando valores em um dicionário
meu_dicionario["profissao"] = "Engenheira"
meu_dicionario["idade"] = 26  # Modifica o valor existente
```

## Removendo valores

Para remover um item de um dicionário, você pode usar o operador `del`:

```python
# Removendo um item de um dicionário
del meu_dicionario["cidade"]
```

## Verificando a existência de uma chave

Você pode verificar se uma chave existe em um dicionário usando o operador `in`:

```python
# Verificando a existência de uma chave
if "cidade" in meu_dicionario:
    print("A chave 'cidade' existe no dicionário.")
```

## Iterando através de um dicionário

Você pode iterar através das chaves, valores ou pares chave-valor em um dicionário usando loops. Aqui está um exemplo de como fazer isso:

```python
# Iterando através das chaves
for chave in meu_dicionario:
    print(chave)

# Iterando através dos valores
for valor in meu_dicionario.values():
    print(valor)

# Iterando através dos pares chave-valor
for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")
```

# Conjuntos em Python

## O que é um conjunto?

Um conjunto em Python é uma coleção não ordenada de elementos únicos. Os conjuntos são úteis quando você precisa armazenar um conjunto de itens sem repetições.

## Criando um conjunto

Você pode criar um conjunto em Python usando chaves `{}` ou a função `set()`. Aqui está um exemplo de um conjunto simples:

```python
# Criando um conjunto
meu_conjunto = {1, 2, 3, 4, 5}
```

## Adicionando e removendo elementos

Para adicionar um elemento a um conjunto, você pode usar o método `add()`. Para remover um elemento, use o método `remove()` ou `discard()`:

```python
# Adicionando elementos a um conjunto
meu_conjunto.add(6)

# Removendo elementos de um conjunto
meu_conjunto.remove(3)
```

O método `remove()` gera um erro se o elemento não existir no conjunto, enquanto o método `discard()` não gera erro.

## Operações de conjunto

Conjuntos suportam várias operações, como união, interseção e diferença. Aqui estão alguns exemplos:

```python
# União de conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.union(conjunto2)  # ou conjunto1 | conjunto2

# Interseção de conjuntos
intersecao = conjunto1.intersection(conjunto2)  # ou conjunto1 & conjunto2

# Diferença entre conjuntos
diferenca = conjunto1.difference(conjunto2)  # ou conjunto1 - conjunto2
```

## Verificando a existência de elementos

Você pode verificar se um elemento existe em um conjunto usando o operador `in`:

```python
# Verificando a existência de um elemento
if 4 in meu_conjunto:
    print("O elemento 4 está no conjunto.")
```

Espero que este tutorial tenha sido útil para entender dicionários e conjuntos em Python. Eles são estruturas de dados poderosas que podem ser usadas em muitos contextos diferentes.