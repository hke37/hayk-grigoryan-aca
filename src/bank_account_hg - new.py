#Developer
from Person_hg import Customer
from money_hg import Money
from date_hg import Date

class BankAccount:

    INTEREST_RATE = {"AMD": 10, "RUB": 5, "USD": 6, "EUR": 4}

    def __init__(self, p: Customer, m: Money, d: Date) -> None:
        self.__customer = p
        self.__balance = m
        self.__valid_till = d

    def __str__(self):
        return "{}\nvalid till - {}\n{}".format(self.__customer, self.__valid_till, self.__balance)

    # TODO: make transaction , check if balance is enough
    def deal(self, m):
        self.__balance = self.__balance - m
        return self.__balance

    # TODO: fill your balance
    def fill_balance(self, m):
        self.__balance = self.__balance + m
        return self.__balance

    # TODO: count many after duration with p percent
    def deposit (self, m, d, dt, p=1):

        print("start date is :", dt)
        end_date = dt.add_day(d)
        print("maturity date is :", dt)

        """Interest rate is different for different currencies
        Income tax on deposit is 10% regardless currency
        """

        p = BankAccount.INTEREST_RATE[m.get_currency()]
        interest_amount = m * p/100 * d * (1/365)
        income_tax = interest_amount * 0.1
        net_interest_amount = interest_amount - income_tax
        deposit_amount = m + net_interest_amount
        print("deposit amount will be: ")
        return deposit_amount


##############################
#USER

p = Customer("Valod", "Valodyan", 40, "Male", "AG0012233", "bloger", 10)
m = Money("USD", 200)
d = Date(2023, 6, 15)
# a = p.acc_number
# c = m.currency

obj1 = BankAccount(p, m, d)
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

m5 = Money("EUR", 1500)
d5 = Date(2022, 7, 18)
d1 = obj1.deposit(m5, 150, d5)
print(d1)
