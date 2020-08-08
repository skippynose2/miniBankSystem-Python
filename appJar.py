from appJar import gui

app = gui()

#Input Feilds
app.addLabelEntry("User Name")
app.addLabelSecretEntry("Password")

def LoginBtn(button):
    if button == "Cancel":
        app.stop()

    else:
        username = app.getEntry("User Name")
        password = app.getEntry("Password")
        print(username)
        print(password)


app.addButtons(["Login", "Cancel"], LoginBtn)    
app.go()
#####
