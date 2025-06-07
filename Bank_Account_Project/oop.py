from bank_account import * 

Tayyaba = BankAccount(1000,"Tayyaba")
Sidra = BankAccount(2000,"Sidra")

Tayyaba.getBalance()
Sidra.getBalance()

Tayyaba.deposit(5000)
Sidra.withdraw(3000)

Tayyaba.transfer(3000,Sidra)

Mubashir = InterestRewardAcc(3000,"Mubashir")

Mubashir.getBalance() 

Mubashir.deposit(1000)

Mubashir.transfer(4000,Tayyaba)

Chand = SavingAcc(5000,"chand")

Chand.getBalance()

Chand.withdraw(4000)

Chand.transfer(1000)