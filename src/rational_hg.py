# class Money:
#     EXCHANGE = { "AMD": 1, "RUB": 5, "USD": 500, "EUR": 600 }
#     def __init__(self, crc, val):
#         self.currency = crc
#         self.amount = val
#
#     def __str__(self):
#         return "{} {}".format(self.amount, self.currency)
#
#     def __add__(self, other):
#         x = self.amount
#         if self.currency == other.currency:
#             x += other.amount
#         else:
#             rate = self.EXCHANGE[other.currency] / self.EXCHANGE[self.currency]
#             x += (rate * other.amount)
#         return Money(self.currency, x)
#
#     def __mul__(self, n):
#         return Money(self.currency, self.amount * n)
#
#     def valod(self, x):
#         print("Happy new year")
#
# # TEST
# m1 = Money('USD', 100)
# print("m1 =", m1)
# m2 = Money('EUR', 200)
# print("m2 =", m2)
# # m3 = Money("RUB", 10000)
# m1 + m2             # m1.__add__(m2)
# print("m1 + m2 = ", m1+m2)


####################################################################

class ValueError(Exception):
    def __init__(self, msg, val):
        self.__message = msg
        self.__value = val

    def get_info(self):
        return "{} value can't be {}".format(self.__message, self.__value)

    def get_value(self):
        return self.__value


class Rational:
    def __init__(self, n, d):
        try:
            if d == 0:
                raise ValueError("Denominator", d)
        except ValueError as err:
            print(err.get_info())
        else:
            self.nominator = n // self.gcd(n, d)
            self.denominator = d // self.gcd(n, d)

    def gcd (self, x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x

    def __repr__(self):
        return "{}/{}".format(self.nominator, self.denominator)


# User
Obj1 = Rational(4,2)
print(Obj1)

Obj2 = Rational(3,7)
print(Obj2)

Obj3 = Rational(5,0)
print(Obj3)
