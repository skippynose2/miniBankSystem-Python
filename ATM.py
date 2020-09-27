#Database code should go up here
import productionDB as CDB
from productionDB import *
#Experimental code
print("From ATM.PY")
print(CDB.db)
print("FROM ATM")

class Control:
  Logged = False
  def __init__(self, userName):
    self.userName = userName
    self.LoggedInBroadCast = 1
    self.WrongPassword = 2
    self.NoAccountBroadCast = 3
    self.NotEnoughBroadCast = 4
    


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
        
def SignUp(userName, password):
  CDB.NewAccount(userName, password)


