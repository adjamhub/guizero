from guizero import App, ListBox, Text

def visualizzaCibo(cibo):
    testo.value = "Hai selezionato " + cibo
    return

app = App()
listbox = ListBox(app, items=["Beef", "Chicken", "Fish", "Vegetarian"], command=visualizzaCibo)
testo = Text(app)

app.display()
