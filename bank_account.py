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