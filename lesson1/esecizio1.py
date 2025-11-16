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

# TO DO 1 crea due rettangoli
rect1 = pygame.Rect(200, 200, 100, 100)
rect2 = pygame.Rect(350, 200, 100, 100)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Collisione
    if rect1.colliderect(rect2):
        print("I rettangoli si toccano!")
    else:
        print("I rettangoli NON si toccano.")

    # Disegno
    win.fill(BLACK)
    pygame.draw.rect(win, RED, rect1)
    pygame.draw.rect(win, BLUE, rect2)

    pygame.display.update()
    clock.tick(60)
 
pygame.quit()
