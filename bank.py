def withdraw(w):
    global balance
    balance-=w
    print("Withdrawn successfully.Go back to the main menu to view balance.")
def deposit(d):
    global balance
    balance+=d
    print("Desposited successfully>>>")
def checkbalance():
    print("Your balance is:"balance)
def end_transaction():
    quit()



balance=20000
print("*****RRR BANK*****)

while True:
    print("
