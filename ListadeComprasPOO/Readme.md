

Este módulo implementa uma aplicação simples para gerenciar uma lista de compras. Ele oferece funcionalidades básicas, como adicionar itens à lista, remover itens e exibir a lista atualizada.

Funcionalidades Implementadas:
1. Adicionar Item à Lista:
    - Permite ao usuário adicionar um novo item à lista de compras.

2. Remover Item da Lista:
    - Permite ao usuário remover um item existente da lista de compras.

3. Mostrar Lista de Compras:
    - Exibe a lista atualizada de compras na saída padrão.

Estrutura do Código:
1. Classe ListaDeCompras:
    - A classe encapsula as funcionalidades relacionadas à lista de compras.
    - Métodos:
        - __init__(self): Inicializa a lista de compras.
        - adicionar_item(self, item): Adiciona um item à lista de compras.
        - remover_item(self, item): Remove um item da lista de compras, se presente.
        - mostrar_lista(self): Mostra a lista de compras na saída padrão.

2. Exemplo de Uso:
    - Um loop permite que o usuário interaja com o programa.
    - O usuário pode escolher entre adicionar, remover, mostrar a lista de compras ou sair do programa.

Exemplo de Uso:
    lista = ListaDeCompras()

    while True:
        # Menu de opções
        ...

Este módulo fornece uma maneira simples e interativa de gerenciar uma lista de compras em Python, utilizando uma abordagem orientada a objetos para manter o código organizado e modular.
