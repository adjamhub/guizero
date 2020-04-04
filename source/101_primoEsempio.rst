========================
Primi esempi con GuiZero
========================


All'inizio di ogni programma con guizero devi scegliere gli oggetti grafici che vuoi utilizzare e importarli nel programma:


.. code:: python
    
    from guizero import App, PushButton, Slider
    

Nell'esempio sopra sono stati importati 3 oggetti: *App*, *PushButton* e *Slider*.

Tutti i programmi guizero iniziano con una *main window* che viene definita **App**. La struttura tipica di ogni applicazione guizero è:

#. Crei un oggetto di tipo App

#. Definisci l'interfaccia grafica contenuta in esso (pulsanti, etichette, etc...)

#. Visualizza l'oggetto di tipo App

Vediamo un esempio di codice:


.. code:: python
    
    from guizero import App
    app = App(title="Hello world")
    app.display()

    
Salva il codice ed esegui! Ecco fatto!!!



Aggiungere widgets
==================


Le **widget** sono gli oggetti grafici che appaiono in una GUI, come i pulsanti, gli slider, le caselle di spunta, ecc...

Dal punto di vista della programmazione, una widget è dunque un oggetto (un'istanza) di una classe grafica. Essa va inserita in una main window,
indicandolo in fase di istanziazione:


.. code:: python

    from guizero import App, Text
    app = App(title="Hello world")
    message = Text(app, text="Welcome to the Hello world app!")
    app.display()
    
Eseguendo questo codice si ottiene:

.. image:: images/hello-world.png


Diamo un occhio all'oggetto `Text` più da vicino:

.. code:: python

    message = Text(app, text="Welcome to the Hello world app!")


* ``message`` sarebbe la variabile che contiene l'oggetto di tipo `Text`

* ``Text`` è il tipo di oggetto. E' una widget che visualizza un pò testo sullo schermo. In italiano di solito si traduce con `Etichetta`.

* ``app`` è l'oggetto di tipo `App` (Main Window) che conterrà l'etichetta.

* ``text="Welcome to the Hello world app!"`` il testo da visualizzare.


E questo è quanto per adesso! 

Per imparare più cose sull'oggetto Text e su tutte le altre widget vi basterà leggere la documentazione su di esse.

