# import ----------------------

from guizero import  App, Drawing, Text

# functions ------------------

def draw_image():
    picture.clear()
    picture.image(0,0,"image.png")
    picture.text(20, 100, inside_test.value)

# variables -------------------

# app -------------------------

app = App("Annotate Tool")
text = Text(app, text="Annotate below")
picture = Drawing(app, width="fill", height="fill")
inside_test = Text(app, text="test")

draw_image()

app.display()
