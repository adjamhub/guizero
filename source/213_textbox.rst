=======
TextBox
=======

L'oggetto `TextBox` contiene una casella di testo il cui l'utente può digitare una stringa.


.. image:: images/textbox_windows.png


Contiene un oggetto `tkinter.Entry`


.. code:: python

    __init__(
        self,
        master,
        text="",
        width=10,
        height=1,
        grid=None,
        align=None,
        visible=True,
        enabled=None,
        multiline=False,
        scrollbar=False,
        command=None,
        hide_text=False)

        
Per utilizzare un oggetto `TextBox` basta scrivere un codice tipo questo:


.. code:: python

    from guizero import App, TextBox
    app = App()
    input_box = TextBox(app)
    app.display()


Parametri iniziali
==================

Quando si crea un oggetto `TextBox`, **si deve specificare un master** e poi eventualmente altri parametri opzionali. I parametri sono:


=========== ================ ========= ============ ========================================================================================
Parametro   Tipo             Default   Obbligatorio Descrizione
----------- ---------------- --------- ------------ ----------------------------------------------------------------------------------------
master      App, Window, Box           Yes          Il contenitore a cui la widget appartiene
align       string           None      No           Allineamento della widget nel suo contenitore: `"top"`, `"bottom"`, `"left"`, `"right"`.
grid        List             None      No           Coordinate `[x,y]` della widget. Solo con layout grid.
text        string           ""                     Il testo "pre-inserito" nella `TextBox`
visible     boolean          True      No           Visibilità della widget
enabled     boolean          None      No           Se la widget è abilitata oppure no.
width       size             None      No           Larghezza della widget in pixel, oppure `"fill"`
height      size             None      No           Altezza della widget in pixel, oppure `"fill"`
multiline   boolean          False     No           Se True, permette di inserire più linee di testo
scrollbar   boolean          False     No           Aggiunge la scrollbar verticale alla TextBox multiline
command     function         None                   La funzione da chiamare quando il testo cambia (con ZERO oppure 1 argomento: il testo)
hide_text   boolean          False                  Se True, nasconde il testo con `*` permettendo di digitare una password.
=========== ================ ========= ============ ========================================================================================



Metodi
======

Elenco alfabetico dei metodi disponibili nell'oggetto `TextBox`:


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


update_command(command)
    *command (function)*
    
    Aggiorna il nome della funzione da chiamare quando il testo viene modificato.



Attributi
=========

Elenco degli attributi accessibili per l'oggetto `TextBox`:


=========== ================ ========================================================================================
Parametro   Tipo             Descrizione
----------- ---------------- ----------------------------------------------------------------------------------------
align       string           Allineamento della widget nel suo contenitore: `"top"`, `"bottom"`, `"left"`, `"right"`.
bg          color            Il colore di sfondo della widget
enabled     boolean          Se la widget è abilitata oppure no.
font        string           Nome del font da utilizzare nella widget
grid        List             Coordinate `[x,y]` della widget. Solo con layout grid.
height      size             Altezza della widget in pixel, oppure `"fill"`.
hide_text   boolean          Se True, nasconde il testo con `*` permettendo di digitare una password.
master      App, Window, Box Il contenitore a cui la widget appartiene
text_size   int              Dimensione del font da utilizzare nella widget
text_color  color            Colore del font da utilizzare nella widget
value       string           Il testo corrente
visible     boolean          Visibilità della widget
width       size             Larghezza della widget in pixel, oppure `"fill"`
=========== ================ ========================================================================================



Esempi
======


**Creating a TextBox with default text**


.. code:: python

    from guizero import App, TextBox
    app = App()
    input_box = TextBox(app, text="Type here")
    app.display()


**Creating a password TextBox with hidden text**


.. code:: python

    from guizero import App, TextBox
    app = App()
    password_box = TextBox(app, hide_text=True)
    app.display()


**Creating a multi-line TextBox**


.. code:: python

    from guizero import App, TextBox
    app = App()
    input_box = TextBox(app, text="Type lines here", height=10, multiline=True)
    app.display()

    
**Creating a multi-line TextBox with scrollbar**


.. code:: python

    from guizero import App, TextBox
    app = App()
    input_box = TextBox(app, text="Type lines here", height=10, multiline=True, scrollbar=True)
    app.display()
