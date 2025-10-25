
import pygame
 
pygame.init()
 
# Finestra e clock
win = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()
 
# Colori
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

font = pygame.font.SysFont(None, 80)
condizione = 0

# Giocatore
player = pygame.Rect(40, 45, 30, 30)
vel = 4
 
# Obiettivo
goal = pygame.Rect(1100, 500, 50, 50)  # rettangolo verde
 
#nemico 
nemico = pygame.Rect(525, 180, 30,30)
 
velocita = 50

 
dt = clock.tick(60) / 1000.0
 
verso = 1
distanza = 220
startx = nemico1.x
starty = nemico3.y
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    #movimento nemico

    #nemico 
    nemico3.y += verso * velocita * dt
 
    if verso == 1 and nemico.y >= starty + distanza:
        nemico.y = starty + distanza
        verso = -1
 

    if player.colliderect(nemico):
        condizione = 1
        run = False
 
    # Movimento orizzontale con collisione
    if keys[pygame.K_a]:
        player.x -= vel
        for wall in walls:
            if player.colliderect(wall):
                player.x += vel
    if keys[pygame.K_d]:
        player.x += vel
        for wall in walls:
            if player.colliderect(wall):
                player.x -= vel
 
    # Movimento verticale con collisione
    if keys[pygame.K_w]:
        player.y -= vel
        for wall in walls:
            if player.colliderect(wall):
                player.y += vel
    if keys[pygame.K_s]:
        player.y += vel
        for wall in walls:
            if player.colliderect(wall):
                player.y -= vel
 
    # Controllo vittoria
    if player.colliderect(goal):
        condizione = 2
        run = False  # termina il gioco
 
    # Disegna tutto
    win.fill(BLACK)
    pygame.draw.rect(win, YELLOW, player)
    pygame.draw.rect(win, GREEN, goal)
    pygame.draw.rect(win, RED, nemico1)
    pygame.draw.rect(win, RED, nemico2)
    pygame.draw.rect(win, RED, nemico3)
    for wall in walls:
        pygame.draw.rect(win, BLUE, wall)
    if condizione == 1:
        win.blit(font.render("Hai perso", True, (255, 0, 0)), (430, 275))
    elif condizione == 2:
        win.blit(font.render("Hai vinto", True, (0, 255, 0)), (430, 275))
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
