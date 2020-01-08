======
Window
======

L'oggetto `Window` permette di creare nuove finestre in GuiZero.

.. image:: images/window.png

Contiene un oggetto `tkinter.TopLevel`


.. code:: python

    __init__(
        self, 
        master, 
        title="guizero", 
        width=500, 
        height=500, 
        layout="auto", 
        bg=None, 
        visible=True)

Per creare un oggetto `Window` basta scrivere una cosa tipo:

.. code:: python

    from guizero import App, Window
    app = App()
    window = Window(app)
    app.display()


Parametri iniziali
==================

Quando si crea un oggetto `Window`, **si deve specificare un master** e poi eventualmente altri parametri opzionali. I parametri sono:


========= ======= ========= ============ ===========================================================
Parametro Tipo    Default   Obbligatorio Descrizione
--------- ------- --------- ------------ -----------------------------------------------------------
master    App               Yes          La App a cui la Window appartiene
bg        color   None      No           Il colore di sfondo della window
height    int     500       No           L'altezza della window in pixels
layout    string  "auto"    No           Il tipo di layout. Può essere "auto" oppure "grid"
title     string  "guizero" No           Il titolo visualizzato sulla barra del titolo della window
width     int     500       No           La larghezza della windows in pixels
visible   boolean True      No           Se la window è visibile oppure no
========= ======= ========= ============ ===========================================================



Metodi
======

Elenco alfabetico dei metodi disponibili nell'oggetto `Window`:


add_tk_widget(tk_widget, grid=None, align=None, visible=True, enabled=None, width=None, height=None) 
    *tk_widget (tk), grid (list), align (str), visible (bool), enabled (bool), width (int), height (int)*
    
    Aggiunge una widget tk in una window GuiZero. PS: Funzionalità avanzata. Verrà utilizzata solo se necessario.
    

after(time, command, args=None)
    *time (int), command (function name), args (list of arguments)*
    
    Programma una chiamata **singola** alla funzione indicata nel parametro `command` dopo `time` millisecondi.
    

cancel(command)
    *command (function name)*
    
    Cancella una chiamata programmata a `command`.
    

destroy()
    Distrugge la widget.
    

disable()
    Disabilita la window e tutte le widget al suo interno.
    
    
enable()
    Abilita la window e tutte le widget al suo interno.
    
    
error(title, text)
    *title (str), text (str)*
    
    Visualizza un popup di errore con il titolo e il testo indicati.
    
    
exit_full_screen()
    Esce dalla visualizzazione fullscreen.
    
    
focus()
    Mette la widget in primo piano.
    

hide()
    Nasconde la widget.
    
    
info(title, text)
    *title (str), text (str)*
    
    Visualizza un popup informativo con il titolo e il testo indicati.

    
question(title, text, initial_value=None)
    *title (str), text (str), initial_value (str)*
    
    Visualizza un popup per una domanda con il titolo e il testo indicati e una casella per scrivere. Ritorna la stringa digitata dall'utente se preme `Ok`
    oppure `None` se preme `Cancel`.
    
    
repeat(time, command, args=None)
    *time (int), command (function name), args (list of arguments)*
    
    Programma una chiamata **ripetuta** alla funzione indicata nel parametro `command` dopo ogni `time` millisecondi.
    
    
select_file(title="Select file", folder=".", filetypes=[["All files", "*.*"]], save=False)
    *title (str), folder (str), filetypes (list), save (bool)*
    
    Ritorna una stringa contenente il percorso completo del file selezionato nel popup.
    
    
select_folder(title="Select folder", folder=".")
    *title (str), folder (str)*
    
    Ritorna una stringa contenente il percorso completo della cartella selezionata nel popup.
    

set_full_screen(keybind)
    *String*
    
    Imposta la widget in modalità fullscreen impostando anche il tasto con cui uscire dalla modalità (`ESC` di default)
    

show(wait = False)
    *wait (boolean)*
    
    Visualizza la window se prima era stata nascosta con `hide()`.
    
    
update()
    Forza l'aggiornamento dell'applicazione. Solitamente necessario se durante l'esecuzione si aggiungono o tolgono widget dal layout.
    

warn(title, text)
    *title (str), text (str)*
    
    Visualizza un popup di avviso con il titolo e il testo indicati.

    
yesno(title, text)
    *title (str), text (str)*
    
    Visualizza un popup di domanda di tipo Sì/No con il titolo e il testo indicati. Ritorna un valore booleano.
    

_on_close(command)_
    *_command (function name)_*
    
    Chiamata la funzione indicata quando l'utente prova a chiudere la finestra.
    
    
Attributi
=========

Elenco degli attributi accessibili per l'oggetto `Window`:

=========== ======== ===========================================================
Parametro   Tipo     Descrizione
----------- -------- -----------------------------------------------------------
bg          color    Il colore di sfondo della window
children    list     La lista delle widget contenute
enabled     boolean  Se la widget è abilitata oppure no
height      int      L'altezza della window in pixels
font        string   Nome del font da utilizzare nella widget
full_screen boolean  fullscreen oppure no. Falso inizialmente.
layout      string   Il tipo di layout. Può essere "auto" oppure "grid"
title       string   Il titolo visualizzato sulla barra del titolo della window
text_size   int      Dimensione del font da utilizzare nella widget
text_color  color    Colore del font da utilizzare nella widget
visible     boolean  Se la window è visibile oppure no
when_closed function Funzione da chiamare quando la `App` viene chiusa
width       int      La larghezza della windows in pixels
=========== ======== ===========================================================


Esempi
======


**Creating a Window object**

.. code:: python

    from guizero import App, Window
    app = App(title="My app", height=300, width=200)
    window = Window(title = "2nd Window", height=300, width=200)
    app.display()


**Showing and hiding a Window**

.. code:: python

    from guizero import App, Window, PushButton

    def open_window():
        window_2.show()

    app = App(title="My app", height=300, width=200)
    window = Window(app, title = "2nd Window", height=300, width=200)
    window.hide()

    open_button(app, text="open 2nd window", command=open_window)

    app.display()


Se vogliamo che una finestra diventi **modale** dobbiamo modificare il parametro opzionale `wait` della funzione show():

.. code:: python

    # ...
    def open_window():
        window_2.show(wait = True)
    # ...

    
