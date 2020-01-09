========
Immagini
========

Alcune widget come la Picture e il PushButton permettono di utilizzare delle immagini nella applicazione grafica:

.. code:: python
    
    from guizero import App, Picture
    app = App()
    picture = Picture(app, image="test.gif")
    app.display()


In questo codice di esempio, il file `test.gif` si trova nella stessa cartella del file python che contiene quel codice. 
Il tipo di immagini supportate (es: GIF, JPG, PNG, etc...) dipende da come hai installato GuiZero e dal setup del tuo computer.



Tipi di immagini supportate
===========================

Tutti i sistemi operativi supportano nativamente le immagini di tipo `GIF`.

Windows e Linux supportano nativamente anche i file di tipo `PNG`.

Se hai installato le funzionalità aggiuntive per le immagini descritte nell'installazione e hai installato `PIL` (la Python Imaging Library), i tuoi programmi Python
supporteranno praticamente tutti i tipi di immagine.

GuiZero può comunque evidenziare quali tipi di immagine supporta eseguendo il seguente codice:

.. code:: python
    
    from guizero import system_config
    print(system_config.supported_image_types)


Se avete installato tutto quello che serve, i tipi di immagine supportati sono dunque: **GIF, Animated GIF, BMP, ICO, PNG, JPG, TIF**. 
Direi che sono abbastanza!!!



Ridimensionamento
=================

Quando si ridimensiona una finestra, le widget al suo interno vengono ridimensionate. Se `PIL` è installato, l'immagine si ridimensiona in maniera coerente con la finestra,
altrimenti NON si ridimensiona e viene ritagliata.



GIF animate
===========

Se `PIL` non è installato le GIF animate saranno visualizzate in modalità statica.

