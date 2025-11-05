
## TODO1: crea i 3 Rect nemici e crea una variabile velocita_nemico

Crea tre rettangoli che rappresentano i nemici e una variabile per la loro velocità.  
Ogni nemico avrà posizione e dimensione proprie.

Esempio:
```python
nemico1 = pygame.Rect(420, 30, 30, 30)
nemico2 = pygame.Rect(420, 545, 30, 30)
nemico3 = pygame.Rect(525, 180, 30, 30)

velocita_nemico = 50  # pixel per secondo
```

- I numeri dentro `Rect` indicano: posizione X, posizione Y, larghezza, altezza.
- La velocità controlla quanto rapidamente si muovono lungo il loro percorso.

---

## TODO2: crea le variabili che servono ai nemici

I nemici devono muoversi avanti e indietro, quindi serve sapere:
- Il **verso** del movimento (`1` o `-1`).
- La **distanza massima** che possono percorrere.
- Le coordinate di partenza (per calcolare il ritorno).

Esempio:
```python
verso = 1
distanza = 220
startx = nemico1.x
starty = nemico3.y
```

- `verso` indica la direzione (1 = avanti, -1 = indietro).
- `distanza` è quanto possono spostarsi prima di invertire il movimento.
- `startx` e `starty` servono per ricordare la posizione iniziale.

---

## TODO3: scrivi il movimento dei tre nemici

Ogni nemico si muove lungo un asse:
- **Nemico 1 e 2** si muovono orizzontalmente.
- **Nemico 3** si muove verticalmente.

Esempio:
```python
# Nemico 1
nemico1.x += verso * velocita_nemico * dt
if verso == 1 and nemico1.x >= startx + distanza:
    nemico1.x = startx + distanza
    verso = -1
if verso == -1 and nemico1.x <= startx:
    nemico1.x = startx
    verso = 1

# Nemico 2
nemico2.x += verso * velocita_nemico * dt
if verso == 1 and nemico2.x >= startx + distanza:
    nemico2.x = startx + distanza
    verso = -1
if verso == -1 and nemico2.x <= startx:
    nemico2.x = startx
    verso = 1

# Nemico 3
nemico3.y += verso * velocita_nemico * dt
if verso == 1 and nemico3.y >= starty + distanza:
    nemico3.y = starty + distanza
    verso = -1
if verso == -1 and nemico3.y <= starty:
    nemico3.y = starty
    verso = 1
```

---

## TODO4: gestisci le collisioni con i nemici

Controlla se il giocatore tocca uno dei nemici.  
Se sì, puoi far terminare il gioco o mostrare un messaggio di sconfitta.

Esempio:
```python
if player.colliderect(nemico1) or player.colliderect(nemico2) or player.colliderect(nemico3):
    print("Hai perso!")
    run = False
```

Puoi anche aggiungere un messaggio a schermo:
```python
font = pygame.font.SysFont(None, 80)
win.blit(font.render("Hai perso!", True, (255, 0, 0)), (430, 275))
```

---

![boh](../Immagini/Screenshot_labirintonuovo.png)
