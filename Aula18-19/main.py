class Carros:
    
    def __init__(self, marca, modelo, ano):
         self.marca = marca
         self.modelo = modelo
         self.ano = ano
        
    
    def definir_iformacoes(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
         
    def mostrar_informacoes(self):
        print(f"Marca: {self.marca}")  
        print(f"Modelo: {self.modelo}")  
        print(f"Ano: {self.ano}")  
       
carro1 = Carros("Toyota","Corolla",2022)
carro2 = Carros("Honda","Civic",2023)

carro1.mostrar_informacoes()

print('----------------------------------')

carro1.definir_iformacoes("Chevrolet","Opala",1972)

#carro2.definir_iformacoes("Honda","Civic",2023)

carro1.mostrar_informacoes()
print('----------------------------------')
carro2.mostrar_informacoes()

 

        
          