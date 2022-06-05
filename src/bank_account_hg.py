from Person_hg import Customer
from money_hg import Money
from date_hg import Date
from datetime import date,timedelta


class BankAccount:
    def __init__(self, p : Customer, a: Customer, c: Money, m: Money, d: Date) -> None:
        self.__customer = p
        self.__account_number = a        #TODO: generate random 16-len string from digits
        self.__account_currency = c
        self.__balance = m
        self.__valid_till = d
        #TODO: add other data members if you need

    def __str__(self):
        return "{}\naccount number - {}\nvalid till - {}\n{}".format(self.__customer, self.__account_number, self.__valid_till, self.__balance)


    # TODO: make transaction , check if balance is enough
    def deal(self, c, m):
        m = Money(c, m)
        x = Money.__sub__(self.__balance, m)
        self.__balance = x
        return x

    # TODO: fill your balance
    def fill_balance(self, c, m):
        m = Money(c, m)
        x = Money.__add__(self.__balance, m)
        self.__balance = x
        return x

    # TODO: count many after duration with p percent
    def deposit(self, m, d, c, p = 0):

        INTEREST_RATE = {"AMD": 10, "RUB": 5, "USD": 6, "EUR": 4}

        m = int(input('Enter the amount to deposit: '))
        d = int(input('Enter how many days you want to deposit: '))
        c = str(input('Enter currency of deposit: '))
        p = INTEREST_RATE[c]

        current_date = date.today().strftime("%Y-%m-%d")
        print("current date is: " + current_date)
        maturity_date = date.today() + timedelta(days = d)
        print("maturity date is: ", maturity_date)

        Interest_amount = m * p/100 * d * (1/365)
        Income_tax = Interest_amount * 0.1
        Net_interest_amount = Interest_amount - Income_tax
        Deposit_amount = m + Net_interest_amount
        print("deposit amount will be: ")
        return round(Deposit_amount,2)




p = Customer("Valod", "Valodyan", 40, "Male", "AG0012233", "bloger", 10)
m = Money("USD", 200)
d = Date(2023,6,15)
a = p.acc_number
c = m.currency

obj1 = BankAccount(p, a, c, m, d)
print(obj1)

f1 = obj1.fill_balance("RUB", 10000)
print(f1)

t1 = obj1.deal("RUB", 10000)
print(t1)

f2 = obj1.fill_balance("EUR", 100)
print(f2)

t2 = obj1.deal("USD", 321)
print(t2)

d1 = obj1.deposit(m,d,c)
print(d1)
