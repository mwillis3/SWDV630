#-------------------------------------------------------------------------------
# author: Marcelious Willis
# sem   : Summer 2020
# class : SWDV-630 Object-oriented programming
# @file : CheckingAccount.py
#-------------------------------------------------------------------------------
class CheckingAccount:
    def __init__(self, name, address, account_num):
        self.name = name
        self.address = address
        self.accnum = account_num
        self._balance = float(0)
        print("Hello " + self.name + "! Welcome to your Checking Account!")

    def credit(self):
        amount = float(input("How much would you like to deposit today? "))
        self._balance += amount
        print("\nAmount deposited: " + str(amount))

    def debit(self):
        amount = float(input("How much would you like to withdraw? "))
        if self._balance >= amount:
            self._balance -= amount
            print("\nWithdrawing " + str(amount))
        else:
            print("Insufficient funds, please check your balance \n")

    def check_balance(self):
        print("Your balance is: " + str(self._balance) + "\n")

#-------------------------------------------------------------------------------
# Driver application
#-------------------------------------------------------------------------------

# Create an instance of the CheckingAccount class
myaccount = CheckingAccount("Nancy","1428 Elm Street",123456)
myaccount.check_balance()

# Woohoo! Just got paid!
myaccount.credit()
myaccount.check_balance()

# Need some cash now
myaccount.debit()
myaccount.check_balance()        