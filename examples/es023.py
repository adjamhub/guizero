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

pasta = CheckBox(app, text="pulsante visualizza", command=inserisciPulsante)
pizza = CheckBox(app, text="pulsante esci", command=inserisciPulsante)
dolci = CheckBox(app, text="pulsante", command=inserisciPulsante)

cosaSiMangia = Text(app, text="")

app.display()
