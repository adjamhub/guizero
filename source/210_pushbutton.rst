==========
PushButton
==========


Un oggetto `PushButton` rappresenta un pulsante con un testo o un'immagine, che quando una funzione quando viene premuto.


.. image:: images/pushbutton_windows.png


Contiene un oggetto `tkinter.Button`:


.. code:: python

    __init__(
        self,
        master,
        command=None,
        args=None,
        text="Button",
        image=None,
        pady=10,
        padx=10,
        grid=None,
        align=None,
        icon=None,
        visible=True,
        enabled=None,
        width=None,
        height=None)

E' possibile creare un oggetto `PushButton` (con un testo) con un codice tipo questo:

.. code:: python

    from guizero import App, PushButton
    def do_nothing():
        print("Button was pressed")

    app = App()
    button = PushButton(app, command=do_nothing)
    app.display()


Oppure un pulsante con un'immagine:

.. code:: python

    from guizero import App, PushButton
    def do_nothing():
        print("A picture button was pressed")

    app = App()
    button = PushButton(app, image="button.gif", command=do_nothing)
    app.display()


Per quanto riguarda i **tipi di immagine supportati** ricorda il discorso fatto sulle immagini qui: `108_images.html`.


Parametri iniziali
==================

Quando si crea un oggetto `PushButton`, **si deve specificare un master** e poi eventualmente altri parametri opzionali. I parametri sono:


========== ================ ========= ============ ========================================================================================
Parametro  Tipo             Default   Obbligatorio Descrizione
========== ================ ========= ============ ========================================================================================
master     App, Window, Box           Yes          Il contenitore a cui la widget appartiene
command    function         None      No           La funzione da eseguire quando un'opzione viene selezionata
align      string           None      No           Allineamento della widget nel suo contenitore: \\"top\\", \\"bottom\\", \\"left\\", \\"right\\".
args       List             None      No           Gli (eventuali) argomenti da passare alla funzione del parametro command
grid       List             None      No           Coordinate **[x,y]** della widget. Solo con layout grid.
image      string           None      No           Il percorso relativo dell'immagine da visualizzare
padx       int              10                     Padding orizzontale
pady       int              10                     Padding verticale
text       string           "Button"               Il testo da visualizzare sopra al pulsante
visible    boolean          True      No           Visibilità della widget
enabled    boolean          None      No           Se la widget è abilitata oppure no.
width      size             None      No           Larghezza della widget **in caratteri**, oppure \\"fill\\"
height     size             None      No           Altezza della widget **in caratteri**, oppure \\"fill\\"
========== ================ ========= ============ ========================================================================================



Metodi
======

Elenco alfabetico dei metodi disponibili nell'oggetto `PushButton`:


after(time, command, args=None)
    *time (int), command (function name), args (list of arguments)*
    
    Programma una chiamata **singola** alla funzione indicata nel parametro `command` dopo `time` millisecondi.


cancel(command)
    *command (function name)*
    
    Cancella una chiamata programmata a `command`.
    

destroy()
    Distrugge la widget.
    

disable()
    Disabilita la Box e tutte le widget al suo interno.

    
enable()
    Abilita la window e tutte le widget al suo interno.


focus()
    Da il focus alla Box e quindi agli oggetti in essa contenuti.

    
hide()
    Nasconde la widget.


image(image_source)
    *image_source (string)*
    
    Il percorso relativo dell'immagine da visualizzare.
    
    
padding(padx, pady)
    *padx (int), pady(int)*
    
    Permette di impostare il padding orizzontale e verticale tra il testo (o l'immagine) e i bordi del pulsante.

    
repeat(time, command, args=None)
    *time (int), command (function name), args (list of arguments)*
    
    Programma una chiamata **ripetuta** alla funzione indicata nel parametro `command` dopo ogni `time` millisecondi.


resize(width, height)
    *width (int), height (int)*
    
    Imposta larghezza e altezza del Box.
    
    
show()
    Visualizza il Box se prima era stata nascosto con `hide()`.


toggle()
    Cambia lo stato del pulsante da cliccato a non cliccato e viceversa.
    
    
update_command(command, args=None) 
    *command (function), args (list)*
    
    Aggiorna la funzione da chiamare quando si seleziona un'opzione.


    
Attributi
=========

Elenco degli attributi accessibili per l'oggetto `PushButton`:


=========== ================ ========================================================================================
Parametro   Tipo             Descrizione
=========== ================ ========================================================================================
align       string           Allineamento della widget nel suo contenitore: \\"top\\", \\"bottom\\", \\"left\\", \\"right\\".
bg          color            Il colore di sfondo della widget
enabled     boolean          Se la widget è abilitata oppure no.
font        string           Nome del font da utilizzare nella widget
grid        List             Coordinate **[x,y]** della widget. Solo con layout grid.
height      size             Altezza della widget **in caratteri**, oppure \\"fill\\".
master      App, Window, Box Il contenitore a cui la widget appartiene
text        string           Il testo del pulsante
text_size   int              Dimensione del font da utilizzare nella widget
text_color  color            Colore del font da utilizzare nella widget
value       string           Ritorna `1` se il pulsante è premuto, `0` altrimenti.
visible     boolean          Visibilità della widget
width       size             Larghezza della widget **in caratteri**, oppure \\"fill\\"
=========== ================ ========================================================================================

