# Use the techniques of Section 1.7 to revise the charge and make payment methods of the CreditCard
# class to ensure that the caller sends a number as a parameter.

class CreditCard:

    def __init__(self,customer,bank,account,limit,balance = None):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        if balance == None:
            self._balance = 0
        else:
            self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self,price):
        if not isinstance(price, (int, float)):
            raise TypeError( "price must be numeric" )
        elif price < 0:
            raise ValueError( "price cannot be negative" )
        if (price + self._balance > self._limit):
            return False
        else:
            self._balance +=price
            return True

    def make_payment(self,amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("amount must be numeric" )
        elif amount < 0:
            raise ValueError( "amount cannot be negative" )
        self._balance-=amount

cc = CreditCard('Sam','Chase',101,500)
print("customer: ",cc.get_customer())
print("bank: ", cc.get_bank())
print("account: ",cc.get_account())
print("limit: ",cc.get_limit())
print("balance: ",cc.get_balance())

charged = cc.charge(100)
print(charged)
print("balance: ",cc.get_balance())

cc.make_payment(20)
print("balance: ",cc.get_balance())

cc1 = CreditCard('Sampa','Chase',102,500,100)
print("customer: ",cc1.get_customer())
print("bank: ", cc1.get_bank())
print("account: ",cc1.get_account())
print("limit: ",cc1.get_limit())
print("balance: ",cc1.get_balance())
