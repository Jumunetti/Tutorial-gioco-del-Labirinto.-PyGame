Lezione 3 – I nemici in movimento
In questa lezione aggiungeremo i nemici al gioco.
Ogni nemico sarà rappresentato da un rettangolo colorato che si muove automaticamente, e se il giocatore lo toccherà perderà la partita.

Obiettivi della lezione
1. Creare i tre nemici e una variabile per la velocità.
2. Impostare le variabili che gestiscono il loro movimento.
3. Far muovere i nemici avanti e indietro.
4. Gestire le collisioni tra giocatore e nemici.

TODO1 – Creazione dei nemici
All’inizio del codice, subito dopo la creazione del giocatore, trovi questo commento:

#TODO1: crea i 3 Rect nemici e crea una variabile velocita_nemico
Qui devi aggiungere le seguenti righe di codice:

nemico1 = pygame.Rect(420, 30, 30, 30)
nemico2 = pygame.Rect(420, 545, 30, 30)
nemico3 = pygame.Rect(525, 180, 30, 30)
velocita = 50

Spiegazione:
• Ogni nemico è un rettangolo (pygame.Rect) con posizione iniziale (x, y) e dimensioni di 30x30.
• La variabile velocita indica la velocità di spostamento dei nemici.

TODO2 – Variabili di movimento
#TODO2: crea le variabili che servono ai nemici
Aggiungi qui le seguenti variabili:

verso = 1
distanza = 220
startx = nemico1.x
starty = nemico3.y

Spiegazione:
• verso serve per sapere se il nemico si muove in avanti (1) o indietro (-1).
• distanza indica quanto spazio può percorrere il nemico prima di invertire direzione.
• startx e starty memorizzano la posizione iniziale dei nemici per calcolare i limiti di movimento.

TODO3 – Movimento dei tre nemici
Dentro il loop principale (while run:), nella sezione “#movimento nemici”, trovi:

#TODO3: scrivi il movimento dei tre nemici
Qui devi aggiungere questo codice:

# nemico 1 (movimento orizzontale)
nemico1.x += verso * velocita * dt
if verso == 1 and nemico1.x >= startx + distanza:
   nemico1.x = startx + distanza
   verso = -1
if verso == -1 and nemico1.x <= startx:
   nemico1.x = startx
   verso = 1

# nemico 2 (movimento orizzontale)
nemico2.x += verso * velocita * dt
if verso == 1 and nemico2.x >= startx + distanza:
   nemico2.x = startx + distanza
   verso = -1
if verso == -1 and nemico2.x <= startx:
   nemico2.x = startx
   verso = 1

# nemico 3 (movimento verticale)
nemico3.y += verso * velocita * dt
if verso == 1 and nemico3.y >= starty + distanza:
   nemico3.y = starty + distanza
   verso = -1
if verso == -1 and nemico3.y <= starty:
   nemico3.y = starty
   verso = 1

Spiegazione:
• Ogni nemico si muove avanti e indietro tra la posizione iniziale e un limite (startx + distanza o starty + distanza)
• Quando un nemico raggiunge uno dei due limiti, inverte la direzione cambiando il segno di verso.
• nemico1x += verso * velocita * dt serve per rendere il movimento fluido e indipendente dal frame.
• I nemici 1 e 2 si muovono in orizzontale, mentre il nemico 3 si muove in verticale.

TODO4 – Collisioni con i nemici
Infine trovi:
#TODO4: gestigli le collisioni con i nemici
Aggiungi qui:

if player.colliderect(nemico1):
   condizione = 1
   run = False

if player.colliderect(nemico2):
   condizione = 1
   run = False

if player.colliderect(nemico3):
   condizione = 1
   run = False

Spiegazione:
• player.colliderect(nemicoX) controlla se il giocatore tocca un nemico.
• In caso di contatto, condizione = 1 e il giocatore ha perso.
• run = False ferma il gioco per mostrare la schermata di sconfitta.
