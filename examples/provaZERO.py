from guizero import App,BoxPushButton, Text

def show():
    print("width:",b1.width)
    print("height:",b1.height)
    return

a = App(width=300,height=400,title="keypad")

b1 = PushButton(a,text="1",command=show, width=10, height=10)
b2 = PushButton(a,text="2")

a.display()