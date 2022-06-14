class Money:
    EXCHANGE = { "AMD": 1, "RUB": 5, "USD": 500, "EUR": 600 }
    def __init__(self, crc, val):
        self.currency = crc
        self.amount = val

    def __str__(self):
        return "balance: {} {}".format(self.amount, self.currency)


    def get_currency(self):
        return self.currency

    def __add__(self, other):
        x = self.amount
        if self.currency == other.currency:
            x += other.amount
        else:
            rate = self.EXCHANGE[other.currency] / self.EXCHANGE[self.currency]
            x += (rate * other.amount)
        return Money(self.currency, x)

    def __sub__(self, other):
        x = self.amount
        rate = self.EXCHANGE[other.currency] / self.EXCHANGE[self.currency]

        if x - rate * other.amount >= 0:
            if self.currency == other.currency:
                x -= other.amount
            else:
                x -= (rate * other.amount)
        else:
            print("Your balance is not enough for transaction, please fill your balance first.")
        return Money(self.currency, x)


    def __mul__(self, n):
        if n > 0:
            x = self.amount * n
        elif n < 0:
            print("Not acceptable value for n")
        else:
            x = self.amount
        return Money(self.currency, round(x))


    def __truediv__(self, n):
        x = self.amount
        if n != 0:
            x = x / n
        else:
            print ("Value of n can't be zero")
        return Money(self.currency, round(x))


# TEST
m1 = Money('USD', 200)
# print("m1 =", m1)
#
m2 = Money('EUR', 150)
# print("m2 =", m2)
#
# # m3 = Money("RUB", 10000)
#
# # m1 + m2
print("m1 + m2 = ", m1 + m2)
#
# # m1 - m2
# print("m1 - m2 = ", m1 - m2)
#
# n = 15
# print("m1 * n = ", m1 * n)
# print("m1 / n = ", m1 / n)




