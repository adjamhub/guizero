=================
Finestre Multiple
=================

Una applicazione GuiZero si basa su un'unica finestra principale, che è rappresentata dall'oggetto **App**. Se però vuoi aggiungere una seconda (o terza, o quarta, etc...)
finestra devi usare un oggetto **Window**.


Finestra Secondaria
===================

Quando crei una seconda finestra gli devi passare l'oggetto principale come primo elemento:

.. code:: python
    
    from guizero import App, Window

    app = App(title="Main window")
    window = Window(app, title="Second window")

    app.display()


Aggiungere widget alla seconda window è come aggiungerle alla finestra principale: hai solo bisogno di specificare il nome della finestra:

.. code:: python
    
    from guizero import App, Window, Text

    app = App(title="Main window")
    window = Window(app, title="Second window")
    text = Text(window, text="This text will show up in the second window")

    app.display()


Aprire e chiudere finestre
==========================


Quando un oggetto Window viene istanziata, viene immediatamente visualizzato sullo schermo. Si può controllare la visibilità di un oggetto tramite le funzioni ``show()``
e ``hide()``. Nell'esempio seguente si crea una finestra con due pulsanti per mostrare e nascondere la finestra secondaria.


.. code:: python

    from guizero import App, Window, PushButton

    def open_window():
        window.show()

    def close_window():
        window.hide()

    app = App(title="Main window")

    window = Window(app, title="Second window")
    window.hide()

    open_button = PushButton(app, text="Open", command=open_window)
    close_button = PushButton(window, text="Close", command=close_window)

    app.display()


Finestre modali
===============

Quando una finestra secondaria viene aperta (tramite definizione o con chiamata esplicita al comando show()), viene aperta di fianco alla finestra principale.
Le finestre di questo tipo vengono definite **non modali**. Una **finestra modale** infatti è una finestra che si sovrappone forzatamente alla sua finestra principale.

Fate attenzione ad usarle!

Questo tipo di finestre sono fastidiose! Usatele solo per una reale necessità: un avviso importante, una scelta dell'utente che può compromettere i dati. Poco altro.

Si attivano passando il valore ``True`` al parametro opzionale ``wait``.

.. code:: python

    # Apre una finestra modale
    window.show(wait=True)



