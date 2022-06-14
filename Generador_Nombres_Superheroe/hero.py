from guizero import *

raiz = App(title="Super Hero name generator", width=550, height=580)

# ----------------------------------------------------------------------


def make_hero_name():
    adjetivo = btn_adjetivos.value
    color = color_escojido.value
    animal = btn_animales.value
    friend = listbox.value
    hero = adjetivo + " " + color + " " + animal + " " + friend + "'s dude"
    lbl_output.value = "You are... the " + hero + "."


def make_dark_mode():
    if btl_darkmode.value:
        raiz.bg = "black"
        raiz.text_color = "white"

    else:
        raiz.bg = "white"
        raiz.text_color = "black"


# ----------------------------------------------------------------------
# insert an image
image = Picture(raiz, image="hero.png")
# ------------------------------------------------------------------------

label1 = Text(raiz, text="Choose an adjective...")

btn_adjetivos = Combo(raiz, options=("Amazing", "Bonny",
                                     "Charming", "Delightful", "Lovely", "Curious"))

label2 = Text(raiz, text="Enter a colour?")

color_escojido = TextBox(raiz)

label3 = Text(raiz, text="Pick an Animal")
btn_animales = ButtonGroup(raiz, options=[
                           "Aardvark", "Badger", "Cat", "Dolphin", "Velociraptor", "Mouse", "Ant"])

label4 = Text(raiz, text="Choose a friend for our hero")
listbox = ListBox(raiz, items=["Spiderman", "Superman",
                               "Batman", "IronMan"], width=100, height=80)

btn_generar = PushButton(raiz, text="Make me a Hero!", command=make_hero_name)

lbl_output = Text(raiz, "A hero name will appear here")


# -----------------------------------------------------------------------------------------------------
# Dark mode
btl_darkmode = CheckBox(raiz, text="Dark mode",
                        align="left", command=make_dark_mode)

raiz.display()
