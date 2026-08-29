class Bank:
    def __init__(self, initialBalance = 0.0):
        self._balance = initialBalance
    def getBalance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        Penalty = 10
        if amount >  self._balance:
            self._balance -= Penalty
        else:
            self._balance -= amount
    
    def addInterest(self, rate):
        self._balance = self._balance * (1 + rate/100) 

