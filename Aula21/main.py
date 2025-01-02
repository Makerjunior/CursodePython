class Carros:
    
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
    
    def definir_informacoes(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
    
    def mostrar_informacoes(self):
        print(f"Marca: {self.__marca}")  
        print(f"Modelo: {self.__modelo}")  
        print(f"Ano: {self.__ano}")
    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca
    
    def get_modelo(self):
        return self.__modelo
    
    def set_modelo(self, modelo):
        self.__modelo = modelo
    
    def get_ano(self):
        return self.__ano
    
    def set_ano(self, ano):
        self.__ano = ano

class CarroEsportivo(Carros):
    
    def __init__(self, marca, modelo, ano, velocidade_maxima, potencia):
        super().__init__(marca, modelo, ano)
        self.__velocidade_maxima = velocidade_maxima
        self.__potencia = potencia
        self.__ligado = False  # Estado inicial do carro
    
    def definir_informacoes(self, marca, modelo, ano, velocidade_maxima, potencia):
        super().definir_informacoes(marca, modelo, ano)
        self.__velocidade_maxima = velocidade_maxima
        self.__potencia = potencia
    
    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Velocidade Maxima: {self.__velocidade_maxima} km/h")
        print(f"Potencia: {self.__potencia} CV")
        print(f"Status: {'Ligado' if self.__ligado else 'Desligado'}")
    
    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            print("Carro esportivo ligado.")
        else:
            print("O carro ja esta ligado.")
    
    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print("Carro esportivo desligado.")
        else:
            print("O carro ja esta desligado.")
    
    def get_velocidade_maxima(self):
        return self.__velocidade_maxima
    
    def set_velocidade_maxima(self, velocidade_maxima):
        self.__velocidade_maxima = velocidade_maxima
    
    def get_potencia(self):
        return self.__potencia
    
    def set_potencia(self, potencia):
        self.__potencia = potencia



# Criando um carro esportivo
carro_esportivo = CarroEsportivo("Ferrari", "488 Spider", 2021, 330, 670)

# Usando os métodos específicos do carro esportivo
carro_esportivo.ligar()
carro_esportivo.mostrar_informacoes()

print('----------------------------------')

# Atualizando informações
carro_esportivo.definir_informacoes("Porsche", "911 Turbo", 2022, 320, 650)
carro_esportivo.desligar()
carro_esportivo.mostrar_informacoes()
