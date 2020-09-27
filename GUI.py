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
    elif btn == "Withdraw":
        amount = app.getEntry("Amount")
        session = ATM.Control(app.getEntry("User Name"))
        session.Login(app.getEntry("Password"))
        session = ATM.Accounts(app.getEntry("User Name"))
        session.WithDraw(float(amount))
        app.clearEntry("Amount")
        if session.WithDraw(float(amount)) == 4:
            print("Reeeeeee")
            app.addLabel("Not enough money")
            app.clearEntry("Amount")
    else:
        app.stop()

    
def Manager():
    app.startSubWindow("Account")
    app.addLabel("l1", "Press the button to close this window")
    # set the button's name to match the SubWindow's name
    app.addLabelEntry("Amount")
    app.addButtons(["Deposit", "Withdraw", "Close"], Dep)
    app.showSubWindow("Account", hide=True)

def ReTry():
    user = app.getEntry("User Name")
    session = ATM.Control(user)
    pwd = app.getEntry("Password")
    session.Login(pwd)
    if session.Login(pwd) == 2:
        app.addLabel("Wrong Password")
        ReTry()
    else:
        Manager()


def Sign():
    app.startSubWindow("SignUp")
    app.addLabel("Welcome create a account")
    app.addLabelEntry("Your User Name")
    app.addLabelEntry("Your Password")
    usr = app.getEntry("Your User Name")
    pwdd = app.getEntry("Your Password")
    app.addButton("CreateAccount", ATM.SignUp(usr, pwdd))
    app.showSubWindow("SignUp", hide=True)

def LoginBtn(button):
    if button == "Cancel":
        app.stop()
    elif button == "Submit":
        user = app.getEntry("User Name")
        session = ATM.Control(user)
        pwd = app.getEntry("Password")
        session.Login(pwd)
        if session.Login(pwd) == 1:
            Manager()
        elif session.Login(pwd) == 2:
           app.addLabel("Wrong Password")
           ReTry()       
    else:
        print('WTF')
        Sign()



app.addButtons(["Submit", "Cancel", "Sign Up"], LoginBtn)
app.go(startWindow="Login")
