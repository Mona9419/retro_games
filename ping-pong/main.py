import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Define as dimensões da janela do jogo
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ping Pong by Mona")

# Define as cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)

# Configura o relógio para controlar a taxa de frames
clock = pygame.time.Clock()

# Define as dimensões e posições iniciais das barras e da bola
largura_barra = 15
altura_barra = 90
barra_a_x = 50
barra_a_y = altura // 2 - altura_barra // 2
barra_b_x = largura - 50 - largura_barra
barra_b_y = altura // 2 - altura_barra // 2
velocidade_barra = 10

raio_bola = 15
bola_x = largura // 2
bola_y = altura // 2
velocidade_bola_x = 5
velocidade_bola_y = 5

# Inicializa as pontuações
score_a = 0
score_b = 0

# Configura a fonte para o texto de pontuação
fonte = pygame.font.Font(None, 74)

# Função para desenhar as barras, a bola e a pontuação
def desenhar():
    tela.fill(preto)
    pygame.draw.rect(tela, branco, (barra_a_x, barra_a_y, largura_barra, altura_barra))
    pygame.draw.rect(tela, branco, (barra_b_x, barra_b_y, largura_barra, altura_barra))
    pygame.draw.ellipse(tela, vermelho, (bola_x - raio_bola, bola_y - raio_bola, raio_bola * 2, raio_bola * 2))
    pygame.draw.aaline(tela, branco, (largura // 2, 0), (largura // 2, altura))
    
    texto = fonte.render(f"{score_a}  {score_b}", True, branco)
    tela.blit(texto, (largura // 2 - texto.get_width() // 2, 10))
    
    pygame.display.flip()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Movimento das barras
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and barra_a_y > 0:
        barra_a_y -= velocidade_barra
    if teclas[pygame.K_s] and barra_a_y < altura - altura_barra:
        barra_a_y += velocidade_barra
    if teclas[pygame.K_UP] and barra_b_y > 0:
        barra_b_y -= velocidade_barra
    if teclas[pygame.K_DOWN] and barra_b_y < altura - altura_barra:
        barra_b_y += velocidade_barra

    # Movimento da bola
    bola_x += velocidade_bola_x
    bola_y += velocidade_bola_y

    # Colisão com as bordas superiores e inferiores
    if bola_y - raio_bola <= 0 or bola_y + raio_bola >= altura:
        velocidade_bola_y = -velocidade_bola_y

    # Colisão com as barras
    if bola_x - raio_bola <= barra_a_x + largura_barra and barra_a_y < bola_y < barra_a_y + altura_barra:
        velocidade_bola_x = -velocidade_bola_x
    if bola_x + raio_bola >= barra_b_x and barra_b_y < bola_y < barra_b_y + altura_barra:
        velocidade_bola_x = -velocidade_bola_x

    # Verificação de ponto (reinicia a bola e atualiza a pontuação)
    if bola_x < 0:
        score_b += 1
        bola_x = largura // 2
        bola_y = altura // 2
        velocidade_bola_x = -velocidade_bola_x
    if bola_x > largura:
        score_a += 1
        bola_x = largura // 2
        bola_y = altura // 2
        velocidade_bola_x = -velocidade_bola_x

    desenhar()
    clock.tick(60)
