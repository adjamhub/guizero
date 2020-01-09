======
Eventi
======

Oltre agli eventi predefiniti, catturabili come abbiamo visto con `command`, è possibile intercettare una serie di eventi
grafici particolari che accadono alle widgets GuiZero e fare in modo che i nostri programmi reagiscano a questi.

Questi eventi sono:

============================ =================================================
Evento                       Descrizione
---------------------------- -------------------------------------------------
`when_clicked`               Quando si fa click sopra un oggetto
`when_left_button_pressed`   Quando si tiene premuto il tasto sx del mouse
`when_left_button_released`  Quando si rilascia il tasto sx del mouse
`when_right_button_pressed`  Quando si tiene premuto il tasto dx del mouse
`when_right_button_released` Quando si rilascia il tasto dx del mouse
`when_key_pressed`           Quando si tiene premuto un tasto
`when_key_released`          Quando si rilascia un tasto
`when_mouse_enters`          Quando il puntatore del mouse va sopra un oggetto
`when_mouse_leaves`          Quando il puntatore del mouse esce da un oggetto
`when_mouse_dragged`         Quando si trascina un oggetto con il mouse
============================ =================================================


Gli eventi vengono impostati assegnando loro una funzione:

.. code:: python

    def do_this():
        print("The widget was clicked")

    widget.when_clicked = do_this


Dati degli eventi
=================

La funzione chiamata può contenere opzionalmente un parametro che, se presente, sarà riempito dall'evento con una serie di dati sull'evento stesso.

Questi dati sono:

* ``widget``: la widget che ha scatenato l'evento

* ``tk_event``: l'evento tkinter abbinato (speriamo non ci interessi...)

* ``key``:  il tasto che (eventualmente) ha scatenato l'evento

* ``x``: la posizione x del mouse (relativa alla widget) quando l'evento è occorso

* ``y``: la posizione y del mouse (relativa alla widget) quando l'evento è occorso

* ``display_x``: la posizione x del mouse (relativa allo schermo) quando l'evento è occorso
 
* ``display_y``: la posizione y del mouse (relativa allo schermo) quando l'evento è occorso


.. code:: python

    def clicked(event_data):
        print("widget clicked = " + event_data.widget)
        print("mouse position = " + event_data.x + "." + event_data.y)

    widget.when_clicked = clicked


Esempio
=======


Cambia il colore di sfondo di una text box quando il mouse ci passa sopra


.. code:: python

    from guizero import App, TextBox

    def highlight():
        text_box.bg = "lightblue"

    def lowlight():
        text_box.bg = "white"

    app = App()
    text_box = TextBox(app)

    # When the mouse enters the TextBox
    text_box.when_mouse_enters = highlight
    # When the mouse leaves the TextBox
    text_box.when_mouse_leaves = lowlight

    app.display()
    

