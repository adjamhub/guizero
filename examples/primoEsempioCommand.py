from guizero import App, Text, PushButton

def saluta():
    text.value = "Ciao ciao ;)"

app = App()
text = Text(app, text="salutami cliccando il pulsante")
button = PushButton(app, text="clicca qui", command=saluta)
app.display()
