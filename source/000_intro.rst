===================
Che cosa è guizero?
===================


guizero è una libreria Python3 per creare semplici GUI. E da qui si ricomincia: che cosa è una GUI?
GUI è l'acronimo di *Graphical User Interface* ovvero una applicazione che presenta una interfaccia
grafica come quella tipica dei sistemi operativi moderni.

.. image:: images/have-a-go.png


Le sue caratteristiche principali sono:

* Funziona semplicemente grazie alla libreria GUI predefinita **Tkinter**, di cui rappresenta una reimplementazione.
* Elimina dalle opzioni tutti i dettagli *difficili* della libreria Tkinter.
* Utilizza un semplice sistema di naming per identificare tutti gli oggetti grafici.
* E' abbastanza flessibile per realizzare progetti complessi, ma comunque semplice da capire per gli studenti.
* E' Completa di documentazione ed esempi (semplici e in Italiano, grazie al prof).
* E' In grado di generare messaggi di errore addizionali.


Vediamo un esempio di codice:

.. code:: python

    from guizero import App, Text, PushButton
    app = App(title="guizero")
    intro = Text(app, text="Copia il codice su un file .py per testare guizero!")
    ok = PushButton(app, text="Ok")
    app.display()

Spero tutto questo sia abbastanza per invogliarvi allo studio della libreria :)
