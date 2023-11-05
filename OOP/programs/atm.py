#Below is a ATM software without GUI
#using oop

class Atm:
    def __init__(self):
        self.pin = 0
        self.balance = 0
        self.menu()
    
    def menu(self):
        user_in = int(input('''
        Enter your choice
        1. Set Pin
        2. Deposit
        3. Withdraw
        4. Check balance
        5. exit '''))

        while True:
            if user_in ==1:
                self.setPin()
            elif user_in == 2:
                self.deposit()
            elif user_in == 3:
                self.withdraw()
            elif user_in == 4:
                self.checkBalance()
            else:
                break

    def setPin(self):
        while True:
            self.pin = int(input('Enter your pin: '))
            if self.pin == int(input('Confirm your PIN: ')):
                break
            else:
                print('Pin does not match, Try again!')
    
    def deposit(self):
        if self.pin == int(input('Enter your pin: ')):
            dep = int(input('Enter the amount you want to deposit: '))
            self.balance += dep
            print('Operation Successful')
        else:
            print('Invalid PIN')


    def withdraw(self):
        if self.pin == int(input('Enter your pin: ')):
            wit = int(input('Enter the amount you want to withdraw: '))
            if wit< self.balance:
                self.balance -= wit
                print('Your money has been withdrawn successfully')
            else:
                print('Insufficient Funds')
        else:
            print('Invalid PIN')

    def checkBalance(self):
        if self.pin == int(input('Enter your pin: ')):
            print('Balance: ',self.balance)
        else:
            print('Invalid PIN')

