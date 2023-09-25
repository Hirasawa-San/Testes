import pygame
import random

# inicializar o Pygame
pygame.init()
pygame.display.set_caption("test.exe")


# definir as dimensões da janela do jogo
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# criar a janela do jogo
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# definir as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# definir a posição e o tamanho do jogador
player_x = 400
player_y = 500
player_width = 50
player_height = 50
player_vel = 0.5

# definir a posição e o tamanho do inimigo
enemy_x = random.randint(0, WINDOW_WIDTH - player_width)
enemy_y = 0
enemy_width = 50
enemy_height = 50
enemy_speed = 0.1

# definir a pontuação inicial
score = 0

# criar a fonte de texto
font = pygame.font.SysFont(None, 40)

# definir o loop do jogo
game_running = True
while game_running:

    # processar os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_LEFT]:
        player_x -= player_vel

    if comandos[pygame.K_RIGHT]:
        player_x += player_vel

        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_LEFT:
        #        player_x -= player_vel
        #    elif event.key == pygame.K_RIGHT:
        #        player_x += player_vel

    # atualizar a posição do inimigo
    enemy_y += enemy_speed
    if enemy_y > WINDOW_HEIGHT:
        enemy_x = random.randint(0, WINDOW_WIDTH - player_width)
        enemy_y = 0
        score += 1
        enemy_speed += 0.06
        player_vel += 0.1

    # detectar colisão entre jogador e inimigo
    if (enemy_x < player_x + player_width and
        enemy_x + enemy_width > player_x and
        enemy_y < player_y + player_height and
        enemy_y + enemy_height > player_y):
        game_running = False

    # limpar a tela
    screen.fill(WHITE)

    # desenhar o jogador
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))

    # desenhar o inimigo
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))

    # desenhar a pontuação
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # atualizar a tela
    pygame.display.update()

# encerrar o Pygame
pygame.quit()