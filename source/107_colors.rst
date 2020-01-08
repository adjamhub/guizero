======
Colori
======

In GuiZero si possono impostare i colori in tre modi. Usando:

#. il nome del colore (in inglese). Es: `white`

#. il valore esadecimale #RGB. Es: `#ffffff`

#. la tupla dei valori RGB. Es: `(255,255,255)`


I colori possono essere utilizzati sia come parametri iniziali...

.. code:: python
    
    app = App(bg = "red")
    app = App(bg = "#ff0000")
    app = App(bg = (255, 0, 0))

... che come proprietà.

.. code:: python
    
    text = Text(app, text = "hi")
    text.text_color = "green"
    text.text_color = "#00ff00"
    text.text_color = (0, 255, 0)

Se un colore viene impostato con il nome del colore, rimane memorizzato così. Allo stesso modo funziona con il valore esadecimale.
La tupla dei valori RGB è invece solo un diverso metodo di memorizzazione per il valore esadecimale: se un colore è impostato tramite una tupla di valori RGB,
verrà memorizzato come un valore decimale #RGB.


Nomi dei colori
===============

Alcuni colori possono essere impostati con il loro nome inglese, per esempio:

* `white`

* `black`

* `red`

* `green`

* `blue`

* `yellow`

Una lista completa dei nomi dei colori è una cosa semplice e complessa allo stesso tempo: se volete una strada semplice, diciamo che praticamente tutti i nomi dei colori
che conoscete, ci sono! Quindi pensate al colore che vi interessa e scrivetelo in inglese minuscolo e il gioco è fatto!

Se volete la soluzione più completa ma allo stesso tempo più complessa, vi propongo un esercizio: al link seguente trovate un file CSV contenente 4 colonne di valori:
il nome ufficiale del colore e i valori RGB corrispondenti. Scaricate il file e scrivete un programma che lo carica e produce una griglia di etichette (oggetti Text)
con sfondo il colore che potete ricavare dai valori RGB e sopra scritto in nero o in bianco il nome del colore con vicino la tupla dei valori (R,G,B).



Valori Esadecimali RGB (rgb hex)
================================

Un valore esadecimale RGB per un colore è un numero esadecimale di 6 cifre, che inizia con il simbolo `#` e che utilizza le prime 2 cifre per il rosso, le seconde 2 per
il verde e le ultime 2 per il blu. Ogni cifra esadecimale è un valore che va da `0` a `f` (maiuscolo o minuscolo).

Ecco alcuni esempi:

* white = `#ffffff`

* black = `#000000`

* red = `#ff0000`

* green = `#00ff00`

* blue = `#0000ff`

* yellow = `#ffff00`


Ovviamente si possono mischiare rosso, verde e blu a piacere per ottenere qualsiasi colore nella sfumatura preferita. 
In questa notazione si possono ottenere 16.777.216 colori diversi (e fra uno di questi ci sarà pure il vostro colore preferito, no?)

A questo punto vi propongo un nuovo esercizio: etichetta vuota e tre caselle di testo per inserire i tre valori RGB. Quando clicchi su un pulsante l'etichetta diventa
dello sfondo del colore corrispondente alla sequenza RGB!


Tuple RGB
=========

La tupla dei colori `(red, green, blue)` deve contenere 3 elementi nell'ordine RED, GREEN, BLUE e ognuno deve essere un valore tra 0 e 255. Ad esempio:


* white = (255, 255, 255)

* black = (0, 0, 0)

* red = (255, 0, 0)

* green = (0, 255, 0)

* blue = (0, 0, 255)

* yellow = (255, 255, 0)

