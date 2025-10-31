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

player = pygame.Rect(40, 45, 30, 30)
vel = 4
 
#nemici

#TODO1: crea i 3 Rect nemici e crea una variabile velocita_nemico
 
dt = clock.tick(60) / 1000.0

# info nemici
#TODO2: crea le variabili che servono ai nemici


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    #movimento nemici

    #TODO3: scrivi il movimento dei tre nemici
  
    #nemico 1
    

    #nemico 2
 
 
    #nemico 3


  

    #gestione dei collide
 
    #TODO4: gestigli le collisioni con i nemici

    #Movimento orizzontale con collisione
 
    # Movimento verticale con collisione

 
    # Disegna tutto
    win.fill(BLACK)
    pygame.draw.rect(win, YELLOW, player)
    pygame.draw.rect(win, RED, nemico1)
    pygame.draw.rect(win, RED, nemico2)
    pygame.draw.rect(win, RED, nemico3)
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
