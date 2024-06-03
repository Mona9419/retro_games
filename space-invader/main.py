import pygame
import random

# Inicialização do pygame
pygame.init()

# Configurações da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Cores
black = (0, 0, 0)
white = (255, 255, 255)

# Jogador
player_width = 50
player_height = 50
player_x = (screen_width // 2) - (player_width // 2)
player_y = screen_height - player_height - 10
player_speed = 5

# Inimigo
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemy_list = []

# Projéteis
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullet_list = []

# Função para desenhar o jogador
def draw_player(x, y):
    pygame.draw.rect(screen, white, (x, y, player_width, player_height))

# Função para desenhar os inimigos
def draw_enemies(enemies):
    for enemy in enemies:
        pygame.draw.rect(screen, white, (enemy[0], enemy[1], enemy_width, enemy_height))

# Função para desenhar projéteis
def draw_bullets(bullets):
    for bullet in bullets:
        pygame.draw.rect(screen, white, (bullet[0], bullet[1], bullet_width, bullet_height))

# Função principal
def game_loop():
    global player_x
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed
        if keys[pygame.K_SPACE]:
            bullet_x = player_x + (player_width // 2) - (bullet_width // 2)
            bullet_y = player_y
            bullet_list.append([bullet_x, bullet_y])

        # Movimento dos projéteis
        for bullet in bullet_list:
            bullet[1] -= bullet_speed
            if bullet[1] < 0:
                bullet_list.remove(bullet)

        # Geração de inimigos
        if random.randint(1, 20) == 1:
            enemy_x = random.randint(0, screen_width - enemy_width)
            enemy_y = 0
            enemy_list.append([enemy_x, enemy_y])

        # Movimento dos inimigos
        for enemy in enemy_list:
            enemy[1] += enemy_speed
            if enemy[1] > screen_height:
                enemy_list.remove(enemy)

        # Colisões
        for bullet in bullet_list:
            for enemy in enemy_list:
                if (bullet[0] >= enemy[0] and bullet[0] <= enemy[0] + enemy_width) or (bullet[0] + bullet_width >= enemy[0] and bullet[0] + bullet_width <= enemy[0] + enemy_width):
                    if bullet[1] >= enemy[1] and bullet[1] <= enemy[1] + enemy_height:
                        bullet_list.remove(bullet)
                        enemy_list.remove(enemy)
                        break

        draw_player(player_x, player_y)
        draw_enemies(enemy_list)
        draw_bullets(bullet_list)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Execução do jogo
game_loop()
