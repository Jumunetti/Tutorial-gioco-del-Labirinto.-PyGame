# 🧩 Lezione 4 – Schermate di vittoria e sconfitta

In questa lezione aggiungeremo due elementi fondamentali al nostro gioco:
- le **variabili di stato** (`font` e `condizione`);
- e le **schermate di fine gioco** che mostrano se il giocatore ha vinto o perso.

Alla fine del lavoro, il tuo gioco mostrerà a schermo il messaggio **"Hai vinto"** o **"Hai perso"** quando il giocatore raggiunge il traguardo o viene colpito da un nemico.

---

## 🎯 Obiettivi della lezione

1. Creare una variabile `font` per scrivere testi sullo schermo.  
2. Creare la variabile `condizione` per gestire se il giocatore ha vinto o perso.  
3. Mostrare il messaggio corrispondente alla fine del gioco (vittoria o sconfitta).

---

## 🧠 TODO1 – Variabili `font` e `condizione`

All’inizio del programma, subito dopo la sezione dei **colori**, trovi questo commento:

```python
#TODO1: scrivi la variabile font e la variabile condizione
```

Qui devi aggiungere due righe di codice:

```python
font = pygame.font.SysFont(None, 80)
condizione = 0
```

### 🔍 Spiegazione
- `pygame.font.SysFont(None, 80)` crea un oggetto **font** (stile di testo) di grandezza 80.  
  L’opzione `None` usa il font di default del sistema.  
- `condizione = 0` è una variabile che useremo per capire se il giocatore:
  - ha **perso** → `condizione = 1`
  - ha **vinto** → `condizione = 2`
  - è ancora in gioco → `condizione = 0`

---

## 🧩 TODO2 – Variabile `condizione` nelle collisioni

Nel codice del gioco ci sono già dei controlli per verificare se il **giocatore** tocca il **traguardo** (vittoria) o un **nemico** (sconfitta).  
Dentro a questi blocchi devi inserire la variabile `condizione`.

Esempio:

```python
# Controllo vittoria e sconfitta
if player.colliderect(goal):
    condizione = 2
    run = False  # il giocatore ha vinto

if player.colliderect(nemico):
    condizione = 1
    run = False  # il giocatore ha perso
```

### 🧠 Spiegazione
- Quando il giocatore **raggiunge il traguardo verde**, `condizione` diventa `2`.
- Quando **tocca un nemico rosso**, `condizione` diventa `1`.
- In entrambi i casi `run = False` serve per **fermare il ciclo di gioco**.

---

## 🖥️ TODO3 – Schermate di vittoria e sconfitta

Alla fine del loop principale (dopo aver disegnato tutti i rettangoli) trovi questo commento:

```python
#TODO3: scrivi la condizione per le schermate
```

Qui dobbiamo dire al gioco **quale testo mostrare a schermo** a seconda della variabile `condizione`.

Scrivi:

```python
if condizione == 1:
    win.blit(font.render("Hai perso", True, (255, 0, 0)), (430, 275))
elif condizione == 2:
    win.blit(font.render("Hai vinto", True, (0, 255, 0)), (430, 275))
```

### 🔍 Spiegazione
- `font.render("Hai perso", True, (255, 0, 0))` crea un testo rosso (“Hai perso”) come superficie.  
- `win.blit(...)` lo **disegna sullo schermo** alle coordinate indicate (in questo caso al centro).
- Il secondo `elif` fa la stessa cosa per il messaggio di vittoria.

---

## ✅ Risultato finale

Dopo aver completato i tre TODO, il tuo gioco:
1. mostrerà un messaggio di **vittoria** o **sconfitta** al termine della partita;
2. userà la variabile `condizione` per gestire lo stato di gioco;
3. sarà pronto per essere esteso con altri nemici o livelli!

---

## 💡 Suggerimento extra

Puoi aggiungere una **pausa prima di chiudere il gioco** dopo la vittoria o la sconfitta, ad esempio:

```python
pygame.time.wait(2000)  # aspetta 2 secondi prima di chiudere
```

oppure potresti creare una **nuova schermata di fine partita** con la possibilità di **ricominciare** — lo vedremo nelle lezioni successive!

---

✍️ **Obiettivo completato:** hai imparato a gestire le condizioni di vittoria e sconfitta e a visualizzare messaggi di testo con Pygame!
