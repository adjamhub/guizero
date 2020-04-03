===============
Dimensionamento
===============

In GuiZero è possibile impostare la larghezza (``width``) e l'altezza (``height``) delle widgets.

L'unità di misura di queste proprietà può essere in pixel o in caratteri (a seconda se la widget può contenerne). Alcune
widget inoltre possono anche essere impostate a riempire (``fill``) lo spazio disponibile.

.. code:: python

    from guizero import App, PushButton, Slider, ListBox

    app = App()

    # A PushButton's size is noted in characters
    button = PushButton(app, width=30, height=5)

    # A Slider's size is noted in pixels
    slider = Slider(app, width=300, height=30)

    # Some widgets such as ListBox can also be told to fill all the available space
    listbox = ListBox(app, width="fill", height="fill")

    app.display()


Vediamo una tabella riassuntiva (soprattutto utile da riconsultare quando necessario) che ci dice quali unità di misura supportano le varie widgets.

====================== ======================== ==== 
Widget                 Characters or Pixels     Fill                                                                   
====================== ======================== ==== 
Box                    Pixels                   Yes 
ButtonGroup            Characters               Yes
CheckBox               Characters               Yes                                                                         
Combo                  Characters               Yes                                                                          
ListBox                Pixels                   Yes                                                                          
Picture                Pixels                   No   
PushButton             Characters               Yes                                                                         
PushButton with image  Pixels                   No   
Slider                 Pixels                   Yes                                                                          
Text                   Characters               Yes                                                                          
TextBox                Characters               Yes  
Waffle                 Pixels                   No                                                                           
====================== ======================== ==== 


