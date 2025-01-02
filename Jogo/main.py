import tkinter as tk
import random

class JogoCorrida:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo de Corrida com Obstáculos")
        
        self.largura = 400
        self.altura = 600
        self.carro_largura = 40
        self.carro_altura = 70
        self.velocidade_obstaculo = 15  # Velocidade inicial
        
        self.canvas = tk.Canvas(master, width=self.largura, height=self.altura, bg="gray")
        self.canvas.pack()
        
        self.carro = self.canvas.create_rectangle(self.largura // 2 - self.carro_largura // 2, 
                                                   self.altura - self.carro_altura - 10, 
                                                   self.largura // 2 + self.carro_largura // 2, 
                                                   self.altura - 10, fill="blue")
        
        self.obstaculos = []
        self.pontos = 0  # Inicializa os pontos
        self.marcador = self.canvas.create_text(50, 20, text=f"Pontos: {self.pontos}", fill="white", font=("Helvetica", 16))
        
        self.criar_obstaculo()
        
        self.jogo_em_andamento = True
        self.mover_obstaculos()
        
        # Inicia o aumento da velocidade
        self.aumentar_velocidade()
        
        self.master.bind("<Left>", self.mover_esquerda)
        self.master.bind("<Right>", self.mover_direita)
        self.master.bind("<Up>", self.mover_frente)  # Bind para mover para frente
        self.master.bind("<Down>", self.mover_atras)  # Bind para mover para trás

    def criar_obstaculo(self):
        x = random.randint(0, self.largura - 40)
        obstaculo = self.canvas.create_rectangle(x, 0, x + 40, 30, fill="red")
        self.obstaculos.append(obstaculo)
        self.master.after(2000, self.criar_obstaculo)  # Cria um novo obstáculo a cada 2 segundos

    def mover_obstaculos(self):
        for obstaculo in self.obstaculos:
            self.canvas.move(obstaculo, 0, self.velocidade_obstaculo)
            if self.canvas.coords(obstaculo)[1] > self.altura:
                self.canvas.delete(obstaculo)
                self.obstaculos.remove(obstaculo)
                self.pontos += 1  # Aumenta os pontos
                self.atualizar_marcador()  # Atualiza o marcador de pontos
        
        if self.jogo_em_andamento:
            self.verificar_colisao()
            self.master.after(50, self.mover_obstaculos)  # Chama a função novamente após 50ms

    def atualizar_marcador(self):
        self.canvas.itemconfig(self.marcador, text=f"Pontos: {self.pontos}")  # Atualiza o texto do marcador

    def mover_esquerda(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.carro)
        if x1 > 0:
            self.canvas.move(self.carro, -20, 0)

    def mover_direita(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.carro)
        if x2 < self.largura:
            self.canvas.move(self.carro, 20, 0)

    def mover_frente(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.carro)
        if y2 > 0:  # Certifica-se de que o carro não saia da tela
            self.canvas.move(self.carro, 0, -10)  # Move o carro para frente (cima)

    def mover_atras(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.carro)
        if y1 < self.altura:  # Certifica-se de que o carro não saia da tela
            self.canvas.move(self.carro, 0, 10)  # Move o carro para trás (baixo)

    def verificar_colisao(self):
        carro_coords = self.canvas.coords(self.carro)
        for obstaculo in self.obstaculos:
            obstaculo_coords = self.canvas.coords(obstaculo)
            if (carro_coords[2] > obstaculo_coords[0] and carro_coords[0] < obstaculo_coords[2] and
                carro_coords[1] < obstaculo_coords[3]):
                self.game_over()
    
    def game_over(self):
        self.jogo_em_andamento = False
        self.canvas.create_text(self.largura // 2, self.altura // 2, text="Game Over", fill="white", font=("Helvetica", 24))

    def aumentar_velocidade(self):
        if self.jogo_em_andamento:
            self.velocidade_obstaculo += 1  # Aumenta a velocidade
            self.master.after(30000, self.aumentar_velocidade)  # Chama a função novamente após 30 segundos

# Cria a janela do jogo
janela = tk.Tk()
jogo = JogoCorrida(janela)
janela.mainloop()
