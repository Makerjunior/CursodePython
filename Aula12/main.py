class Carro:
         
    def __init__(self, modelo, cor, ano, velocidade=0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self, v):
        self.velocidade += v
        print(f'O carro esta acelerando. Velocidade atual: {self.velocidade} km/h')

    def frear(self, v):
        if self.velocidade >= v:
            self.velocidade -= v
            print(f'O carro esta freando. Velocidade atual: {self.velocidade} km/h')
        else:
            print('O carro ja esta parado.')

    def obter_informacoes(self):
        return f'Modelo: {self.modelo}, Cor: {self.cor}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h'

# Exemplo de uso da classe Carro
carro1 = Carro(modelo='Fusca', cor='Azul', ano=2020)
print(carro1.obter_informacoes())

carro1.acelerar(30)
carro1.frear(10)

print(carro1.obter_informacoes())
