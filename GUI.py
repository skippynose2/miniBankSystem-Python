from appJar import gui
import ATM as ATM
app = gui()

#Input Feilds
app.startSubWindow("Login")
app.addLabelEntry("User Name")
app.addLabelSecretEntry("Password")

def Dep(btn):
    if btn == "Deposit":
        amount = app.getEntry("Amount")
        session = ATM.Control(app.getEntry("User Name"))
        session.Login(app.getEntry("Password"))
        session = ATM.Accounts(app.getEntry("User Name"))
        session.Deposit(float(amount))
        app.clearEntry("Amount")
    elif btn= "Withdraw":
        print("Withdraw function")
    else:
        app.stop()
    '''
    session = ATM.Control(app.getEntry("User Name"))
    session.Login(app.getEntry("Password"))
    session = ATM.Accounts(app.getEntry("User Name"))
    session.Deposit(x)
    '''

    
def Manager():
    app.startSubWindow("Account")
    app.addLabel("l1", "Press the button to close this window")
    # set the button's name to match the SubWindow's name
    app.addLabelEntry("Amount")
    app.addButtons(["Deposit", "Withdraw", "Close"], Dep)
    app.showSubWindow("Account", hide=True)

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
