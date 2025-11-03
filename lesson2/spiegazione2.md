
# TODO1: crea il player e una variabile velocità_player
Cosa fare:
Si deve creare un rettangolo che rappresenti il giocatore e una variabile per la velocità di movimento.
Esempio:

player = pygame.Rect(40, 45, 30, 30)  # x, y, larghezza, altezza
velocita_player = 4  # velocità di movimento
Questo ti permette di muovere il giocatore più avanti nel codice.


# TODO3: crea una lista walls con dentro tutti i muri che vuoi
si deve creare una lista di pygame.Rect che rappresentano i muri del livello. Servono per limitare i movimenti del giocatore e creare un labirinto.
Esempio:

walls = [
    pygame.Rect(0, 0, 1200, 20),   # muro superiore
    pygame.Rect(0, 0, 20, 600),    # muro sinistro
    pygame.Rect(1180, 0, 20, 600), # muro destro
    pygame.Rect(0, 580, 1200, 20), # muro inferiore
    pygame.Rect(300, 200, 200, 30),
    pygame.Rect(600, 400, 150, 30)
]

# TODO5: gestisci la con il goal e la vittoria
Verifica se il giocatore ha raggiunto l’obiettivo (goal). Se sì, puoi stampare un messaggio o terminare il gioco.
Esempio:

if player.colliderect(goal):
    print("Hai vinto!")
    run = False
