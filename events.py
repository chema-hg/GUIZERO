# Import the GUI widgets that you'll be using, and create the 'app' for your program.
from guizero import App, TextBox, PushButton, Text, info, Window
app = App(title="Main Window")

# New password window
window = Window(app, title="password window")
window.hide()

# Function definitions for your events go here.

#Evento para que cuando se pase por el Txtbox del nombre se encienda y se apague.
def highlight():
    txt_name.bg = "lightblue"

def lowlight():
    txt_name.bg = "white"
#----------------------------------------------------------------------------------------
# to open or close the second window

def open_window():
    window.show()


def close_window():
    window.hide()
#-------------------------------------------------------------------------------------

def btn_verifpass_clicked():
    if txt_passwd.value == txt_repasswd.value:
        info("Password OK", "All perfect")
    else:
        info("Password NOK", "Passwords do not match, retype them")


def btn_go_clicked():
    info("Greetings", "Hello, " + txt_name.value +
         " - I hope you and your pet " + txt_pet.value + " are having a good day")


# Your GUI widgets go here
# first window code
lbl_name = Text(app, text="Hello. What's your name?")
txt_name = TextBox(app)
lbl_pet = Text(app, text="What's the name of your pet?")
txt_pet = TextBox(app)
btn_go = PushButton(app, command=btn_go_clicked, text="Done")
btn_passwd = PushButton(app, command=open_window, text="Change password")
#-------------------------------------------------------------------------------
# second window code
lbl_passwd = Text(window, text="Enter the new password")
txt_passwd = TextBox(window, hide_text=True)
lbl_repasswd = Text(window, text="Repeat the password")
txt_repasswd = TextBox(window, hide_text=True)
btn_verify_psswd = PushButton(
    window, command=btn_verifpass_clicked, text="check")
#--------------------------------------------------------------------------------
#evento para un widget: encender y apagar el fondo de un cuadro de texto.
# When the mouse enters the TextBox
txt_name.when_mouse_enters = highlight
# When the mouse leaves the TextBox
txt_name.when_mouse_leaves = lowlight


# Show the GUI on the screen
app.display()
