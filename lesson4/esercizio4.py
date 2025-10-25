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



#TODO1: scrivi la variabile font e la variabile condizione



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
starty = nemico.y
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    #movimento nemico

    #nemico 
    nemico.y += verso * velocita * dt
 
    if verso == 1 and nemico.y >= starty + distanza:
        nemico.y = starty + distanza
        verso = -1
        
    if verso == -1 and nemico.y <= starty:
        nemico.y = starty
        verso = 1
 
    # Movimento orizzontale con collisione
    if keys[pygame.K_a]:
        player.x -= vel

    if keys[pygame.K_d]:
        player.x += vel


    # Movimento verticale con collisione
    if keys[pygame.K_w]:
        player.y -= vel

    if keys[pygame.K_s]:
        player.y += vel


    #TODO2: inserisci la variabile nelle condizioni di collisione
 
    # Controllo vittoria e sconfitta
    if player.colliderect(goal):
        condizione = 2
        run = False  

    if player.colliderect(nemico):
        condizione = 1
        run = False
 
    # Disegna tutto
    win.fill(BLACK)
    pygame.draw.rect(win, YELLOW, player)
    pygame.draw.rect(win, GREEN, goal)
    pygame.draw.rect(win, RED, nemico)
 
    #TODO3: scrivi la condizione per le schermate
 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()

