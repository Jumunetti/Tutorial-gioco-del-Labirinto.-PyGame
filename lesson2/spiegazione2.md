
## TODO1: crea il player e una variabile velocità_player

Crea un rettangolo che rappresenta il giocatore (il personaggio controllato dall’utente) e una variabile che indica la sua velocità di movimento.

Esempio:
```python
player = pygame.Rect(40, 45, 30, 30)  # posizione iniziale e dimensioni del giocatore
velocità_player = 4  # pixel di movimento per frame
```

- Il primo e secondo numero (`40, 45`) sono le coordinate iniziali (x, y).
- Il terzo e quarto numero (`30, 30`) sono larghezza e altezza del rettangolo.

---

## TODO2: crea il Rect goal

Crea un rettangolo che rappresenta il traguardo da raggiungere (in genere di colore verde).

Esempio:
```python
goal = pygame.Rect(1100, 500, 50, 50)
```

- Questo sarà il punto in cui il giocatore deve arrivare per vincere.
- Puoi scegliere liberamente la posizione e le dimensioni.

---

## TODO3: crea una lista walls con dentro tutti i muri che vuoi

I muri servono per creare il labirinto o gli ostacoli.  
Vanno inseriti in una lista di `pygame.Rect`.

Esempio:
```python
walls = [
    pygame.Rect(0, 0, 1200, 20),  # bordo superiore
    pygame.Rect(0, 0, 20, 600),   # bordo sinistro
    pygame.Rect(0, 580, 1200, 20), # bordo inferiore
    pygame.Rect(1180, 0, 20, 600), # bordo destro
    # altri muri interni
    pygame.Rect(200, 100, 30, 200),
    pygame.Rect(400, 300, 250, 30)
]
```

- Ogni muro è un rettangolo che blocca il movimento del giocatore.
- Puoi aggiungere quanti ne vuoi per creare percorsi o labirinti.

---

## TODO4: movimento del personaggio e collisione con i muri

Gestisci il movimento con i tasti `W`, `A`, `S`, `D` e impedisci che il giocatore attraversi i muri.

Esempio:
```python
keys = pygame.key.get_pressed()

# Movimento orizzontale
if keys[pygame.K_a]:
    player.x -= velocità_player
    for wall in walls:
        if player.colliderect(wall):
            player.x += velocità_player
if keys[pygame.K_d]:
    player.x += velocità_player
    for wall in walls:
        if player.colliderect(wall):
            player.x -= velocità_player

# Movimento verticale
if keys[pygame.K_w]:
    player.y -= velocità_player
    for wall in walls:
        if player.colliderect(wall):
            player.y += velocità_player
if keys[pygame.K_s]:
    player.y += velocità_player
    for wall in walls:
        if player.colliderect(wall):
            player.y -= velocità_player
```

- Ogni volta che il giocatore si muove, controlli se collide con un muro.
- Se sì, annulli lo spostamento.

---

## TODO5: gestisci la collisione con il goal e la vittoria

Controlla se il giocatore tocca il rettangolo del traguardo e mostra un messaggio di vittoria.

Esempio:
```python
if player.colliderect(goal):
    print("Hai vinto!")
    run = False  # termina il gioco
```

---

## TODO6: disegna tutto

Disegna tutti gli elementi sulla finestra: sfondo, giocatore, obiettivo e muri.

Esempio:
```python
win.fill(BLACK)  # sfondo nero
pygame.draw.rect(win, YELLOW, player)  # giocatore
pygame.draw.rect(win, GREEN, goal)     # obiettivo
for wall in walls:
    pygame.draw.rect(win, BLUE, wall)  # muri
```

![Testo alternativo](../Immagini/Screenshot_minilabirinto.png)
