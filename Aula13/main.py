itens = []

def adicionar_item(item):
    itens.append(item)
    print(f"{item} adicionado à lista.")

def remover_item(item):
    if item in itens:
        itens.remove(item)
        print(f"{item} removido da lista.")
    else:
        print(f"{item} não encontrado na lista.")

def mostrar_lista():
    if itens:
        print("Lista de Compras:")
        for i, item in enumerate(itens, start=1):
            print(f"{i}. {item}")
    else:
        print("Lista de compras vazia.")




# Exemplo de uso
while True:
    print("\n1. Adicionar item à lista")
    print("2. Remover item da lista")
    print("3. Ver lista de compras")
    print("4. Sair")

    escolha = input("Escolha uma opção (1/2/3/4): ")

    if escolha == "1":
        item = input("Digite o item a ser adicionado: ")
        adicionar_item(item)
    elif escolha == "2":
        item = input("Digite o item a ser removido: ")
        remover_item(item)
    elif escolha == "3":
        mostrar_lista()
    elif escolha == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
