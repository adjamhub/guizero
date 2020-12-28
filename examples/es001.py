from guizero import App, PushButton, Slider, Text

def saluta():
    print("Ciao a tutti")
    
app = App(title="Hello world")
message = Text(app,text="Ciao mondo!")
button = PushButton(app, text="dì ciao", command=saluta)
app.display()

