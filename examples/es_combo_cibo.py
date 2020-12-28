from guizero import App, Combo, Text

def visualizzaCibo(cibo):
    testo.value = "Hai selezionato " + cibo
    return
    
app = App(title="sempre cibo...")
combo = Combo(app, options=["Beef", "Chicken", "Fish", "Vegetarian"],command=visualizzaCibo)
testo = Text(app)

app.display()
