========
CheckBox
========

L'oggetto `CheckBox` visualizza (appunto) una checkbox, ovvero una casella spuntabile che può essere `ticked` oppure no.


.. image:: images/checkbox_windows.png


Contiene un oggetto `tkinter.Checkbutton`


.. code:: python

    __init__(
        self,
        master,
        text="",
        command=None,
        grid=None,
        align=None,
        args=None,
        visible=True,
        enabled=None,
        width=None,
        height=None)

Per utilizzare un oggetto `CheckBox` basta scrivere un codice tipo questo:

.. code:: python

    from guizero import App, CheckBox
    app = App()
    checkbox = CheckBox(app, text="Add extra glitter")
    app.display()


Parametri iniziali
==================

Quando si crea un oggetto `CheckBox`, **si deve specificare un master e un text** e poi eventualmente altri parametri opzionali. I parametri sono:


========== ================ ========= ============ ========================================================================================
Parametro  Tipo             Default   Obbligatorio Descrizione
========== ================ ========= ============ ========================================================================================
master     App, Window, Box           Yes          Il contenitore a cui la widget appartiene
text       string                     Yes          Il testo da visualizzare nella checkbox
align      string           None      No           Allineamento della widget nel suo contenitore: \\"top\\", \\"bottom\\", \\"left\\", \\"right\\".
command    function         None      No           La funzione da eseguire quando un'opzione viene selezionata
args       List             None      No           Gli (eventuali) argomenti da passare alla funzione del parametro command
grid       List             None      No           Coordinate **[x,y]** della widget. Solo con layout grid.
visible    boolean          True      No           Visibilità della widget
enabled    boolean          None      No           Se la widget è abilitata oppure no.
width      size             None      No           Larghezza della widget **in caratteri**, oppure \\"fill\\"
height     size             None      No           Altezza della widget **in caratteri**, oppure \\"fill\\"
========== ================ ========= ============ ========================================================================================


Metodi
======

Elenco alfabetico dei metodi disponibili nell'oggetto `CheckBox`:



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


repeat(time, command, args=None)
    *time (int), command (function name), args (list of arguments)*
    
    Programma una chiamata **ripetuta** alla funzione indicata nel parametro `command` dopo ogni `time` millisecondi.


resize(width, height)
    *width (int), height (int)*
    
    Imposta larghezza e altezza del Box.
    
    
show()
    Visualizza il Box se prima era stata nascosto con `hide()`.


toggle()
    Se la casella è spuntata, la deseleziona e viceversa
    

update_command(command, args=None) 
    *command (function), args (list)*
    
    Aggiorna la funzione da chiamare quando si seleziona un'opzione.



Attributi
=========

Elenco degli attributi accessibili per l'oggetto `CheckBox`:


=========== ================ ========================================================================================
Parametro   Tipo             Descrizione
=========== ================ ========================================================================================
align       string           Allineamento della widget nel suo contenitore: \\"top\\", \\"bottom\\", \\"left\\", \\"right\\".
bg          color            Il colore di sfondo della widget
enabled     boolean          Se la widget è abilitata oppure no.
font        string           Nome del font da utilizzare nella widget
grid        List             Coordinate **[x,y]** della widget. Solo con layout grid.
height      size             Altezza della widget in pixel, oppure \\"fill\\".
master      App, Window, Box Il contenitore a cui la widget appartiene
text        string           Il testo associato alla `CheckBox`.
text_size   int              Dimensione del font da utilizzare nella widget
text_color  color            Colore del font da utilizzare nella widget
value       string           Vale `1` se la casella è spuntata, `0` altrimenti.
value_text  string           Il testo associato con l'opzione selezionata.
visible     boolean          Visibilità della widget
width       size             Larghezza della widget **in caratteri**, oppure \\"fill\\"
=========== ================ ========================================================================================


Esempi
======


**Creating multiple CheckBoxes**


.. code:: python

    from guizero import App, CheckBox
    app = App()
    glitter = CheckBox(app, text="Add glitter")
    sparkles = CheckBox(app, text="Add sparkles")
    app.display()


    
**Calling a function when a CheckBox value changes**


.. code:: python

    from guizero import App, Text, CheckBox, TextBox
    def calculate_extras():
        total = 0
        if syrup.value == 1:
            total += 20
        if sprinkles.value == 1:
            total += 10
        if cream.value == 1:
            total += 50
        cost.value = total

    app = App()

    questions = Text(app, text="What would you like with your coffee?")

    syrup = CheckBox(app, text="Caramel syrup (20p)", command=calculate_extras)
    sprinkles = CheckBox(app, text="Chocolate sprinkles (10p)", command=calculate_extras)
    cream = CheckBox(app, text="Whipped cream (50p)", command=calculate_extras)

    cost_of_extras = Text(app, text="Cost of extras:")
    cost = TextBox(app, text="0")

    app.display()


.. image:: images/checkbox_function_windows.png

