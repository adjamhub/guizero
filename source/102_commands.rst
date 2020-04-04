=======
Comandi
=======

Nella terminologia guizero **i comandi sono le funzioni che l'utente può abbinare ad un oggetto, da eseguire in risposta al suo evento predefinito**.

Ad esempio per un pulsante l'evento predefinito è il click su di esso e se il programmatore abbina come comando la funzione pippo(), 
quando l'utente clicca il pulsante, il codice della funzione pippo() viene eseguito.

Vediamo un esempio di codice in cui si abbina una funzione semplicissima ad un pulsante.

.. code:: python

    from guizero import App, Text, PushButton

    def saluta():
        text.value = "Ciao ciao ;)"

    app = App()
    text = Text(app, text="salutami cliccando il pulsante")
    button = PushButton(app, text="clicca qui", command=saluta)
    app.display()


Tutto qui! Provare per credere!
