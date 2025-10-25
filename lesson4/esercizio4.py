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

# info nemici
#TODO4: crea le variabili che servono ai nemici


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    #movimento nemici

    #TODO5: scrivi il movimento dei tre nemici
    #nemico 1
    

    #nemico 2
 
 
    #nemico 3


    #gestione dei collide
 
    #TODO6: gestigli le collisioni con i nemici


    #TODO8: movimento del personaggio e collisione con i muri
    # Movimento orizzontale con collisione
    
 
    # Movimento verticale con collisione

 
    # Controllo vittoria
    # TODO9: gestisci la con il goal e la vittoria
 
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
