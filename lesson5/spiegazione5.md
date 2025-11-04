# Lezione 5 – Soluzione e spiegazione dei TODO

---

## TODO1 – Informazioni per la schermata

Serve per gestire le **schermate di vittoria o sconfitta**.

```python
font = pygame.font.SysFont(None, 80)
condizione = 0
```

- `font` serve per scrivere testo sullo schermo.  
- `condizione` serve per capire lo stato del gioco:  
  - `0` = partita in corso  
  - `1` = sconfitta  
  - `2` = vittoria  

---

## TODO2 – Crea il player e una variabile velocità_player

Creiamo il rettangolo del giocatore e la sua velocità.

```python
player = pygame.Rect(40, 45, 30, 30)
vel = 4
```

- Il rettangolo `Rect` rappresenta il giocatore.
- `vel` indica di quanti pixel si muove per ogni frame.

---

## TODO3 – Crea il Rect goal

Aggiungiamo il **rettangolo verde** che rappresenta l’obiettivo finale.

```python
goal = pygame.Rect(1100, 500, 50, 50)
```

Quando il giocatore collide con questo rettangolo, il gioco sarà vinto.

---

## TODO4 – Crea i 3 Rect nemici e la velocità

Definiamo i tre nemici e la velocità con cui si muoveranno.

```python
nemico1 = pygame.Rect(420, 30, 30, 30)
nemico2 = pygame.Rect(420, 545, 30, 30)
nemico3 = pygame.Rect(525, 180, 30, 30)

velocita = 50
```

---

## TODO5 – Crea la lista `walls`

Serve a disegnare e gestire i muri del labirinto.  
Ogni muro è un rettangolo `Rect`, e li mettiamo in una lista per disegnarli e controllare le collisioni.

```python
walls = [
    pygame.Rect(0, 0, 1200, 20), pygame.Rect(0, 0, 20, 600),
    pygame.Rect(0, 580, 1200, 20), pygame.Rect(1180, 0, 20, 600),
    pygame.Rect(100,00,30,350), pygame.Rect(100,430,30,400),

    pygame.Rect(200,65, 30,190),pygame.Rect(200,340, 30,190),
    pygame.Rect(450,65, 30,190),pygame.Rect(450,340, 30,190),

    pygame.Rect(200,65, 250,30),pygame.Rect(200,340, 250,30),
    pygame.Rect(200,225, 250,30),pygame.Rect(200,500, 250,30),

    pygame.Rect(600,65, 30,190),pygame.Rect(600,340, 30,190),
    pygame.Rect(850,65, 30,190),pygame.Rect(850,340, 30,190),

    pygame.Rect(600,65, 250,30),pygame.Rect(600,340, 250,30),
    pygame.Rect(600,225, 250,30),pygame.Rect(600,500, 250,30),
    pygame.Rect(1000,-200,30,350), pygame.Rect(1000,220,30,400),
]
```

---

## TODO6 – Crea le variabili che servono ai nemici

Servono per gestire il **verso e la distanza del movimento** dei nemici.

```python
verso = 1
distanza = 220
startx = nemico1.x
starty = nemico3.y
```

- `verso` serve per cambiare direzione (1 = avanti, -1 = indietro)  
- `distanza` indica quanto lontano si muovono prima di tornare indietro  
- `startx` e `starty` memorizzano la posizione iniziale dei nemici  

---

## TODO7 – Movimento dei tre nemici

I nemici si muovono avanti e indietro finché raggiungono un limite, poi cambiano direzione.

```python
# nemico 1
nemico1.x += verso * velocita * dt
if verso == 1 and nemico1.x >= startx + distanza:
    nemico1.x = startx + distanza
    verso = -1
if verso == -1 and nemico1.x <= startx:
    nemico1.x = startx
    verso = 1

# nemico 2
nemico2.x += verso * velocita * dt
if verso == 1 and nemico2.x >= startx + distanza:
    nemico2.x = startx + distanza
    verso = -1
if verso == -1 and nemico2.x <= startx:
    nemico2.x = startx
    verso = 1

# nemico 3
nemico3.y += verso * velocita * dt
if verso == 1 and nemico3.y >= starty + distanza:
    nemico3.y = starty + distanza
    verso = -1
if verso == -1 and nemico3.y <= starty:
    nemico3.y = starty
    verso = 1
```

---

## TODO8 – Gestisci le collisioni con i nemici

Se il giocatore tocca un nemico, la partita è persa.

```python
if player.colliderect(nemico1):
    condizione = 1
    run = False

if player.colliderect(nemico2):
    condizione = 1
    run = False

if player.colliderect(nemico3):
    condizione = 1
    run = False
```

---

## TODO9 – Movimento del personaggio e collisione con i muri

Controlliamo il movimento del giocatore e impediamo di attraversare i muri.

```python
# Movimento orizzontale
if keys[pygame.K_a]:
    player.x -= vel
    for wall in walls:
        if player.colliderect(wall):
            player.x += vel
if keys[pygame.K_d]:
    player.x += vel
    for wall in walls:
        if player.colliderect(wall):
            player.x -= vel

# Movimento verticale
if keys[pygame.K_w]:
    player.y -= vel
    for wall in walls:
        if player.colliderect(wall):
            player.y += vel
if keys[pygame.K_s]:
    player.y += vel
    for wall in walls:
        if player.colliderect(wall):
            player.y -= vel
```

---

## TODO10 – Controllo vittoria

Se il giocatore tocca il rettangolo verde (`goal`), la partita è vinta.

```python
if player.colliderect(goal):
    condizione = 2
    run = False
```

---

## TODO11 – Schermate di vittoria e sconfitta

Dopo che `run` diventa `False`, mostriamo un messaggio in base alla condizione.

```python
if condizione == 1:
    win.blit(font.render("Hai perso", True, (255, 0, 0)), (430, 275))
elif condizione == 2:
    win.blit(font.render("Hai vinto", True, (0, 255, 0)), (430, 275))
```

