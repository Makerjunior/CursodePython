
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
       



class CarrosEsportivos(Carros):
    def __init__(self, marca, modelo, ano, velocidade_maxima, potencia):
        super().__init__(marca, modelo, ano)
        self.__velocidade_maxima = velocidade_maxima
        self.__potencia = potencia
        self.__ligado = False

    def mostrar_informacoes(self):
        super().mostrar_informacoes() 
        print(f"Velocidade Maxima {self.__velocidade_maxima}")  
        print(f"Potencia {self.__potencia}") 
        
    def ligar(self):
        if not self.__ligado:
            self.__ligado = True 
            print(f"O carro {self.get_modelo()} foi ligado")
        else:
            print(f"O carro {self.get_modelo()}  ja esta ligado")      
        
    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            print(f"O carro {self.get_modelo()} foi desligado")
        else:
            print(f"O carro {self.get_modelo()} ja foi desligado")    
    
    def get_velocidade_maxima(self):
        return __velocidade_maxima
    
    def set_velocidade_maxima(self, velocidade_maxima):
        self.__velocidade_maxima = velocidade_maxima    
    
    
    def get_potencia(self):
        return self.__potencia
    
    def set_potencia(self, potencia):
        self.__potencia = potencia
        
        
         
     

carro_esportivo = CarrosEsportivos("Ferrari","488", 2021, 330, 670)
carro_esportivo.ligar()
carro_esportivo.desligar()
print('___________________________________________')
carro_esportivo.mostrar_informacoes()
print('___________________________________________')
carro_esportivo.set_velocidade_maxima(550)
carro_esportivo.set_potencia(1000)
carro_esportivo.mostrar_informacoes()
print('___________________________________________')










