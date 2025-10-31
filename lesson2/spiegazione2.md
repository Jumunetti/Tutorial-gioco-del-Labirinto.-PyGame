# 1. Creazione del Giocatore

player = pygame.Rect(40, 45, 30, 30)
vel = 4
Spiegazione:
pygame.Rect(x, y, larghezza, altezza) 
Crea un rettangolo (in questo caso rappresenta il personaggio/giocatore).
È una struttura dati di Pygame che serve per:
-disegnare elementi sullo schermo;
-gestire le collisioni tra oggetti.
Quindi: 

player = pygame.Rect(40, 45, 30, 30)

crea un rettangolo con:
-posizione iniziale: (x = 40, y = 45)
-dimensioni: 30x30 pixel
Questo sarà il "corpo" del giocatore sullo schermo.
vel = 4 
Questa è la velocità del giocatore, cioè di quanti pixel si muove ogni volta che premi un tasto direzionale. Più il valore è alto, più il giocatore si sposta rapidamente.

# 2. Creazione dei Muri


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
Spiegazione:
Qui viene creata una lista di muri dell’arena di gioco. Ogni muro è anch’esso un rettangolo definito da pygame.Rect.
Esempio:

pygame.Rect(0, 0, 1200, 20)
È un muro orizzontale che parte dall’alto a sinistra dello schermo (0,0), ha una larghezza di 1200 pixel e un’altezza di 20 pixel , quindi rappresenta il bordo superiore.
Le prime 4 righe infatti disegnano i bordi esterni del gioco:
(0, 0, 1200, 20) → muro superiore
(0, 0, 20, 600) → muro sinistro
(0, 580, 1200, 20) → muro inferiore
(1180, 0, 20, 600) → muro destro
Le righe successive disegnano muri interni che formano un percorso.

# 3. Controllo della Vittoria

if player.colliderect(goal):
    condizione = 2
    run = False  # termina il gioco
Spiegazione:
player.colliderect(goal) È una funzione di Pygame che verifica se due rettangoli si toccano o si sovrappongono. In questo caso controlla se il giocatore entra in contatto con il rettangolo goal, che rappresenta la fine del livello.
Se c’è una collisione: 
condizione = 2
run = False
 -condizione = 2 → segnala che il giocatore ha vinto;
-run = False → fa terminare il ciclo principale del gioco,quindi finisce la partita.

