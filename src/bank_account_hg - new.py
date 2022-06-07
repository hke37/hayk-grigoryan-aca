#Developer

from Person_hg import Customer
from money_hg import Money
from date_hg import Date
# from datetime import date, timedelta


class BankAccount:

    INTEREST_RATE = {"AMD": 10, "RUB": 5, "USD": 6, "EUR": 4}

    def __init__(self, p: Customer, a: Customer, m: Money, d: Date) -> None:
        self.__customer = p
        self.__account_number = a   #TODO: generate random 16-len string from digits
        #self.__account_currency = c
        self.__balance = m
        self.__valid_till = d
        #TODO: add other data members if you need

    def __str__(self):
        return "{}\naccount number - {}\nvalid till - {}\n{}".format(self.__customer, self.__account_number, self.__valid_till, self.__balance)

    # TODO: make transaction , check if balance is enough
    def deal(self, m):
        x = self.__balance - m
        self.__balance = x
        return x

    # TODO: fill your balance
    def fill_balance(self, m):
        x = self.__balance + m
        self.__balance = x
        return x

    # TODO: count many after duration with p percent
    def deposit (self, m, d, p=0):

        p = BankAccount.INTEREST_RATE[Money.get_currency(m)]
        interest_amount = m * p/100 * d * (1/365)
        income_tax = interest_amount * 0.1
        net_interest_amount = interest_amount - income_tax
        deposit_amount = m + net_interest_amount
        print("deposit amount will be: ")
        return deposit_amount


        # current_date = date.today().strftime("%Y-%m-%d")
        # print("current date is: ", current_date)
        # maturity_date = date.today() + timedelta(days=d)
        # print("maturity date is: ", maturity_date)



##############################
#USER

p = Customer("Valod", "Valodyan", 40, "Male", "AG0012233", "bloger", 10)
m = Money("USD", 200)
d = Date(2023, 6, 15)
a = p.acc_number
# c = m.currency

obj1 = BankAccount(p, a, m, d)
print(obj1)

m1 = Money("USD", 50)
f1 = obj1.fill_balance(m1)
print(f1)

m2 = Money("EUR",120)
t1 = obj1.deal(m2)
print(t1)

m3 = Money("RUB", 12000)
f2 = obj1.fill_balance(m3)
print(f2)

m5 = Money("USD", 1000)
d1 = obj1.deposit(m5,130)
print(d1)
