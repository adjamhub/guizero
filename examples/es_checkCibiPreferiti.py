from guizero import App, Text, CheckBox

def visualizzaCibiPreferiti():
    frase = "Le cose che ti piacciono: "
    if pasta.value == True:
        frase += "pasta "
    if pizza.value == True:
        frase += "pizza "
    if dolci.value == True:
        frase += "dolci "
    if gelato.value == True:
        frase += "gelato "
    if fritto.value == True:
        frase += "fritto "
    if broccoli.value == True:
        frase += "broccoli "
    
    cosaSiMangia.value = frase
        

app = App(title="Quali cibi preferisci?")

pasta = CheckBox(app, text="Pasta", command=visualizzaCibiPreferiti)
pizza = CheckBox(app, text="Pizza", command=visualizzaCibiPreferiti)
dolci = CheckBox(app, text="Dolci", command=visualizzaCibiPreferiti)
gelato = CheckBox(app, text="Gelato", command=visualizzaCibiPreferiti)
fritto = CheckBox(app, text="Fritto", command=visualizzaCibiPreferiti)
broccoli = CheckBox(app, text="Broccoli", command=visualizzaCibiPreferiti)

cosaSiMangia = Text(app, text="")

app.display()