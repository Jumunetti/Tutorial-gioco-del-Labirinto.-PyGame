PUNTO 1
Cos’è Pygame e come funziona:

Pygame è una libreria di Python pensata per creare giochi 2D.È costruita sopra un’altra libreria chiamata SDL (Simple DirectMedia Layer), che gestisce le immagini, i suoni, la tastiera e il mouse.
Pygame Permette di:
disegnare elementi grafici (rettangoli, cerchi, immagini);
rilevare input da tastiera e mouse;controllare il tempo e il movimento;gestire suoni e animazioni.
Tutto si basa su una finestra grafica, chiamata “screen”, dentro la quale si disegna e si aggiorna continuamente il contenuto.

Ogni programma Pygame ruota attorno a un game loop (ciclo principale del gioco), che si ripete decine di volte al secondo (di solito 60).
A ogni ciclo il gioco:legge gli eventi (tasti, mouse, chiusura finestra);aggiorna lo stato logico (posizioni, collisioni, punteggi);ridisegna la scena (tutti gli oggetti).Questo meccanismo è alla base di qualsiasi gioco, anche professionale.

Un programma con Pygame segue quasi sempre la stessa struttura:

1) Importare la libreria:
import pygame

2)Inizializzare Pygame:
pygame.init()

3)Creare la finestra di gioco:
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Il mio gioco")

4)Ciclo principale (game loop)
Questo è il cuore del gioco: qui si ripetono continuamente tre cose:
controllare gli eventi (come tasti premuti o chiusura della finestra),
aggiornare la posizione degli oggetti:
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # sfondo nero
    pygame.display.flip()   # aggiorna lo schermo




#PUNTO 2 
classe rect,cos'è e come funziona:

In Pygame, la classe Rect (abbreviazione di rectangle) serve per rappresentare un rettangolo.
È molto utile perché:indica dove si trova un oggetto sullo schermo,definisce la sua grandezza,
e permette di gestire movimenti e collisioni in modo semplice.

Come si crea un Rect:
Puoi creare un rettangolo in vari modi, ma il più comune è questo:
rect = pygame.Rect(x, y, larghezza, altezza)
rect = pygame.Rect(50, 100, 60, 40)
Cio è: un rettangolo che parte dal punto (50, 100) e ha una larghezza di 60 e un’altezza di 40 pixel.

Come usarlo nel gioco:
Spesso si usa Rect per rappresentare la posizione di un personaggio o di un oggetto, anche se poi lo disegni con un’immagine o una forma.

Disegnare un Rect sullo schermo:
pygame.draw.rect(screen, RED, player_rect)
Questo disegna il rettangolo player_rect di colore rosso.





#PUNTO 3
















disegnare tutto sullo schermo.
