class ListaDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item} adicionado a lista.")

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"{item} removido da lista.")
        else:
            print(f"{item} nao encontrado na lista.")

    def mostrar_lista(self):
        if self.itens:
            print("Lista de Compras:")
            for i, item in enumerate(self.itens, start=1):
                print(f"{i}. {item}")
        else:
            print("Lista de compras vazia.")

# Exemplo de uso
lista = ListaDeCompras()

while True:
    print("\n1. Adicionar item a lista")
    print("2. Remover item da lista")
    print("3. Ver lista de compras")
    print("4. Sair")

    escolha = input("Escolha uma opcao (1/2/3/4): ")

    if escolha == "1":
        item = input("Digite o item a ser adicionado: ")
        lista.adicionar_item(item)
    elif escolha == "2":
        item = input("Digite o item a ser removido: ")
        lista.remover_item(item)
    elif escolha == "3":
        lista.mostrar_lista()
    elif escolha == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opcao invalida. Tente novamente.")
