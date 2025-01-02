
class Veiculo:
    def __init__(self,nome):
        self.nome=nome
    def mover(self):
        raise NotImplementedError("O metodo deve ser implementado na subclasse")
        #print("O metodo deve ser implementado na subclasse")    

class Carro(Veiculo):
    def mover(self):
        return f"O {self.nome} esta na estrada" 
    
class Bicicleta(Veiculo):
     def mover(self):
        return f"A  {self.nome} esta na ciclovia"
     
class Aviao(Veiculo):
      def mover(self):
        return f"O {self.nome} esta no ceu"  

veiculos = [
    Carro("Ferrari"),
    Bicicleta("BMX"),
    Aviao("Boeing 747")
]                
for veiculo in veiculos:
    print(veiculo.mover())                    