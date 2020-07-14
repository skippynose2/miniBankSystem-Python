<<<<<<< HEAD
import pickle

account = {'holder':None}
money = {"holder": None}
loged = False
errorMessageForInput = "Please enter L,S,D,W,C,Q"
errorMessageForLogin = "Login in required"

def loadData():
    #load data code
    global account
    account = pickle.load(open("account.p", "rb"))
    global money
    money = pickle.load(open("money.p", "rb"))
    print("Data loaded")
    

def saveData():
    #save data code
    pickle.dump(account, open("account.p", "wb"))
    pickle.dump(money, open("money.p", "wb"))

def login():
    #login in code
    name = input('Your user name')
    print(name)
    code = input('Your password')
    realCode = account[name]
    if name not in account.values():
        if str(realCode) == str(code):
            print("Logged in as")
            #how you stop a global var from redefining itself
            global user
            user = name
            print(user)
            global loged
            loged = True
        else:
            print("Incorrect Password")
    else:
        print("eeeeeeeeeeeee")
        
    

def signup():
    #Signup code
    print("Sign up")
    username = input("Name:")
    password = input("Password")
    if username in account.values():
        account[username] = password
        money[username] = 0
    else:
        print("You already have an account")

def deposit():
    amount = input("Amount")
    finalAmount = money[user] + int(amount)
    money[user] = finalAmount
    print("Your current amount " + str(money[user]))

def WithDraw():
    amount = input("Amount")
    if money[user] - int(amount) < 0:
        print("You do not have enough money")
    else:
        curAmount = money[user]
        money[user] = curAmount - int(amount)
        print("Balance remaning " + str(money[user]))
    print(money)

def check():
    print("Bank balance " + str(money[user]))


loadData()
print("data loaded")


while True:
    user_input = input("L --> login, S -->Sign Up, D --> Deposit, W --> Withdraw, C --> Look at current amount, Q --> Quit")
    if user_input == "L":
        login()
    elif user_input == "S":
        signup()
    elif user_input == "D" and loged == True:
        deposit()
    elif user_input == "W" and loged == True:
        WithDraw()
    elif user_input == "C" and loged == True:
        check()
    elif user_input == "Q":
        saveData()
        break
    else:
        if loged == True:
            print(errorMessageForInput)
        else:
            print(errorMessageForLogin)

    

=======
#Database code should go up here
import productionDB as CDB
from productionDB import *
#Experimental code
print("From ATM.PY")
print(CDB.db)
print("FROM ATM")
'''one correct Procedure to do it
sql = "UPDATE ACCOUNTS SET AMOUNT = 5000 WHERE NAME='John'"
CDB.cursor.execute(sql)
CDB.db.commit()
'''
#This works too and it works better
'''CDB.Add("Akhil", 20000)
results = CDB.Fetch('Akhil')
CDB.NewAccount("Test", "TEST")
'''

class Control:
  Logged = False
  def __init__(self, userName):
    self.userName = userName
    
  def SignUp(self):
    userName = input("Your username")
    password = input("Your password")
    CDB.NewAccount(userName, password)
    self.Login(password)
    Control.Logged = True

  def Login(self, passwordGiven):
    results = CDB.Fetch(self.userName)
    if results != []:
      if results[0][0] == passwordGiven:
        print("Correct pass")
        Control.Logged = True
      else:
        password = input("Incorrect please try again")
        self.Login(password)
    else:
      print("does not exsit")
      self.SignUp()
  def SignOut(self):
    Control.Logged = False
    print("Signed out")


#need accounts to be child of Control
class Accounts(Control):
    
  def Deposit(self, amount):
    print(Control.Logged)
    if Control.Logged == True:
      results = CDB.Fetch(self.userName)
      newAmount = results[0][1] + amount
      CDB.Add(self.userName, newAmount)
  def WithDraw(self, amount):
    if Control.Logged == True:
      results = CDB.Fetch(self.userName)
      if results[0][1] - amount >= 0:
        newAmount = results[0][1] - amount
        CDB.Add(self.userName, newAmount)
      else:
        print("Not Enough Funds")
        



#Find way to actually allow user to interact with system
Initil = False
while 1 == 1:
  while Initil == False:
    UserName = input("User Name")
    Password = input("Password")
    session = Control(UserName)
    session.Login(Password)
    Initil = True
  session = Accounts(UserName)
  Actions = input("Type W to Withdraw funds and D to deposit funds")
  if Actions in ["d", "D"]:
    amount = int(input("How much do you want to deposit"))
    session.Deposit(amount)
  if Actions in ["W", 'w']:
    amount = int(input("How much do you want to Withdraw"))
    session.WithDraw(amount)
  if Actions in ['Q', 'q']:
    session.SignOut()
    break

'''session = Control('Akhil')
session.Login('1234')
session = Accounts('Akhil')
session.WithDraw(6000)
'''
>>>>>>> Bank accounts with database intergration
