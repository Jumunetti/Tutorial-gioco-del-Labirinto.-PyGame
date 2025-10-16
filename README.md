# Classe `Rect` in Pygame

La classe `Rect` è una delle componenti fondamentali di Pygame per la gestione delle aree rettangolari, molto utile per la gestione di sprite, collisioni, posizionamento e ritaglio.

---

## Cos'è `Rect`

`Rect` rappresenta un rettangolo, definito da quattro valori interi:

- `x`: la coordinata orizzontale (sinistra)
- `y`: la coordinata verticale (superiore)
- `width`: la larghezza del rettangolo
- `height`: l'altezza del rettangolo

---

## Creazione di un `Rect`

Puoi creare un oggetto `Rect` in vari modi:

```python
import pygame

# Creazione da coordinate e dimensioni
rect1 = pygame.Rect(10, 20, 100, 50)

# Creazione da una tupla (x, y, width, height)
rect2 = pygame.Rect((10, 20, 100, 50))

# Creazione da un'altra Rect (copia)
rect3 = pygame.Rect(rect1)
