class User:
    def __init__(self,name,email):
        self.name = name
        self.email= email
        self.account = {
            "Checking" : BankAccount(0.02,0),
            "Saving" : BankAccount(0.05,5000)
        }
    def _user_balance(self):
        print(f"User:{self.name}, Checking Balance:{self.account['Checking'].display_account_info()}")
        print(f"User:{self.name}, Saving Balance:{self.account['Saving'].display_account_info()}")

    # def transfer_money(self,amount,ouser):
    #     self.account.account_balance -= amount
    #     ouser.account.account_balance += amount
    #     self._user_balance()
    #     ouser._user_balance()


class BankAccount:
    account_balance = 0
    accounts =[]
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        self.account_balance -= amount
        if self.account_balance < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self
    def display_account_info(self):
        return f"${self.account_balance}"
        
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += self.account_balance * self.int_rate
        else:
            print("false")
        return self
    @classmethod
    def print_all_accounts(cls):
        for accounts in cls.accounts:
            accounts.display_account_info()


mondo = User("mondoman","mondosemail@myemail.com")
mondo.account['Checking'].deposit(100000000)
mondo.account['Saving'].deposit(200)
mondo._user_balance()