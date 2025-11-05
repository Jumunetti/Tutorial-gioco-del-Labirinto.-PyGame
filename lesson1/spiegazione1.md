
## TODO1: crea 2 Rect che si toccano oppure no

I `Rect` in Pygame rappresentano rettangoli che possono essere usati per disegnare forme o rilevare collisioni.  
Qui devi creare **due rettangoli**: puoi posizionarli in modo che si tocchino oppure no.

Esempio:
```python
rect1 = pygame.Rect(200, 200, 100, 100)  # primo rettangolo
rect2 = pygame.Rect(350, 200, 100, 100)  # secondo rettangolo
```

- Il primo e secondo numero indicano le coordinate (x, y) del rettangolo.
- Gli ultimi due valori sono larghezza e altezza.
- Se vuoi che **si tocchino**, puoi impostare le coordinate in modo che i bordi si incontrino:
  ```python
  rect2 = pygame.Rect(300, 200, 100, 100)
  ```

---

## TODO2: scrivi una condizione che dice se i 2 Rect si toccano

Pygame offre un metodo semplice per controllare se due rettangoli si sovrappongono:  
`colliderect()`.

Esempio:
```python
if rect1.colliderect(rect2):
    print("I rettangoli si toccano!")
else:
    print("I rettangoli NON si toccano.")
```

- `colliderect()` restituisce **True** se i due rettangoli si intersecano o si toccano.

![attaccato](Immagini/Screenshot_attaccato.png)

- `colliderect()` restituisce **False** se i due rettangoli non si intersecano o non si toccano.

![staccato](Immagini/Screenshot_labirinto.png)

- Puoi anche usare questa condizione per mostrare un messaggio a schermo.

---

## TODO3: scrivi la parte per far apparire a schermo i Rect

Per disegnare i rettangoli sulla finestra, usa `pygame.draw.rect()` dopo aver riempito lo schermo con un colore di sfondo.

Esempio:
```python
win.fill(BLACK)  # sfondo nero

pygame.draw.rect(win, BLUE, rect1)   # primo rettangolo blu
pygame.draw.rect(win, GREEN, rect2)  # secondo rettangolo verde
```

Puoi anche cambiare colore se si toccano:
```python
if rect1.colliderect(rect2):
    pygame.draw.rect(win, RED, rect1)
    pygame.draw.rect(win, RED, rect2)
else:
    pygame.draw.rect(win, BLUE, rect1)
    pygame.draw.rect(win, GREEN, rect2)
```


