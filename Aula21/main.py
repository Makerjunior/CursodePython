class Carros:
    
    def __init__(self, marca, modelo, ano):
        # Atributos privados
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    # Propriedade para 'marca'
    @property
    def marca(self):
        """Getter para o atributo 'marca'"""
        return self.__marca

    @marca.setter
    def marca(self, valor):
        """Setter para o atributo 'marca'"""
        self.__marca = valor

    @marca.deleter
    def marca(self):
        """Deleter para o atributo 'marca'"""
        del self.__marca

    # Propriedade para 'modelo'
    @property
    def modelo(self):
        """Getter para o atributo 'modelo'"""
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        """Setter para o atributo 'modelo'"""
        self.__modelo = valor

    @modelo.deleter
    def modelo(self):
        """Deleter para o atributo 'modelo'"""
        del self.__modelo

    # Propriedade para 'ano'
    @property
    def ano(self):
        """Getter para o atributo 'ano'"""
        return self.__ano

    @ano.setter
    def ano(self, valor):
        """Setter para o atributo 'ano'"""
        self.__ano = valor

    @ano.deleter
    def ano(self):
        """Deleter para o atributo 'ano'"""
        del self.__ano

    # Método para mostrar informações
    def mostrar_informacoes(self):
        print(f"Marca: {self.__marca}")  
        print(f"Modelo: {self.__modelo}")  
        print(f"Ano: {self.__ano}")

# Criando instâncias da classe
carro1 = Carros("Toyota", "Corolla", 2022)
carro2 = Carros("Honda", "Civic", 2023)

# Mostrando informações do carro1
carro1.mostrar_informacoes()

print('----------------------------------')

# Alterando informações do carro1 usando as propriedades
carro1.marca = "Chevrolet"
carro1.modelo = "Opala"
carro1.ano = 1972

# Mostrando informações atualizadas do carro1
carro1.mostrar_informacoes()

print('----------------------------------')

# Mostrando informações do carro2
carro2.mostrar_informacoes()
