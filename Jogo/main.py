import tkinter as tk
import random

# Configurações iniciais
largura = 400
altura = 400
tamanho_cobra = 20
delay = 100  # Tempo de atualização em milissegundos

# Função para criar uma maçã em uma posição aleatória
def criar_maca():
    x = random.randint(0, (largura - tamanho_cobra) // tamanho_cobra) * tamanho_cobra
    y = random.randint(0, (altura - tamanho_cobra) // tamanho_cobra) * tamanho_cobra
    return x, y

# Inicializa o jogo
def iniciar_jogo():
    global cobra, direcao, maca, jogo_em_andamento
    
    cobra = [(100, 100)]
    direcao = 'direita'
    maca = criar_maca()
    jogo_em_andamento = True
    
    canvas.delete("all")
    canvas.create_rectangle(0, 0, largura, altura, fill="black")
    canvas.create_rectangle(maca[0], maca[1], maca[0] + tamanho_cobra, maca[1] + tamanho_cobra, fill="red")
    
    mover_cobra()
    
# Função para mover a cobra
def mover_cobra():
    global direcao, maca
    
    if jogo_em_andamento:
        x, y = cobra[0]
        
        if direcao == 'direita':
            x += tamanho_cobra
        elif direcao == 'esquerda':
            x -= tamanho_cobra
        elif direcao == 'cima':
            y -= tamanho_cobra
        elif direcao == 'baixo':
            y += tamanho_cobra
        
        nova_cabeca = (x, y)
        cobra.insert(0, nova_cabeca)
        
        if nova_cabeca == maca:
            maca = criar_maca()
        else:
            cobra.pop()
        
        if verificar_colisao():
            game_over()
        else:
            desenhar_cobra()
            janela.after(delay, mover_cobra)

# Função para desenhar a cobra
def desenhar_cobra():
    canvas.delete("cobra")
    
    for segmento in cobra:
        x, y = segmento
        canvas.create_rectangle(x, y, x + tamanho_cobra, y + tamanho_cobra, fill="green", tag="cobra")

# Função para verificar colisões
def verificar_colisao():
    x, y = cobra[0]
    
    if x < 0 or x >= largura or y < 0 or y >= altura or cobra[0] in cobra[1:]:
        return True
    return False

# Função para encerrar o jogo
def game_over():
    global jogo_em_andamento
    jogo_em_andamento = False
    canvas.create_text(largura // 2, altura // 2, text="Game Over", fill="white", font=("Helvetica", 24))

# Funções para controlar a direção da cobra
def mover_direita(event):
    global direcao
    if direcao != 'esquerda':
        direcao = 'direita'

def mover_esquerda(event):
    global direcao
    if direcao != 'direita':
        direcao = 'esquerda'

def mover_cima(event):
    global direcao
    if direcao != 'baixo':
        direcao = 'cima'

def mover_baixo(event):
    global direcao
    if direcao != 'cima':
        direcao = 'baixo'

# Cria a janela do jogo
janela = tk.Tk()
janela.title("Jogo da Cobrinha")

# Cria o canvas
canvas = tk.Canvas(janela, width=largura, height=altura)
canvas.pack()

# Configura os controles
janela.bind("<Right>", mover_direita)
janela.bind("<Left>", mover_esquerda)
janela.bind("<Up>", mover_cima)
janela.bind("<Down>", mover_baixo)

# Botão para iniciar o jogo
btn_iniciar = tk.Button(janela, text="Iniciar Jogo", command=iniciar_jogo)
btn_iniciar.pack()

# Inicializa o jogo
iniciar_jogo()

# Inicia a interface gráfica
janela.mainloop()
