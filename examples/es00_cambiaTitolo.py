from guizero import App, PushButton, TextBox

def cambiaTitolo():
    app.title = testo.value
    testo.value = ""

app = App()
testo = TextBox(app)
pulsante = PushButton(app,
                      text="Inserisci un titolo e clicca il pulsante",
                      command=cambiaTitolo)
app.display()
