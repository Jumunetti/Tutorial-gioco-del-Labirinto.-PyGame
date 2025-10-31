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
 
# Muri
#TODO3: crea una lista walls con dentro tutti i muri che vuoi
 
dt = clock.tick(60) / 1000.0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    #gestione dei collide

    #TODO4: movimento del personaggio e collisione con i muri
    # Movimento orizzontale con collisione
    
 
    # Movimento verticale con collisione

 
    # Controllo vittoria
    # TODO5: gestisci la con il goal e la vittoria
 
    # Disegna tutto
    win.fill(BLACK)
 
    #TODO6: scrivi la partee necessaria per disegnare a schermo i nemici
 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
