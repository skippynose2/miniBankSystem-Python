from appJar import gui
import ATM as ATM
app = gui()



#Input Feilds
app.startSubWindow("Login")
app.addLabelEntry("User Name")
app.addLabelSecretEntry("Password")


def Manager():
    app.startSubWindow("Demo")
    app.addLabel("l1", "Press the button to close this window")
    # set the button's name to match the SubWindow's name
    app.addNamedButton("CLOSE", "Demo", app.hideSubWindow)
    app.showSubWindow("Demo", hide=True)

def LoginBtn(button):
    if button == "Cancel":
        app.stop()
    else:
        user = app.getEntry("User Name")
        session = ATM.Control(user)
        pwd = app.getEntry("Password")
        session.Login(pwd)
        if session.Login(pwd) == 1:
            Manager()
        else:
            print("Nope")

app.addButtons(["Submit", "Cancel"], LoginBtn)
app.go(startWindow="Login")


