""" Em Python, não há uma maneira de tornar atributos e métodos
verdadeiramente privados, como em algumas outras linguagens (por exemplo, Java).
No entanto, você pode seguir convenções para indicar 
que eles não devem ser acessados diretamente fora da classe.

Atributos e Métodos com um Único Subscrito (_): 
    Indicam que são "protegidos" e que seu acesso deve ser evitado fora da classe.
Atributos e Métodos com Dois Subscritos (__): 
    Indicam que são "privados" e que o acesso externo deve ser evitado. 
    O Python usa um mecanismo chamado "name mangling" para modificar o nome desses atributos e métodos.
"""

class Carros:
    
    def __init__(self, marca, modelo, ano):
        # Atributos privados, não devem ser acessados diretamente
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    # Método para definir informações
    def definir_informacoes(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    # Método para mostrar informações
    def mostrar_informacoes(self):
        print(f"Marca: {self.__marca}")  
        print(f"Modelo: {self.__modelo}")  
        print(f"Ano: {self.__ano}")

    # Getters e Setters para 'marca'
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    # Getters e Setters para 'modelo'
    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

    # Getters e Setters para 'ano'
    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano


# Criando instâncias da classe
carro1 = Carros("Toyota", "Corolla", 2022)
carro2 = Carros("Honda", "Civic", 2023)

# Mostrando informações do carro1
carro1.mostrar_informacoes()

print('----------------------------------')

# Alterando informações do carro1 usando os setters
carro1.set_marca("Chevrolet")
carro1.set_modelo("Opala")
carro1.set_ano(1972)

# Mostrando informações atualizadas do carro1

carro1.mostrar_informacoes()

print('----------------------------------')

# Mostrando informações do carro2
carro2.mostrar_informacoes()
