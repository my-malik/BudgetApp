class Budget():
    def __init__(self,balance):
        self.balance = balance

    def __repr__(self):
        return f"This budget has £{self.balance} remaining."


    def withdraw(self, amount):
        self.balance -= amount
        return f"£{amount} withdrawn. New balance after withdraw is £{self.balance}"
        # return amount

    def deposit(self,amount):
        self.balance += amount
        return f"£{amount} deposited. New balance after deposit is £{self.balance}"
        # return amount


    def transferOut(self, transferOutAmount):
        self.balance -= transferOutAmount
        return f"£{transferOutAmount} transfered.£{self.balance} remaining."

    def transferIn(self, transferInAmount):
        self.balance += transferInAmount
        return f"£{transferInAmount} transfered.£{self.balance} remaining."
