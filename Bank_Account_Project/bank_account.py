class BalanceException(Exception): 
    pass
class BankAccount: 
    def __init__(self,initialAmount,accName): 
        self.balance = initialAmount
        self.name = accName
        print(f"\n Account '{self.name} created.\n Balance = ${self.balance:.2f}")
    def getBalance(self): 
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    def deposit(self,amount): 
        self.balance = self.balance + amount 
        print("\n deposited completed.")
        self.getBalance()
    
    def viableTransaction(self,amount): 
        if self.balance >= amount: 
            return
        else: 
            raise BalanceException(f"Sorry , account '{self.name}' has only a balance of '${self.balance}'")
    def withdraw(self,amount): 
        try: 
            self.viableTransaction(amount)
            self.balance = self.balance - amount        
            print("\n Withdraw complted.") 
            self.getBalance()
        except BalanceException as error: 
            print(f'\n Withdraw interrupted : {error}')

    def transfer(self,amount,account): 
        try: 
            print('\n***********\n\n Beginning Transfer....🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('Transfer Completed!✅\n\n**********')
        except BalanceException as error: 
            print(f'\nTransfer interrupted.❌ {error}')

class InterestRewardAcc(BankAccount): 
    def deposit(self,amount): 
        self.balance = self.balance + (amount * 1.05)
        print("\n Deposit completed.")
        self.getBalance()

class SavingAcc(InterestRewardAcc):
    def __init__(self,initialAmount,acctName):
        super().__init__(initialAmount,acctName)
        self.fees = 5
    
    def withdraw(self, amount):
        try: 
            self.viableTransaction(amount)
            self.balance = self.balance - (amount + self.fees)
            print("\n Withdraw Completed. ")
            self.getBalance()
        except BalanceException as error: 
            print("\n withdraw intrrupted : {error}")