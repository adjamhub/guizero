from guizero import App, ButtonGroup, Text

def update_text():
    voceSelezionata.value = activities.value

app = App()
Text(app,"Seleziona il tuo sport preferito")
activities = ButtonGroup(app,
                         options=["calcio", "basket", "volley", "rugby","divano"],
                         command=update_text)

voceSelezionata = Text(app, text=".....")
app.display()