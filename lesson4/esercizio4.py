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
 
# Giocatore

#TODO1: crea il player e una variabile velocità_player
 
# Obiettivo

#TODO2: crea il Rect goal 
 
#nemici

#TODO3: crea i 3 Rect nemici e crea una variabile velocita_nemico

 
# Muri
#TODO4: crea una lista walls con dentro tutti i muri che vuoi
 
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

    #movimento nemico

    #nemico 1
    nemico1.x += verso * velocita * dt
 
    if verso == 1 and nemico1.x >= startx + distanza:
        nemico1.x = startx + distanza
        verso = -1
 
    if verso == -1 and nemico1.x <= startx:
        nemico1.x = startx
        verso = 1
 
 
    #nemico 2
 
    nemico2.x += verso * velocita * dt
 
    if verso == 1 and nemico2.x >= startx + distanza:
        nemico2.x = startx + distanza
        verso = -1
 
    if verso == -1 and nemico2.x <= startx:
        nemico2.x = startx
        verso = 1

    #nemico 3
    nemico3.y += verso * velocita * dt
 
    if verso == 1 and nemico3.y >= starty + distanza:
        nemico3.y = starty + distanza
        verso = -1
 
 
    if verso == -1 and nemico3.y <= starty:
        nemico3.y = starty
        verso = 1


    keys = pygame.key.get_pressed()
    if player.colliderect(nemico1):
        print("Hai perso")
        run = False
    if player.colliderect(nemico2):
        print("Hai perso")
        run = False
 
    if player.colliderect(nemico3):
        print("Hai perso")
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
        print("Hai vinto!")
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
 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
