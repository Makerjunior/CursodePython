Código linha por linha:

1. `itens = []`: Cria uma lista vazia chamada `itens`.

2. `def adicionar_item(item):`: Define uma função chamada `adicionar_item` que recebe um argumento `item`.

3. `    itens.append(item)`: Adiciona o item à lista `itens` usando o método `append`.

4. `    print(f"{item} adicionado à lista.")`: Imprime uma mensagem indicando que o item foi adicionado à lista.

5. `def remover_item(item):`: Define uma função chamada `remover_item` que recebe um argumento `item`.

6. `    if item in itens:`: Verifica se o item está presente na lista `itens`.

7. `        itens.remove(item)`: Se o item estiver na lista, remove o primeiro item encontrado com o valor especificado.

8. `        print(f"{item} removido da lista.")`: Imprime uma mensagem indicando que o item foi removido da lista.

9. `    else:`: Se o item não estiver na lista, o bloco de código dentro do `else` é executado.

10. `        print(f"{item} não encontrado na lista.")`: Imprime uma mensagem indicando que o item não foi encontrado na lista.

11. `def mostrar_lista():`: Define uma função chamada `mostrar_lista`.

12. `    if itens:`: Verifica se a lista `itens` não está vazia.

13. `        print("Lista de Compras:")`: Se a lista não estiver vazia, imprime uma mensagem indicando que a lista de compras será exibida.

14. `        for i, item in enumerate(itens, start=1):`: Itera sobre os itens na lista usando `enumerate`, começando com índice 1.

15. `            print(f"{i}. {item}")`: Imprime cada item na lista com seu índice.

16. `    else:`: Se a lista `itens` estiver vazia, o bloco de código dentro do `else` é executado.

17. `        print("Lista de compras vazia.")`: Imprime uma mensagem indicando que a lista de compras está vazia.

18. O bloco de código após as funções é um exemplo de uso, onde um menu interativo é exibido dentro de um loop `while True`.

19. `    escolha = input("Escolha uma opção (1/2/3/4): ")`: Solicita ao usuário que escolha uma opção do menu.

20. As instruções `if`, `elif` e `else` são usadas para realizar a ação correspondente com base na escolha do usuário.

21. O loop continua até que o usuário escolha a opção "4", momento em que é exibida uma mensagem indicando que o programa está saindo, e o loop é interrompido com `break`.

22. Se a opção escolhida pelo usuário não é válida, é exibida uma mensagem indicando que a opção é inválida.