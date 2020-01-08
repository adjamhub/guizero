====
Text
====

L'oggetto `Text` visualizza un testo non modificabile, una etichetta utile per titoli, descrizioni o istruzioni.

.. image:: images/text_windows.png

Contiene un oggetto `tkinter.Label`

.. code:: python

    __init__(
        self,
        master,
        text="",
        size=12,
        color="black",
        bg=None,
        font="Helvetica",
        grid=None,
        align=None,
        visible=True,
        enabled=None,
        width=None,
        height=None)

        
Per utilizzare un oggetto `Text` basta scrivere un codice tipo questo:


.. code:: python

    from guizero import App, Text
    app = App()
    text = Text(app, text="Hello World")
    app.display()


Parametri iniziali
==================

Quando si crea un oggetto `Text`, **si deve specificare un master** e poi eventualmente altri parametri opzionali. I parametri sono:


=========== ================ ========= ============ ========================================================================================
Parametro   Tipo             Default   Obbligatorio Descrizione
----------- ---------------- --------- ------------ ----------------------------------------------------------------------------------------
master      App, Window, Box           Yes          Il contenitore a cui la widget appartiene
align       string           None      No           Allineamento della widget nel suo contenitore: `"top"`, `"bottom"`, `"left"`, `"right"`.
color       color            black                  Il colore del testo scritto.
grid        List             None      No           Coordinate `[x,y]` della widget. Solo con layout grid.
size        int              12                     La dimensione del font
visible     boolean          True      No           Visibilità della widget
enabled     boolean          None      No           Se la widget è abilitata oppure no.
width       size             None      No           Larghezza della widget in pixel, oppure `"fill"`
height      size             None      No           Altezza della widget in pixel, oppure `"fill"`
=========== ================ ========= ============ ========================================================================================


Metodi
======

Elenco alfabetico dei metodi disponibili nell'oggetto `Slider`:


after(time, command, args=None)
    *time (int), command (function name), args (list of arguments)*
    
    Programma una chiamata **singola** alla funzione indicata nel parametro `command` dopo `time` millisecondi.
        

append(text)
    *text (string)*
    
    Aggiunge il testo fornito alla fine del testo contenuto nella widget.

    
cancel(command)
    *command (function name)*
    
    Cancella una chiamata programmata a `command`.
    

clear()
    Cancella il testo

    
destroy()
    Distrugge la widget.
    

disable()
    Disabilita la Widget.
    
    
enable()
    Abilita la Widget.
    

focus()
    Da il focus alla Widget.
    
    
hide()
    Nasconde la widget.


repeat(time, command, args=None)
    *time (int), command (function name), args (list of arguments)*
    
    Programma una chiamata **ripetuta** alla funzione indicata nel parametro `command` dopo ogni `time` millisecondi.


resize(width, height)
    *width (int), height (int)*
    
    Imposta larghezza e altezza del Box.
    
    
show()
    Visualizza il Box se prima era stata nascosto con `hide()`.


Attributi
=========

Elenco degli attributi accessibili per l'oggetto `Text`:


=========== ================ ========================================================================================
Parametro   Tipo             Descrizione
----------- ---------------- ----------------------------------------------------------------------------------------
align       string           Allineamento della widget nel suo contenitore: `"top"`, `"bottom"`, `"left"`, `"right"`.
bg          color            Il colore di sfondo della widget
enabled     boolean          Se la widget è abilitata oppure no.
font        string           Nome del font da utilizzare nella widget
grid        List             Coordinate `[x,y]` della widget. Solo con layout grid.
height      size             Altezza della widget in pixel, oppure `"fill"`.
master      App, Window, Box Il contenitore a cui la widget appartiene
text_size   int              Dimensione del font da utilizzare nella widget
text_color  color            Colore del font da utilizzare nella widget
value       string           Il testo corrente
visible     boolean          Visibilità della widget
width       size             Larghezza della widget in pixel, oppure `"fill"`
=========== ================ ========================================================================================

