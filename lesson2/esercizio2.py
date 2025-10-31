# TODO creazione Giocatore
player = pygame.Rect(40, 45, 30, 30)
vel = 4
 

# TODO creazione Muri
walls = [
    pygame.Rect(0, 0, 1200, 20), pygame.Rect(0, 0, 20, 600),
    pygame.Rect(0, 580, 1200, 20), pygame.Rect(1180, 0, 20, 600),
    pygame.Rect(100,00,30,350), pygame.Rect(100,430,30,400),
    #primi 2 
    pygame.Rect(200,65, 30,190),pygame.Rect(200,340, 30,190),
    pygame.Rect(450,65, 30,190),pygame.Rect(450,340, 30,190),

    pygame.Rect(200,65, 250,30),pygame.Rect(200,340, 250,30),
    pygame.Rect(200,225, 250,30),pygame.Rect(200,500, 250,30),
    #secondi 2
    pygame.Rect(600,65, 30,190),pygame.Rect(600,340, 30,190),
    pygame.Rect(850,65, 30,190),pygame.Rect(850,340, 30,190),

    pygame.Rect(600,65, 250,30),pygame.Rect(600,340, 250,30),
    pygame.Rect(600,225, 250,30),pygame.Rect(600,500, 250,30),
    pygame.Rect(1000,-200,30,350), pygame.Rect(1000,220,30,400),

 
]
 

 
    # TODO Controllo vittoria
    if player.colliderect(goal):
        condizione = 2
        run = False  # termina il gioco
 


