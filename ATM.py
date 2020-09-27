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
    self.LoggedInBroadCast = 1
    self.WrongPassword = 2
    self.NoAccountBroadCast = 3
    self.NotEnoughBroadCast = 4
    
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
        return self.LoggedInBroadCast
      elif results[0][0] != passwordGiven:
        print("radlkfjlksdjf")
        return self.WrongPassword
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
        return self.NotEnoughBroadCast
        



#Find way to actually allow user to interact with system
'''
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

session = Control('Akhil')
session.Login('1234')
session = Accounts('Akhil')
session.WithDraw(6000)
'''

