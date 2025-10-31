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

#TODO1: crea 2 Rect che si toccano oppure no
 

 
dt = clock.tick(60) / 1000.0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    #gestione dei collide

    #TODO2:scivi ina condizione che scive se i 2 Rect si toccano
    
 
    # Disegna tutto
    win.fill(BLACK)

    #TODO3:scrivi la parte per far apparire a schermo i Rect
 
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
